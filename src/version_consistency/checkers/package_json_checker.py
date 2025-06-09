import logging
from argparse import Namespace
from pathlib import Path

import packaging.version

from version_consistency.extractors.package_json_extractor import (
    extract_package_json_version,
)
from version_consistency.utils import log_missing_file, parse_version_semver

logger = logging.getLogger(__name__)

def check_package_json(tag_version_pep440:packaging.version.Version, cli_args: Namespace):
    if Path(cli_args.package_json_path).exists():
        package_version = extract_package_json_version(cli_args.package_json_path)
        try:
            tag_semver_str = f"{tag_version_pep440.major}.{tag_version_pep440.minor}.{tag_version_pep440.micro}"
            if tag_version_pep440.is_prerelease and tag_version_pep440.pre is not None:
                tag_semver_str += f"-{tag_version_pep440.pre[0]}.{tag_version_pep440.pre[1]}"

            tag_semver = parse_version_semver(tag_semver_str)
            package_v = parse_version_semver(package_version)

            if tag_semver != package_v:
                logger.error(f"Version mismatch: {cli_args.package_json_path or 'package.json'} {package_version} != tag {tag_semver_str}")
        except Exception as e:
            logger.error(f"❌ Parse error: Could not parse tag version as SemVer for {cli_args.package_json_path or 'package.json'}: {e}")
    else:
        msg = f"package_json_path file does not exist: {cli_args.package_json_path or 'package.json'}"
        log_missing_file(logger=logger, msg=msg, cli_args=cli_args)
