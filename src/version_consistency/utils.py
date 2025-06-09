from argparse import Namespace

import packaging.version
import semver


def parse_version_pep440(v: str) -> packaging.version.Version:
    return packaging.version.Version(v)

def parse_version_semver(v: str) -> semver.Version:
    return semver.Version.parse(v)

def log_missing_file(logger, msg: str, cli_args: Namespace):
    if cli_args.fail_for_missing_file.lower() == 'true':
        msg = "❌ " + msg
        logger.error(msg)
    else:
        msg = "⚠️ " + msg
        logger.warning(msg)