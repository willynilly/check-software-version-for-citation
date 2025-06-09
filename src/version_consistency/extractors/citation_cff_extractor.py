import logging
import sys

import yaml

logger = logging.getLogger(__name__)


def extract_citation_cff_version(path) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    version = data.get('version')
    if not version:
        logger.error(f"❌ {path or 'CITATION.cff'} missing 'version' field!")
        sys.exit(1)
    logger.info(f"📖 {path or 'CITATION.cff'} version: {version}")
    return version