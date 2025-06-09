import logging
import sys

import tomli

logger = logging.getLogger(__name__)

def extract_pyproject_toml_version(path) -> str:
    with open(path, 'rb') as f:
        data = tomli.load(f)
    project = data.get('project', {})
    version = project.get('version')
    if not version:
        logger.error(f"❌ {path or 'pyproject.toml'} missing [project] version!")
        sys.exit(1)
    logger.info(f"📖 {path or 'pyproject.toml'} version: {version}")
    return version