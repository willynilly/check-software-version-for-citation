import json

from version_consistency.extractors.file_extractor import FileExtractor


class JsonExtractor(FileExtractor):

    def _get_data(self) -> dict:
        data = {}
        with open(self.target_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data