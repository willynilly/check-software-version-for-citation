from argparse import Namespace
from pathlib import Path

from same_version.extractors.composer_json_extractor import ComposerJsonExtractor


def test_composer_json_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_composer_json_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'composer.json'

def test_composer_json_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_composer_json_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--composer-json-path'

def test_composer_json_extractor_extract_version_with_cli_args_with_valid_composer_json_path(cli_args_with_valid_composer_json_path: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=cli_args_with_valid_composer_json_path)
    assert extractor.extract_version() == '6.0.8'

def test_composer_json_extractor_target_parameter_with_cli_args_with_valid_composer_json_path(cli_args_with_valid_composer_json_path: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=cli_args_with_valid_composer_json_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'composer.json'

def test_composer_json_extractor_target_exists_with_cli_args_with_valid_composer_json_path(cli_args_with_valid_composer_json_path: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=cli_args_with_valid_composer_json_path)
    assert extractor.target_exists is True

def test_composer_json_extractor_target_cli_parameter_name_with_cli_args_with_valid_composer_json_path(cli_args_with_valid_composer_json_path: Namespace):
    extractor:ComposerJsonExtractor = ComposerJsonExtractor(cli_args=cli_args_with_valid_composer_json_path)
    assert extractor.target_cli_parameter_name == '--composer-json-path'