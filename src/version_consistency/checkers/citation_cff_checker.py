import logging
from argparse import Namespace
from pathlib import Path

import packaging.version

from version_consistency.extractors.citation_cff_extractor import (
    extract_citation_cff_version,
)
from version_consistency.utils import log_missing_file, parse_version_pep440

logger = logging.getLogger(__name__)


def check_citation_cff(tag_version_str: str, tag_version_pep440: packaging.version.Version, cli_args: Namespace):
    if Path(cli_args.citation_cff_path).exists():
        citation_cff_version = extract_citation_cff_version(cli_args.citation_cff_path)
        citation_cff_v = parse_version_pep440(citation_cff_version)
        if tag_version_pep440 != citation_cff_v:
            logger.error(f"❌ Version mismatch: {cli_args.citation_cff_path or 'CITATION.cff'} {citation_cff_version} != tag {tag_version_str}")
    else:
        msg = f"citation_cff_path file does not exist: {cli_args.citation_cff_path or 'CITATION.cff'}"
        log_missing_file(logger=logger, msg=msg, cli_args=cli_args)