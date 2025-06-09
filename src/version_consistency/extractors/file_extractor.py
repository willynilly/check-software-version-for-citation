from pathlib import Path

from version_consistency.extractors.extractor import Extractor


class FileExtractor(Extractor):
    def __init__(self, target_file_path: Path, default_target_name: str, target_cli_parameter_name: str):
        self._target_file_path = target_file_path
        self._default_target_name = default_target_name
        self._target_cli_parameter_name = target_cli_parameter_name

    @property
    def target_file_path(self) -> Path:
        return self._target_file_path

    @property
    def target_exists(self) -> bool:
        return self._target_file_path.exists()
    
    @property
    def target_name(self) -> str | None:
        if self.target_exists:
            return str(self._target_file_path)
        else:
            return self._default_target_name
    
    @property    
    def target_cli_parameter_name(self) -> str | None:
        return self._target_cli_parameter_name