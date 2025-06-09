import json
import logging
import sys

logger = logging.getLogger(__name__)


def extract_codemeta_json_version(path) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    version = data.get('version')
    if not version:
        logger.error(f"❌ {path or 'codemeta.json'} missing 'version' field!")
        sys.exit(1)
    logger.info(f"📖 {path or 'codemeta.json'} version: {version}")
    return version