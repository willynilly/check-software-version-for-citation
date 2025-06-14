from argparse import Namespace
from pathlib import Path

from same_version.extractors.ro_crate_metadata_json_extractor import (
    RoCrateMetadataJsonExtractor,
)


def test_ro_crate_metadata_json_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_ro_crate_metadata_json_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'ro-crate-metadata.json'

def test_ro_crate_metadata_json_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_ro_crate_metadata_json_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--ro-crate-metadata-json-path'

def test_ro_crate_metadata_json_extractor_extract_version_with_cli_args_with_valid_ro_crate_metadata_json_path_and_id(cli_args_with_valid_ro_crate_metadata_json_path_and_id: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=cli_args_with_valid_ro_crate_metadata_json_path_and_id)
    assert extractor.extract_version() == '7.2.5'

def test_ro_crate_metadata_json_extractor_target_parameter_with_cli_args_with_valid_ro_crate_metadata_json_path_and_id(cli_args_with_valid_ro_crate_metadata_json_path_and_id: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=cli_args_with_valid_ro_crate_metadata_json_path_and_id)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'ro-crate-metadata.json'

def test_ro_crate_metadata_json_extractor_target_exists_with_cli_args_with_valid_ro_crate_metadata_json_path_and_id(cli_args_with_valid_ro_crate_metadata_json_path_and_id: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=cli_args_with_valid_ro_crate_metadata_json_path_and_id)
    assert extractor.target_exists is True

def test_ro_crate_metadata_json_extractor_target_cli_parameter_name_with_cli_args_with_valid_ro_crate_metadata_json_path_and_id(cli_args_with_valid_ro_crate_metadata_json_path_and_id: Namespace):
    extractor:RoCrateMetadataJsonExtractor = RoCrateMetadataJsonExtractor(cli_args=cli_args_with_valid_ro_crate_metadata_json_path_and_id)
    assert extractor.target_cli_parameter_name == '--ro-crate-metadata-json-path'