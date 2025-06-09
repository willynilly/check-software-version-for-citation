import logging
import subprocess
import sys
from argparse import Namespace

from version_consistency.extractors.file_extractor import FileExtractor

logger = logging.getLogger(__name__)

class SetupPyExtractor(FileExtractor):

    def __init__(self, cli_args: Namespace):
        super().__init__(
            target_file_path=cli_args.setup_py_path, 
            default_target_name="setup.py", 
            target_cli_parameter_name="setup_py_path"
        )

    def _get_data(self) -> dict:
        data = {}
        
        try:
            output = subprocess.check_output(['python', str(self.target_file_path), '--version'], stderr=subprocess.STDOUT)
            data['version'] = output.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Error running {self.target_name} --version:\n{e.output.decode('utf-8')}")
            sys.exit(1)

        return data
    
    def _get_version_from_data(self, data: dict) -> str | None:
        version = data.get('version')
        return version