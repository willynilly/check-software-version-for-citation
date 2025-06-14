from argparse import Namespace
from pathlib import Path

import pytest


@pytest.fixture
def empty_cli_args():
    return Namespace()

@pytest.fixture
def cli_args_with_base_version():
    return Namespace(base_version='1.0.5')

@pytest.fixture
def cli_args_with_valid_package_json_path():
    package_json_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'package.json'
    return Namespace(package_json_path=package_json_path)

@pytest.fixture
def cli_args_with_valid_pom_xml_path():
    pom_xml_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'pom.xml'
    return Namespace(pom_xml_path=pom_xml_path)

@pytest.fixture
def cli_args_with_valid_pyproject_toml_path():
    pyproject_toml_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'pyproject.toml'
    return Namespace(pyproject_toml_path=pyproject_toml_path)

@pytest.fixture
def cli_args_with_valid_cargo_toml_path():
    cargo_toml_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'Cargo.toml'
    return Namespace(cargo_toml_path=cargo_toml_path)

@pytest.fixture
def cli_args_with_valid_composer_json_path():
    composer_json_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'composer.json'
    return Namespace(composer_json_path=composer_json_path)

@pytest.fixture
def cli_args_with_valid_codemeta_json_path():
    codemeta_json_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'codemeta.json'
    return Namespace(codemeta_json_path=codemeta_json_path)

@pytest.fixture
def cli_args_with_valid_ro_crate_metadata_json_path_and_id():
    ro_crate_metadata_json_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'ro-crate-metadata.json'
    ro_crate_metadata_json_id: str = 'software/'
    return Namespace(ro_crate_metadata_json_path=ro_crate_metadata_json_path, ro_crate_metadata_json_id=ro_crate_metadata_json_id)

@pytest.fixture
def cli_args_with_valid_zenodo_json_path():
    zenodo_json_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / '.zenodo.json'
    return Namespace(zenodo_json_path=zenodo_json_path)

@pytest.fixture
def cli_args_with_valid_nuspec_path():
    nuspec_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / '.nuspec'
    return Namespace(nuspec_path=nuspec_path)

@pytest.fixture
def cli_args_with_valid_r_description_path():
    r_description_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'DESCRIPTION'
    return Namespace(r_description_path=r_description_path)

@pytest.fixture
def cli_args_with_valid_setup_cfg_path():
    setup_cfg_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'setup.cfg'
    return Namespace(setup_cfg_path=setup_cfg_path)

@pytest.fixture
def cli_args_with_valid_setup_py_path():
    setup_py_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'setup.py'
    return Namespace(setup_py_path=setup_py_path)

@pytest.fixture
def cli_args_with_valid_citation_cff_path():
    citation_cff_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'CITATION.cff'
    return Namespace(citation_cff_path=citation_cff_path)

@pytest.fixture
def cli_args_with_valid_py_version_assignment_path():
    py_version_assignment_path: Path = Path(__file__).resolve().parent.parent / 'test_data' / 'main_with_literal_version_assignment.py'
    return Namespace(py_version_assignment_path=py_version_assignment_path)

    
