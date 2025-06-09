import logging
from argparse import Namespace

from version_consistency.checkers.file_checker import FileChecker
from version_consistency.extractors.citation_cff_extractor import (
    CitationCffExtractor,
)

logger = logging.getLogger(__name__)


class CitationCffChecker(FileChecker):

    def __init__(self, extractor: CitationCffExtractor, cli_args: Namespace):
        super().__init__(extractor=extractor, cli_args=cli_args)        
    
