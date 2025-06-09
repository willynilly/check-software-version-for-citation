import logging
import subprocess
import sys

logger = logging.getLogger(__name__)

def extract_setup_py_version(path) -> str:
    try:
        output = subprocess.check_output(['python', path, '--version'], stderr=subprocess.STDOUT)
        version = output.decode('utf-8').strip()
        logger.info(f"📖 {path or 'setup.py'} version: {version}")
        return version
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Error running {path or 'setup.py'} --version:\n{e.output.decode('utf-8')}")
        sys.exit(1)