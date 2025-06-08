#!/usr/bin/env python3

import argparse
import os
import sys
import yaml
import tomli
import json
import re
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description="Check tag/release version vs CITATION.cff (optionally pyproject.toml, codemeta.json, .zenodo.json, package.json, setup.py)")
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

def extract_citation_version(cff_path):
    if not os.path.isfile(cff_path):
        print(f"❌ CITATION.cff file not found at: {cff_path}")
        sys.exit(1)

    with open(cff_path, 'r') as f:
        data = yaml.safe_load(f)
    
    version = data.get('version')
    if not version:
        print("❌ Could not find 'version' field in CITATION.cff")
        sys.exit(1)
    
    print(f"📖 CITATION.cff version: {version}")
    return version

def extract_pyproject_version(pyproject_path):
    if not os.path.isfile(pyproject_path):
        print(f"❌ pyproject.toml file not found at: {pyproject_path}")
        sys.exit(1)

    with open(pyproject_path, 'rb') as f:
        data = tomli.load(f)
    
    version = None
    if 'project' in data and 'version' in data['project']:
        version = data['project']['version']
    elif 'tool' in data and 'poetry' in data['tool'] and 'version' in data['tool']['poetry']:
        version = data['tool']['poetry']['version']

    if not version:
        print("❌ Could not find 'version' field in pyproject.toml (checked [project] and [tool.poetry])")
        sys.exit(1)
    
    print(f"📖 pyproject.toml version: {version}")
    return version

def extract_codemeta_version(codemeta_path):
    if not os.path.isfile(codemeta_path):
        print(f"❌ codemeta.json file not found at: {codemeta_path}")
        sys.exit(1)

    with open(codemeta_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    version = data.get('version')
    if not version:
        print("❌ Could not find 'version' field in codemeta.json")
        sys.exit(1)
    
    print(f"📖 codemeta.json version: {version}")
    return version

def extract_zenodo_version(zenodo_path):
    if not os.path.isfile(zenodo_path):
        print(f"❌ .zenodo.json file not found at: {zenodo_path}")
        sys.exit(1)

    with open(zenodo_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    version = data.get('version')
    if not version:
        print("❌ Could not find 'version' field in .zenodo.json")
        sys.exit(1)
    
    print(f"📖 .zenodo.json version: {version}")
    return version

def extract_package_version(package_path):
    if not os.path.isfile(package_path):
        print(f"❌ package.json file not found at: {package_path}")
        sys.exit(1)

    with open(package_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    version = data.get('version')
    if not version:
        print("❌ Could not find 'version' field in package.json")
        sys.exit(1)
    
    print(f"📖 package.json version: {version}")
    return version

def extract_setup_py_version(setup_path):
    if not os.path.isfile(setup_path):
        print(f"❌ setup.py file not found at: {setup_path}")
        sys.exit(1)

    print(f"🔍 Running 'python {setup_path} --version'...")
    try:
        result = subprocess.run(
            ['python', setup_path, '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        version = result.stdout.strip()
        if not version:
            print(f"❌ setup.py did not produce a version")
            sys.exit(1)
        print(f"📖 setup.py version: {version}")
        return version
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to run 'python {setup_path} --version'")
        print(f"STDOUT:\n{e.stdout}")
        print(f"STDERR:\n{e.stderr}")
        sys.exit(1)

def normalize_version(version):
    return version.lstrip('v')

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

def main():
    args = parse_args()

    tag_version = normalize_version(extract_tag_version(args.event_name, args.ref, args.release_tag))
    failures = []

    # Always check CITATION.cff
    citation_version = normalize_version(extract_citation_version(args.cff_path))
    print(f"🔍 Comparing tag/release version '{tag_version}' with CITATION.cff version '{citation_version}'")
    if tag_version != citation_version:
        print("❌ Version mismatch with CITATION.cff!")
        failures.append("CITATION.cff")

    # Optionally check pyproject.toml
    if args.check_pyproject_toml.lower() == 'true':
        pyproject_version = normalize_version(extract_pyproject_version(args.pyproject_toml_path))
        print(f"🔍 Comparing tag/release version '{tag_version}' with pyproject.toml version '{pyproject_version}'")
        if tag_version != pyproject_version:
            print("❌ Version mismatch with pyproject.toml!")
            failures.append("pyproject.toml")

    # Optionally check codemeta.json
    if args.check_codemeta_json.lower() == 'true':
        codemeta_version = normalize_version(extract_codemeta_version(args.codemeta_json_path))
        print(f"🔍 Comparing tag/release version '{tag_version}' with codemeta.json version '{codemeta_version}'")
        if tag_version != codemeta_version:
            print("❌ Version mismatch with codemeta.json!")
            failures.append("codemeta.json")

    # Optionally check .zenodo.json
    if args.check_zenodo_json.lower() == 'true':
        zenodo_version = normalize_version(extract_zenodo_version(args.zenodo_json_path))
        print(f"🔍 Comparing tag/release version '{tag_version}' with .zenodo.json version '{zenodo_version}'")
        if tag_version != zenodo_version:
            print("❌ Version mismatch with .zenodo.json!")
            failures.append(".zenodo.json")

    # Optionally check package.json
    if args.check_package_json.lower() == 'true':
        package_version = normalize_version(extract_package_version(args.package_json_path))
        print(f"🔍 Comparing tag/release version '{tag_version}' with package.json version '{package_version}'")
        if tag_version != package_version:
            print("❌ Version mismatch with package.json!")
            failures.append("package.json")

    # Optionally check setup.py
    if args.check_setup_py.lower() == 'true':
        setup_py_version = normalize_version(extract_setup_py_version(args.setup_py_path))
        print(f"🔍 Comparing tag/release version '{tag_version}' with setup.py version '{setup_py_version}'")
        if tag_version != setup_py_version:
            print("❌ Version mismatch with setup.py!")
            failures.append("setup.py")

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
