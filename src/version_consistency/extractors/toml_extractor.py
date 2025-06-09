
import tomli

from version_consistency.extractors.file_extractor import FileExtractor


class TomlExtractor(FileExtractor):

    def _get_data(self) -> dict:
        data = {}
        with open(self.target_file_path, 'rb') as f:
            data = tomli.load(f)
        return data