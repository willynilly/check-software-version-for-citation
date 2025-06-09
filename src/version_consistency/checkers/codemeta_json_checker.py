import logging
from argparse import Namespace
from pathlib import Path

import packaging.version

from version_consistency.extractors.codemeta_json_extractor import (
    extract_codemeta_json_version,
)
from version_consistency.utils import log_missing_file, parse_version_pep440

logger = logging.getLogger(__name__)

def check_codemeta_json(tag_version_str:str, tag_version_pep440: packaging.version.Version, cli_args: Namespace):
    if Path(cli_args.codemeta_json_path).exists():
            codemeta_version = extract_codemeta_json_version(cli_args.codemeta_json_path)
            codemeta_v = parse_version_pep440(codemeta_version)
            if tag_version_pep440 != codemeta_v:
                logger.error(f"❌ Version mismatch: {cli_args.codemeta_json_path or 'codemeta.json'} {codemeta_version} != tag {tag_version_str}")
    else:
        msg = f"codemeta_json_path file does not exist: {cli_args.codemeta_json_path or 'codemeta.json'}"
        log_missing_file(logger=logger, msg=msg, cli_args=cli_args)