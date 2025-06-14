from argparse import Namespace
from pathlib import Path

from same_version.extractors.pom_xml_extractor import PomXmlExtractor


def test_pom_xml_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_pom_xml_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'pom.xml'

def test_pom_xml_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_pom_xml_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--pom-xml-path'

def test_pom_xml_extractor_extract_version_with_cli_args_with_valid_pom_xml_path(cli_args_with_valid_pom_xml_path: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=cli_args_with_valid_pom_xml_path)
    assert extractor.extract_version() == '1.2.3'

def test_pom_xml_extractor_target_parameter_with_cli_args_with_valid_pom_xml_path(cli_args_with_valid_pom_xml_path: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=cli_args_with_valid_pom_xml_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'pom.xml'

def test_pom_xml_extractor_target_exists_with_cli_args_with_valid_pom_xml_path(cli_args_with_valid_pom_xml_path: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=cli_args_with_valid_pom_xml_path)
    assert extractor.target_exists is True

def test_pom_xml_extractor_target_cli_parameter_name_with_cli_args_with_valid_pom_xml_path(cli_args_with_valid_pom_xml_path: Namespace):
    extractor:PomXmlExtractor = PomXmlExtractor(cli_args=cli_args_with_valid_pom_xml_path)
    assert extractor.target_cli_parameter_name == '--pom-xml-path'