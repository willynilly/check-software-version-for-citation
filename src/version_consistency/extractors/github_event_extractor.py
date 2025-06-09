import logging
import re
from argparse import Namespace

from version_consistency.extractors.extractor import Extractor

logger = logging.getLogger(__name__)

class GitHubEventExtractor(Extractor):
    
    def __init__(self, cli_args: Namespace):
        super().__init__()
        self._data: dict[str, str | None] = {
            'github_event_name': cli_args.github_event_name, 
            'github_event_ref': cli_args.github_event_ref, 
            'github_event_release_tag': cli_args.github_event_release_tag
        }

    def target_exists(self) -> bool:
        return self._data is not None and self._data['github_event_name'] is not None
    
    def target_name(self) -> str | None:
        return self._data['github_event_name']
    
    def target_cli_parameter_name(self) -> str | None:
        return '--github-event-name'

    def _get_data(self) -> dict[str, str | None]:
        return self._data
    
    def _get_version_from_data(self, data: dict) -> str | None:
        event_name: str | None = data.get('github_event_name', None)
        ref: str | None = data.get('github_event_ref', None)
        release_tag: str | None = data.get('github_event_release_tag', None)

        if event_name == 'push':
            if not ref:
                logger.error("❌ Missing GitHub ref (for push)")
                return None
            match = re.match(r'refs/tags/v(.+)', str(ref))
            if not match:
                logger.error(f"❌ Unexpected GitHub ref format for push: {ref}")
                return None
            version = str(match.group(1))            
            logger.info(f"📦 Detected GitHub push tag version: {version}")
            return version
        elif event_name == 'release':
            if not release_tag:
                logger.error("❌ Missing GitHub release tag name (for release)")
                return None
            version = str(release_tag).lstrip('v')
            logger.info(f"📦 Detected GitHub release tag version: {version}")
            return version
        elif event_name == 'pull_request':
            return None
        else:
            logger.error(f"❌ Unsupported GitHub event: {event_name}")
            return None