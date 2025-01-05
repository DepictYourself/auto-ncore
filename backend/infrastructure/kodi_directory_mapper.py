from domain.download_location_mapper import DownloadLocationMapper


class KodiDirectoryMapper(DownloadLocationMapper):

    def get_directory(self, category: str, metadata: dict = None) -> str:
        
        if category == 'show' and metadata:
            show_name = metadata.get("show_name", "unknown_show")
            season_number = metadata.get("season_number", "unknown_season")
            episode_name = metadata.get("episode_name", "unknown_episode")
            return f"{base_directory}/{show_name}/season {season_number}/{episode_name}"