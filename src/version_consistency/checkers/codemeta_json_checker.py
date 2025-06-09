import logging
from argparse import Namespace

from version_consistency.checkers.file_checker import FileChecker
from version_consistency.extractors.codemeta_json_extractor import CodeMetaJsonExtractor

logger = logging.getLogger(__name__)

class CodeMetaJsonChecker(FileChecker):

    def __init__(self, extractor: CodeMetaJsonExtractor, cli_args: Namespace):
        super().__init__(extractor=extractor, cli_args=cli_args)   