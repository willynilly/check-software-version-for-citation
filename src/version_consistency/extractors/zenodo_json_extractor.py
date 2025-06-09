import logging
from argparse import Namespace

from version_consistency.extractors.json_extractor import JsonExtractor

logger = logging.getLogger(__name__)

class ZenodoJsonExtractor(JsonExtractor):

    def __init__(self, cli_args: Namespace):
        super().__init__(
            target_file_path=cli_args.zenodo_json_path, 
            default_target_name=".zenodo.json", 
            target_cli_parameter_name="zenodo_json_path"
        )

    def _get_version_from_data(self, data: dict) -> str | None:
        version = data.get('version')
        return version