from argparse import Namespace

from version_consistency.checkers.checker import Checker
from version_consistency.extractors.github_event_extractor import GitHubEventExtractor


class GitHubEventChecker(Checker):
    def __init__(self, extractor: GitHubEventExtractor, cli_args: Namespace):
        super().__init__(extractor=extractor, cli_args=cli_args) 