from argparse import Namespace
from pathlib import Path

import pytest


@pytest.fixture
def empty_cli_args():
    return Namespace()

@pytest.fixture
def cli_args_with_base_version():
    return Namespace(base_version='1.0.5')

@pytest.fixture
def cli_args_with_valid_package_json_path():
    package_json_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'package.json'
    return Namespace(package_json_path=package_json_path)