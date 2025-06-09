import logging
from argparse import Namespace

from same_version.extractors.extractor import Extractor

logger = logging.getLogger(__name__)

class CliExtractor(Extractor):
    
    def __init__(self, cli_args: Namespace):
        self._cli_args = cli_args

    def extract_version(self) -> str | None:
        if self.target_exists:
            return self._cli_args.base_version
        else:
            return None
    
    @property
    def target_exists(self) -> bool:
        return hasattr(self._cli_args, 'base_version') and self._cli_args.base_version is not None
    
    @property
    def target_name(self) -> str | None:
        return 'CLI parameter'
    
    @property
    def target_cli_parameter_name(self) -> str | None:
        return '--base-version'