import logging
from argparse import Namespace
from pathlib import Path

import packaging.version

from version_consistency.extractors.pyproject_toml_extractor import (
    extract_pyproject_toml_version,
)
from version_consistency.utils import log_missing_file, parse_version_pep440

logger = logging.getLogger(__name__)


def check_pyproject_toml(tag_version_str: str, tag_version_pep440: packaging.version.Version, cli_args: Namespace):
    if Path(cli_args.pyproject_toml_path).exists():
        pyproject_version = extract_pyproject_toml_version(cli_args.pyproject_toml_path)
        pyproject_v = parse_version_pep440(pyproject_version)
        if tag_version_pep440 != pyproject_v:
            logger.error(f"❌ Version mismatch: {cli_args.pyproject_toml_path or 'pyproject.toml'} {pyproject_version} != tag {tag_version_str}")
    else:
        msg = f"pyproject_toml_path file does not exist: {cli_args.pyproject_toml_path or 'pyproject.toml'}"
        log_missing_file(logger=logger, msg=msg, cli_args=cli_args)