from abc import ABC, abstractmethod


class DownloadLocationMapper(ABC):
    @abstractmethod
    def get_directory(self, category: str) -> str | None:
        """
        Get the directory for a given torrent based on it's category.

        :param category: The category of the torrent.
        :return: The corresponding directory path or None if no mapping exists.
        """
        pass