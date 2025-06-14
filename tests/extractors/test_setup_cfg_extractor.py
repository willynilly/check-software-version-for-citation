from argparse import Namespace
from pathlib import Path

from same_version.extractors.setup_cfg_extractor import SetupCfgExtractor


def test_setup_cfg_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_setup_cfg_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'setup.cfg'

def test_setup_cfg_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_setup_cfg_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--setup-cfg-path'

def test_setup_cfg_extractor_extract_version_with_cli_args_with_valid_setup_cfg_path(cli_args_with_valid_setup_cfg_path: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=cli_args_with_valid_setup_cfg_path)
    assert extractor.extract_version() == '9.0.3'

def test_setup_cfg_extractor_target_parameter_with_cli_args_with_valid_setup_cfg_path(cli_args_with_valid_setup_cfg_path: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=cli_args_with_valid_setup_cfg_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'setup.cfg'

def test_setup_cfg_extractor_target_exists_with_cli_args_with_valid_setup_cfg_path(cli_args_with_valid_setup_cfg_path: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=cli_args_with_valid_setup_cfg_path)
    assert extractor.target_exists is True

def test_setup_cfg_extractor_target_cli_parameter_name_with_cli_args_with_valid_setup_cfg_path(cli_args_with_valid_setup_cfg_path: Namespace):
    extractor:SetupCfgExtractor = SetupCfgExtractor(cli_args=cli_args_with_valid_setup_cfg_path)
    assert extractor.target_cli_parameter_name == '--setup-cfg-path'