from argparse import Namespace
from pathlib import Path

from same_version.extractors.cargo_toml_extractor import CargoTomlExtractor


def test_cargo_toml_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_cargo_toml_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'Cargo.toml'

def test_cargo_toml_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_cargo_toml_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--cargo-toml-path'

def test_cargo_toml_extractor_extract_version_with_cli_args_with_valid_cargo_toml_path(cli_args_with_valid_cargo_toml_path: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=cli_args_with_valid_cargo_toml_path)
    assert extractor.extract_version() == '10.0.8'

def test_cargo_toml_extractor_target_parameter_with_cli_args_with_valid_cargo_toml_path(cli_args_with_valid_cargo_toml_path: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=cli_args_with_valid_cargo_toml_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'Cargo.toml'

def test_cargo_toml_extractor_target_exists_with_cli_args_with_valid_cargo_toml_path(cli_args_with_valid_cargo_toml_path: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=cli_args_with_valid_cargo_toml_path)
    assert extractor.target_exists is True

def test_cargo_toml_extractor_target_cli_parameter_name_with_cli_args_with_valid_cargo_toml_path(cli_args_with_valid_cargo_toml_path: Namespace):
    extractor:CargoTomlExtractor = CargoTomlExtractor(cli_args=cli_args_with_valid_cargo_toml_path)
    assert extractor.target_cli_parameter_name == '--cargo-toml-path'