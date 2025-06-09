import logging
import sys
from argparse import Namespace

import yaml

from version_consistency.extractors.file_extractor import FileExtractor

logger = logging.getLogger(__name__)

class CitationCffExtractor(FileExtractor):

    def __init__(self, cli_args: Namespace):
        super().__init__(
            target_file_path=cli_args.citation_cff_path, 
            default_target_name="CITATION.cff", 
            target_cli_parameter_name="--citation-cff-path"
        )
    
    def extract_version(self) -> str:
        with open(self.target_file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        version = data.get('version')
        if not version:
            logger.error(f"❌ {self.target_name} missing 'version' field!")
            sys.exit(1)
        logger.info(f"📖 {self.target_name} version: {version}")
        return version