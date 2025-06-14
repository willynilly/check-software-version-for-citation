from argparse import Namespace
from pathlib import Path

from same_version.extractors.py_version_assignment_extractor import (
    PyVersionAssignmentExtractor,
)


def test_py_version_assignment_extractor_extract_version_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=empty_cli_args)
    assert extractor.extract_version() is None

def test_py_version_assignment_extractor_target_parameter_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=empty_cli_args)
    assert extractor.target_name == "Python file with __version__ assignment to a literal string"

def test_py_version_assignment_extractor_target_exists_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=empty_cli_args)
    assert extractor.target_exists is False

def test_py_version_assignment_extractor_target_cli_parameter_name_with_empty_cli_args(empty_cli_args: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=empty_cli_args)
    assert extractor.target_cli_parameter_name == '--py-version-assignment-path'

def test_py_version_assignment_extractor_extract_version_with_cli_args_with_valid_py_version_assignment_path(cli_args_with_valid_py_version_assignment_path: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=cli_args_with_valid_py_version_assignment_path)
    assert extractor.extract_version() == '15.2.4'

def test_py_version_assignment_extractor_target_parameter_with_cli_args_with_valid_py_version_assignment_path(cli_args_with_valid_py_version_assignment_path: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=cli_args_with_valid_py_version_assignment_path)
    assert extractor.target_name is not None and Path(extractor.target_name).name == 'main_with_literal_version_assignment.py'

def test_py_version_assignment_extractor_target_exists_with_cli_args_with_valid_py_version_assignment_path(cli_args_with_valid_py_version_assignment_path: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=cli_args_with_valid_py_version_assignment_path)
    assert extractor.target_exists is True

def test_py_version_assignment_extractor_target_cli_parameter_name_with_cli_args_with_valid_py_version_assignment_path(cli_args_with_valid_py_version_assignment_path: Namespace):
    extractor:PyVersionAssignmentExtractor = PyVersionAssignmentExtractor(cli_args=cli_args_with_valid_py_version_assignment_path)
    assert extractor.target_cli_parameter_name == '--py-version-assignment-path'