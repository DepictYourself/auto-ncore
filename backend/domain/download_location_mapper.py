from abc import ABC, abstractmethod


class DownloadLocationMapper(ABC):
    @abstractmethod
    def get_tvshow_directory(self, show_name, release_year, season_number, episode_name) -> str:
        pass