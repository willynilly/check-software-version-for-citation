import logging
from argparse import Namespace
from pathlib import Path

import packaging.version

from version_consistency.extractors.zenodo_json_extractor import (
    extract_zenodo_json_version,
)
from version_consistency.utils import log_missing_file, parse_version_pep440

logger = logging.getLogger(__name__)

def check_zenodo_json(tag_version_str:str, tag_version_pep440: packaging.version.Version, cli_args: Namespace):    
    if Path(cli_args.zenodo_json_path).exists():
        zenodo_version = extract_zenodo_json_version(cli_args.zenodo_json_path)
        zenodo_v = parse_version_pep440(zenodo_version)
        if tag_version_pep440 != zenodo_v:
            logger.error(f"❌ Version mismatch: {cli_args.zenodo_json_path or '.zenodo.json'} {zenodo_version} != tag {tag_version_str}")
    else:
        msg = f"zenodo_json_path file does not exist: {cli_args.zenodo_json_path or '.zenodo.json'}"
        log_missing_file(logger, msg=msg, cli_args=cli_args)