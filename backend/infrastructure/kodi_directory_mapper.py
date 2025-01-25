from domain.download_location_mapper import DownloadLocationMapper
from domain.torrent_category import TorrentCategory


class KodiDirectoryMapper(DownloadLocationMapper):

    def map_category(type: str) -> TorrentCategory:
        type_mappings = {
            "xvid_hun": TorrentCategory.MOVIE,
            "xvid": TorrentCategory.MOVIE,
            # "dvd_hun"
            # "dvd"
            # "dvd9_hun"
            # "dvd9"
            # "hd_hun"
            "hd": TorrentCategory.MOVIE,
            "xvidser_hun": TorrentCategory.SHOW,
            "xvidser": TorrentCategory.SHOW,
            # "dvdser_hun"
            # "dvdser"
            "hdser_hun": TorrentCategory.SHOW,
            "hdser": TorrentCategory.SHOW,
            "mp3_hun": TorrentCategory.MUSIC,
            "mp3": TorrentCategory.MUSIC,
            "lossless_hun": TorrentCategory.MUSIC,
            "lossless": TorrentCategory.MUSIC,
            "clip": TorrentCategory.MUSIC,
            "game_iso": TorrentCategory.GAME,
            "game_rip": TorrentCategory.GAME,
            "console": TorrentCategory.GAME,
            "ebook_hun": TorrentCategory.EBOOK,
            "ebook": TorrentCategory.EBOOK,
            "iso": TorrentCategory.SOFTWARE,
            "misc": TorrentCategory.SOFTWARE,
            "mobil": TorrentCategory.SOFTWARE,
            # "xxx_imageset"
            # "xxx_xvid"
            # "xxx_dvd"
            # "xxx_hd"
            # "all_own"
        }
        return type_mappings[type]

    def get_tvshow_directory(self, show_name, release_year, season_number, episode_name) -> str:
        # if category == 'show' and metadata:
        #     show_name = metadata.get("show_name", "unknown_show")
        #     season_number = metadata.get("season_number", "unknown_season")
        #     episode_name = metadata.get("episode_name", "unknown_episode")
        #     return f"{base_directory}/{show_name}/season {season_number}/{episode_name}"
        return ""