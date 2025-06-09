import logging
from argparse import Namespace

from version_consistency.extractors.toml_extractor import TomlExtractor

logger = logging.getLogger(__name__)

class PyprojectTomlExtractor(TomlExtractor):

    def __init__(self, cli_args: Namespace):
        super().__init__(
            target_file_path=cli_args.pyproject_toml_path, 
            default_target_name="pyproject.toml", 
            target_cli_parameter_name="pyproject_toml_path"
        )
    
    def _get_version_from_data(self, data: dict) -> str | None:
        project = data.get('project', {})
        version = project.get('version')
        return version
    
    def _log_missing_version_error(self, data: dict):
        logger.error(f"❌ {self.target_name} missing [project] version!")
