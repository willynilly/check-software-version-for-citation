from argparse import Namespace
from pathlib import Path

from same_version.extractors.citation_cff_extractor import CitationCffExtractor


def test_citation_cff_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_citation_cff_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == 'CITATION.cff'

def test_citation_cff_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_citation_cff_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--citation-cff-path'

def test_citation_cff_extractor_extract_version_with_cli_args_with_valid_citation_cff_path(cli_args_with_valid_citation_cff_path: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=cli_args_with_valid_citation_cff_path)
    assert extractor.extract_version() == '0.0.8000'

def test_citation_cff_extractor_target_parameter_with_cli_args_with_valid_citation_cff_path(cli_args_with_valid_citation_cff_path: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=cli_args_with_valid_citation_cff_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'CITATION.cff'

def test_citation_cff_extractor_target_exists_with_cli_args_with_valid_citation_cff_path(cli_args_with_valid_citation_cff_path: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=cli_args_with_valid_citation_cff_path)
    assert extractor.target_exists is True

def test_citation_cff_extractor_target_cli_parameter_name_with_cli_args_with_valid_citation_cff_path(cli_args_with_valid_citation_cff_path: Namespace):
    extractor:CitationCffExtractor = CitationCffExtractor(cli_args=cli_args_with_valid_citation_cff_path)
    assert extractor.target_cli_parameter_name == '--citation-cff-path'