import logging
from argparse import Namespace

import packaging.version

from version_consistency.extractors.extractor import Extractor
from version_consistency.utils import parse_version_pep440

logger = logging.getLogger(__name__)

class Checker():

    def __init__(self, extractor: Extractor, cli_args: Namespace):
        self.extractor = extractor        
        self.cli_args = cli_args

    def create_pep440_version(self, version_str: str | None) -> packaging.version.Version | None:
        version_pep440 : packaging.version.Version | None = parse_version_pep440(version_str)
        return version_pep440
    
    @property
    def target_version_str(self) -> str | None:
        return self.extractor.extract_version()
    
    @property
    def target_version_pep440(self) -> packaging.version.Version | None:
        return self.create_pep440_version(version_str=self.target_version_str)
    
    @property
    def target_exists(self) -> bool:
        return self.extractor.target_exists

    @property    
    def target_name(self) -> str | None:
        return self.extractor.target_name
    
    @property
    def target_cli_parameter_name(self) -> str | None:
        return self.extractor.target_cli_parameter_name
    
    def check(self, base_version_str: str | None) -> bool:
        if not base_version_str:
                return True
        base_version_pep440 = self.create_pep440_version(version_str=base_version_str)
        if self.target_exists:

            if base_version_pep440 != self.target_version_pep440:
                self._log_version_mismatch(base_version_str=base_version_str)
                return False
            else:
                return True
        else:
            self._log_missing_target()
            return False

    def _log_version_mismatch(self, base_version_str: str | None):
        logger.error(f"❌ Version mismatch: {self.target_name} {self.target_version_str} != base_version {base_version_str}")

    def _log_missing_target(self, msg: str | None = None):
        if msg is None:
            msg = f"Data source for parameter {self.target_cli_parameter_name} does not exist: {self.target_name}"

        if self.cli_args.fail_for_missing_file.lower() == 'true':
            msg = "❌ " + msg
            logger.error(msg)
        else:
            msg = "⚠️ " + msg
            logger.warning(msg)
     


