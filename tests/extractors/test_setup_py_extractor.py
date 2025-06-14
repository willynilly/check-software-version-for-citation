from argparse import Namespace
from pathlib import Path

from same_version.extractors.setup_py_extractor import SetupPyExtractor


def test_setup_py_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_setup_py_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'setup.py'

def test_setup_py_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_setup_py_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--setup-py-path'

def test_setup_py_extractor_extract_version_with_cli_args_with_valid_setup_py_path(cli_args_with_valid_setup_py_path: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=cli_args_with_valid_setup_py_path)
    assert extractor.extract_version() == '8.3.7'

def test_setup_py_extractor_target_parameter_with_cli_args_with_valid_setup_py_path(cli_args_with_valid_setup_py_path: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=cli_args_with_valid_setup_py_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'setup.py'

def test_setup_py_extractor_target_exists_with_cli_args_with_valid_setup_py_path(cli_args_with_valid_setup_py_path: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=cli_args_with_valid_setup_py_path)
    assert extractor.target_exists is True

def test_setup_py_extractor_target_cli_parameter_name_with_cli_args_with_valid_setup_py_path(cli_args_with_valid_setup_py_path: Namespace):
    extractor:SetupPyExtractor = SetupPyExtractor(cli_args=cli_args_with_valid_setup_py_path)
    assert extractor.target_cli_parameter_name == '--setup-py-path'