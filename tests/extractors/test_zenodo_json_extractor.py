from argparse import Namespace
from pathlib import Path

from same_version.extractors.zenodo_json_extractor import ZenodoJsonExtractor


def test_zenodo_json_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_zenodo_json_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == '.zenodo.json'

def test_zenodo_json_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_zenodo_json_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--zenodo-json-path'

def test_zenodo_json_extractor_extract_version_with_cli_args_with_valid_zenodo_json_path(cli_args_with_valid_zenodo_json_path: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=cli_args_with_valid_zenodo_json_path)
    assert extractor.extract_version() == '4.2.6'

def test_zenodo_json_extractor_target_parameter_with_cli_args_with_valid_zenodo_json_path(cli_args_with_valid_zenodo_json_path: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=cli_args_with_valid_zenodo_json_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == '.zenodo.json'

def test_zenodo_json_extractor_target_exists_with_cli_args_with_valid_zenodo_json_path(cli_args_with_valid_zenodo_json_path: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=cli_args_with_valid_zenodo_json_path)
    assert extractor.target_exists is True

def test_zenodo_json_extractor_target_cli_parameter_name_with_cli_args_with_valid_zenodo_json_path(cli_args_with_valid_zenodo_json_path: Namespace):
    extractor:ZenodoJsonExtractor = ZenodoJsonExtractor(cli_args=cli_args_with_valid_zenodo_json_path)
    assert extractor.target_cli_parameter_name == '--zenodo-json-path'