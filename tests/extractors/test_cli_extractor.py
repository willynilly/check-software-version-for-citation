from argparse import Namespace

from same_version.extractors.cli_extractor import CliExtractor


def test_cli_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_cli_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'CLI parameter'

def test_cli_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_cli_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--base-version'

def test_cli_extractor_extract_version_with_cli_args_with_base_version(cli_args_with_base_version: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=cli_args_with_base_version)
    assert extractor.extract_version() == '1.0.5'

def test_cli_extractor_target_parameter_with_cli_args_with_base_version(cli_args_with_base_version: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=cli_args_with_base_version)
    assert extractor.target_name == 'CLI parameter'

def test_cli_extractor_target_exists_with_cli_args_with_base_version(cli_args_with_base_version: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=cli_args_with_base_version)
    assert extractor.target_exists is True

def test_cli_extractor_target_cli_parameter_name_with_cli_args_with_base_version(cli_args_with_base_version: Namespace):
    extractor:CliExtractor = CliExtractor(cli_args=cli_args_with_base_version)
    assert extractor.target_cli_parameter_name == '--base-version'