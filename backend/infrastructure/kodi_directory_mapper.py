from domain.download_location_mapper import DownloadLocationMapper
from domain.torrent_category import TorrentCategory
from infrastructure.config_service import ConfigService


class KodiDirectoryMapper(DownloadLocationMapper):

    def __init__(self, config_service: ConfigService):
        self.config = config_service.get_kodi_config()

    def map_category(self, type: str) -> TorrentCategory:
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


    def get_tvshow_directory(self, show_name, release_year, season_number) -> str:
        return f"{show_name}.{release_year}/season {season_number}/"
    