#!/usr/bin/env python3

import argparse
import os
import sys
import yaml
import tomli
import json
import re
import subprocess
from packaging.version import Version as PEP440Version
import semver

def parse_args():
    parser = argparse.ArgumentParser(description="Check tag/release version vs files with canonical PEP 440 tag version")
    parser.add_argument('--cff-path', required=True, help='Path to CITATION.cff file')
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

def extract_tag_version(event_name, ref, release_tag):
    if event_name == 'push':
        match = re.match(r'refs/tags/v(.+)', ref)
        if not match:
            print(f"❌ Unexpected ref format for push: {ref}")
            sys.exit(1)
        version = match.group(1)
        print(f"📦 Detected push tag version: {version}")
        return version
    elif event_name == 'release':
        version = release_tag.lstrip('v')
        print(f"📦 Detected release tag version: {version}")
        return version
    else:
        print(f"❌ Unsupported event: {event_name}")
        sys.exit(1)

def parse_version_pep440(v):
    return PEP440Version(v)

def parse_version_semver(v):
    return semver.Version.parse(v)

# --- Extractors ---

def extract_cff_version(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    version = data.get('version')
    if not version:
        print(f"❌ {path or 'CITATION.cff'} missing 'version' field!")
        sys.exit(1)
    print(f"📖 {path or 'CITATION.cff'} version: {version}")
    return version

def extract_pyproject_toml_version(path):
    with open(path, 'rb') as f:
        data = tomli.load(f)
    project = data.get('project', {})
    version = project.get('version')
    if not version:
        print(f"❌ {path or 'pyproject.toml'} missing [project] version!")
        sys.exit(1)
    print(f"📖 {path or 'pyproject.toml'} version: {version}")
    return version

def extract_codemeta_json_version(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    version = data.get('version')
    if not version:
        print(f"❌ {path or 'codemeta.json'} missing 'version' field!")
        sys.exit(1)
    print(f"📖 {path or 'codemeta.json'} version: {version}")
    return version

def extract_zenodo_json_version(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    version = data.get('version')
    if not version:
        print(f"❌ {path or '.zenodo.json'} missing 'version' field!")
        sys.exit(1)
    print(f"📖 {path or '.zenodo.json'} version: {version}")
    return version

def extract_package_json_version(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    version = data.get('version')
    if not version:
        print(f"❌ {path or 'package.json'} missing 'version' field!")
        sys.exit(1)
    print(f"📖 {path or 'package.json'} version: {version}")
    return version

def extract_setup_py_version(path):
    try:
        output = subprocess.check_output(['python', path, '--version'], stderr=subprocess.STDOUT)
        version = output.decode('utf-8').strip()
        print(f"📖 {path or 'setup.py'} version: {version}")
        return version
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {path or 'setup.py'} --version:\n{e.output.decode('utf-8')}")
        sys.exit(1)

# --- Main ---

def main():
    args = parse_args()

    tag_version_str = extract_tag_version(args.event_name, args.ref, args.release_tag)
    tag_version_pep440 = parse_version_pep440(tag_version_str)

    failures = []

    # CITATION.cff
    citation_version = extract_cff_version(args.cff_path)
    citation_v = parse_version_pep440(citation_version)
    if tag_version_pep440 != citation_v:
        print(f"❌ Version mismatch with {args.cff_path or 'CITATION.cff'}!")
        failures.append(f"{args.cff_path or 'CITATION.cff'}")

    # pyproject.toml
    if args.check_pyproject_toml.lower() == 'true':
        pyproject_version = extract_pyproject_toml_version(args.pyproject_toml_path)
        pyproject_v = parse_version_pep440(pyproject_version)
        if tag_version_pep440 != pyproject_v:
            print(f"❌ Version mismatch with {args.pyproject_toml_path or 'pyproject.toml'}!")
            failures.append(f"{args.pyproject_toml_path or 'pyproject.toml'}")

    # setup.py
    if args.check_setup_py.lower() == 'true':
        setup_version = extract_setup_py_version(args.setup_py_path)
        setup_v = parse_version_pep440(setup_version)
        if tag_version_pep440 != setup_v:
            print(f"❌ Version mismatch with {args.setup_py_path or 'setup.py'}!")
            failures.append(f"{args.setup_py_path or 'setup.py'}")

    # package.json
    if args.check_package_json.lower() == 'true':
        package_version = extract_package_json_version(args.package_json_path)
        try:
            tag_semver = parse_version_semver(f"{tag_version_pep440.major}.{tag_version_pep440.minor}.{tag_version_pep440.micro}")
            if tag_version_pep440.is_prerelease:
                tag_semver = semver.Version.parse(f"{tag_semver.major}.{tag_semver.minor}.{tag_semver.patch}-{tag_version_pep440.pre[0]}.{tag_version_pep440.pre[1]}")
            package_v = parse_version_semver(package_version)
            if tag_semver != package_v:
                print(f"❌ Version mismatch with {args.package_json_path or 'package.json'}!")
                failures.append(f"{args.package_json_path or 'package.json'}")
        except Exception as e:
            print(f"⚠️ Could not parse tag version as SemVer: {e}")
            failures.append(f"{args.package_json_path or 'package.json'} (parse error)")

    # codemeta.json
    if args.check_codemeta_json.lower() == 'true':
        codemeta_version = extract_codemeta_json_version(args.codemeta_json_path)
        codemeta_v = parse_version_pep440(codemeta_version)
        if tag_version_pep440 != codemeta_v:
            print(f"❌ Version mismatch with {args.codemeta_json_path or 'codemeta.json'}!")
            failures.append(f"{args.codemeta_json_path or 'codemeta.json'}")

    # .zenodo.json
    if args.check_zenodo_json.lower() == 'true':
        zenodo_version = extract_zenodo_json_version(args.zenodo_json_path)
        zenodo_v = parse_version_pep440(zenodo_version)
        if tag_version_pep440 != zenodo_v:
            print(f"❌ Version mismatch with {args.zenodo_json_path or '.zenodo.json'}!")
            failures.append(f"{args.zenodo_json_path or '.zenodo.json'}")

    # Final result
    if failures:
        print("❌ One or more version mismatches detected:")
        for f in failures:
            print(f"- {f}")
        sys.exit(1)
    else:
        print("✅ All versions match!")

if __name__ == '__main__':
    main()
