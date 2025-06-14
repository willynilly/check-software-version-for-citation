from argparse import Namespace
from pathlib import Path

from same_version.extractors.r_description_extractor import RDescriptionExtractor


def test_r_description_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_r_description_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'DESCRIPTION'

def test_r_description_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_r_description_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--r-description-path'

def test_r_description_extractor_extract_version_with_cli_args_with_valid_r_description_path(cli_args_with_valid_r_description_path: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=cli_args_with_valid_r_description_path)
    assert extractor.extract_version() == '3.1.4'

def test_r_description_extractor_target_parameter_with_cli_args_with_valid_r_description_path(cli_args_with_valid_r_description_path: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=cli_args_with_valid_r_description_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'DESCRIPTION'

def test_r_description_extractor_target_exists_with_cli_args_with_valid_r_description_path(cli_args_with_valid_r_description_path: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=cli_args_with_valid_r_description_path)
    assert extractor.target_exists is True

def test_r_description_extractor_target_cli_parameter_name_with_cli_args_with_valid_r_description_path(cli_args_with_valid_r_description_path: Namespace):
    extractor:RDescriptionExtractor = RDescriptionExtractor(cli_args=cli_args_with_valid_r_description_path)
    assert extractor.target_cli_parameter_name == '--r-description-path'