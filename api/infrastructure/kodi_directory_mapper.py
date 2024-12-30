from api.domain.download_location_mapper import DownloadLocationMapper


class KodiDirectoryMapper(DownloadLocationMapper):
    def __init__(self):
        self.category_to_directory = {
            "movie": "/downloads/movies",
            "show": "/downloads/sorozatok"
        }

    def get_directory(self, category: str, metadata: dict = None) -> str |None:
        base_directory = self.category_to_directory(category)
        if not base_directory:
            return None
        
        if category == 'show' and metadata:
            show_name = metadata.get("show_name", "unknown_show")
            season_number = metadata.get("season_number", "unknown_season")
            episode_name = metadata.get("episode_name", "unknown_episode")
            return f"{base_directory}/{show_name}/season {season_number}/{episode_name}"
        
        return base_directory