from argparse import Namespace
from pathlib import Path

from same_version.extractors.nuspec_extractor import NuspecExtractor


def test_nuspec_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_nuspec_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == '.nuspec'

def test_nuspec_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_nuspec_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--nuspec-path'

def test_nuspec_extractor_extract_version_with_cli_args_with_valid_nuspec_path(cli_args_with_valid_nuspec_path: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=cli_args_with_valid_nuspec_path)
    assert extractor.extract_version() == '4.8.12'

def test_nuspec_extractor_target_parameter_with_cli_args_with_valid_nuspec_path(cli_args_with_valid_nuspec_path: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=cli_args_with_valid_nuspec_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == '.nuspec'

def test_nuspec_extractor_target_exists_with_cli_args_with_valid_nuspec_path(cli_args_with_valid_nuspec_path: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=cli_args_with_valid_nuspec_path)
    assert extractor.target_exists is True

def test_nuspec_extractor_target_cli_parameter_name_with_cli_args_with_valid_nuspec_path(cli_args_with_valid_nuspec_path: Namespace):
    extractor:NuspecExtractor = NuspecExtractor(cli_args=cli_args_with_valid_nuspec_path)
    assert extractor.target_cli_parameter_name == '--nuspec-path'