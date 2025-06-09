import logging
import re
import sys

logger = logging.getLogger(__name__)


def extract_tag_version(event_name: str, ref: str | None, release_tag: str | None) -> str:
    if event_name == 'push':
        if not ref:
            logger.error("❌ Missing GitHub ref (for push)")
            sys.exit(1)
        match = re.match(r'refs/tags/v(.+)', ref)
        if not match:
            logger.error(f"❌ Unexpected ref format for push: {ref}")
            sys.exit(1)
        version = str(match.group(1))            
        logger.info(f"📦 Detected push tag version: {version}")
        return version
    elif event_name == 'release':
        if not release_tag:
            logger.error("❌ Missing GitHub release tag name (for release)")
            sys.exit(1)
        version = release_tag.lstrip('v')
        logger.info(f"📦 Detected release tag version: {version}")
        return version
    else:
        logger.error(f"❌ Unsupported event: {event_name}")
        sys.exit(1)