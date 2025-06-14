from argparse import Namespace
from pathlib import Path

from same_version.extractors.pyproject_toml_extractor import PyprojectTomlExtractor


def test_pyproject_toml_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_pyproject_toml_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'pyproject.toml'

def test_pyproject_toml_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_pyproject_toml_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--pyproject-toml-path'

def test_pyproject_toml_extractor_extract_version_with_cli_args_with_valid_pyproject_toml_path(cli_args_with_valid_pyproject_toml_path: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=cli_args_with_valid_pyproject_toml_path)
    assert extractor.extract_version() == '8.7.6'

def test_pyproject_toml_extractor_target_parameter_with_cli_args_with_valid_pyproject_toml_path(cli_args_with_valid_pyproject_toml_path: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=cli_args_with_valid_pyproject_toml_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'pyproject.toml'

def test_pyproject_toml_extractor_target_exists_with_cli_args_with_valid_pyproject_toml_path(cli_args_with_valid_pyproject_toml_path: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=cli_args_with_valid_pyproject_toml_path)
    assert extractor.target_exists is True

def test_pyproject_toml_extractor_target_cli_parameter_name_with_cli_args_with_valid_pyproject_toml_path(cli_args_with_valid_pyproject_toml_path: Namespace):
    extractor:PyprojectTomlExtractor = PyprojectTomlExtractor(cli_args=cli_args_with_valid_pyproject_toml_path)
    assert extractor.target_cli_parameter_name == '--pyproject-toml-path'