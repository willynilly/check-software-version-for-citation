#!/usr/bin/env python3

import argparse
import logging
import sys

import packaging.version

from version_consistency.checkers.citation_cff_checker import check_citation_cff
from version_consistency.checkers.codemeta_json_checker import check_codemeta_json
from version_consistency.checkers.package_json_checker import check_package_json
from version_consistency.checkers.pyproject_toml_checker import check_pyproject_toml
from version_consistency.checkers.setup_py_checker import check_setup_py
from version_consistency.checkers.zenodo_json_checker import check_zenodo_json
from version_consistency.extractors.tag_extractor import extract_tag_version
from version_consistency.log_collector import get_log_collector
from version_consistency.utils import (
    parse_version_pep440,
)

logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check tag/release version vs files with canonical PEP 440 tag version")
    parser.add_argument('--check-citation-cff', required=True, help='Check CITATION.cff? (true/false)')
    parser.add_argument('--citation-cff-path', required=True, help='Path to CITATION.cff file')
    parser.add_argument('--check-pyproject-toml', required=True, help='Check pyproject.toml? (true/false)')
    parser.add_argument('--pyproject-toml-path', required=True, help='Path to pyproject.toml file')
    parser.add_argument('--check-codemeta-json', required=True, help='Check codemeta.json? (true/false)')
    parser.add_argument('--codemeta-json-path', required=True, help='Path to codemeta.json')
    parser.add_argument('--check-zenodo-json', required=True, help='Check .zenodo.json? (true/false)')
    parser.add_argument('--zenodo-json-path', required=True, help='Path to .zenodo.json')
    parser.add_argument('--check-package-json', required=True, help='Check package.json? (true/false)')
    parser.add_argument('--package-json-path', required=True, help='Path to package.json')
    parser.add_argument('--check-setup-py', required=True, help='Check setup.py? (true/false)')
    parser.add_argument('--setup-py-path', required=True, help='Path to setup.py')
    parser.add_argument('--event-name', required=True, help='GitHub event name (push or release)')
    parser.add_argument('--ref', required=False, help='GitHub ref (for push)')
    parser.add_argument('--release-tag', required=False, help='GitHub release tag name (for release)')
    return parser.parse_args()

# --- Main ---

def main():
    cli_args: argparse.Namespace = parse_args()

    tag_version_str: str = extract_tag_version(cli_args.event_name, cli_args.ref, cli_args.release_tag)
    tag_version_pep440: packaging.version.Version = parse_version_pep440(tag_version_str)

    # CITATION.cff
    if cli_args.check_citation_cff.lower() == 'true':
        check_citation_cff(tag_version_str=tag_version_str, tag_version_pep440=tag_version_pep440, cli_args=cli_args)

    # pyproject.toml
    if cli_args.check_pyproject_toml.lower() == 'true':
        check_pyproject_toml(tag_version_str=tag_version_str, tag_version_pep440=tag_version_pep440, cli_args=cli_args)

    # setup.py
    if cli_args.check_setup_py.lower() == 'true':
        check_setup_py(tag_version_str=tag_version_str, tag_version_pep440=tag_version_pep440, cli_args=cli_args)


    # package.json
    if cli_args.check_package_json.lower() == 'true':
        check_package_json(tag_version_pep440=tag_version_pep440, cli_args=cli_args)
        
    # codemeta.json
    if cli_args.check_codemeta_json.lower() == 'true':
        check_codemeta_json(tag_version_str=tag_version_str, tag_version_pep440=tag_version_pep440, cli_args=cli_args)

    # .zenodo.json
    if cli_args.check_zenodo_json.lower() == 'true':
        check_zenodo_json(tag_version_str=tag_version_str, tag_version_pep440=tag_version_pep440, cli_args=cli_args)


    # Final result
    
    if get_log_collector().get_error_logs():
        sys.exit(1)
    else:
        logger.info("✅ All versions match!")

if __name__ == '__main__':
    main()
