import logging
from argparse import Namespace
from pathlib import Path

import packaging.version

from version_consistency.extractors.setup_py_extractor import extract_setup_py_version
from version_consistency.utils import log_missing_file, parse_version_pep440

logger = logging.getLogger(__name__)

def check_setup_py(tag_version_str:str, tag_version_pep440: packaging.version.Version, cli_args: Namespace):
    if Path(cli_args.setup_py_path).exists():
        setup_py_version = extract_setup_py_version(cli_args.setup_py_path)
        setup_py_v = parse_version_pep440(setup_py_version)
        if tag_version_pep440 != setup_py_v:
            logger.error(f"❌ Version mismatch: {cli_args.setup_py_path or 'setup.py'} {setup_py_version} != tag {tag_version_str}")
    else:
        msg = f"setup_py_path file does not exist: {cli_args.setup_py_path or 'setup.py'}"
        log_missing_file(logger=logger, msg=msg, cli_args=cli_args)