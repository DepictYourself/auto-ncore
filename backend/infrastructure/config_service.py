import os
from dotenv import load_dotenv
from typing import TypedDict

class TranmissionConfig(TypedDict):
    host: str
    port: int
    username: str
    password: str
    dir: str

class NcoreConfig(TypedDict):
    username: str | None
    password: str | None
    key: str | None


class TmdbConfig(TypedDict):
    jwt: str | None
    key: str | None
    url: str | None

class KodiConfig(TypedDict):
    movies_folder_name: str
    shows_folder_name: str


class ConfigService:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Transmission credentials
        self.transmission_host=os.getenv('TRANSMISSION_HOST', 'localhost')
        self.transmission_port=int(os.getenv('TRANSMISSION_PORT', 9091))
        self.transmission_username=os.getenv('TRANSMISSION_USER', 'admin')
        self.transmission_password=os.getenv('TRANSMISSION_PASS', 'admin')
        self.transmission_dir=os.getenv('TRANSMISSION_DIR', 'downloads')

        # NCore credentials
        self.ncore_username = os.getenv('NCORE_USER')
        self.ncore_password = os.getenv('NCORE_PASS')
        self.ncore_key = os.getenv('NCORE_KEY')

        self.tmdb_jwt = os.getenv('TMDB_JWT')
        self.tmdb_key = os.getenv('TMDB_KEY')
        self.tmdb_url = os.getenv('TMDB_URL')

        self.kodi_folder_movies = os.getenv('KODI_FOLDER_MOVIES', 'movies')
        self.kodi_folder_shows = os.getenv('KODI_FOLDER_SHOWS', 'shows')


    def get_tranmission_config(self) -> TranmissionConfig:
        config: TranmissionConfig = {
            "host": self.transmission_host,
            "port": self.transmission_port,
            "username": self.transmission_username,
            "password": self.transmission_password,
            "dir": self.transmission_dir
        }
        return config

    def get_ncore_config(self) -> NcoreConfig:
        config: NcoreConfig = {
            "username": self.ncore_username,
            "password": self.ncore_password,
            "key": self.ncore_key
        }
        print("ncore config: ", config)
        return config
    
    def get_tmdb_config(self) -> TmdbConfig:
        config: TmdbConfig = {
            "jwt": self.tmdb_jwt,
            "key": self.tmdb_key,
            "url": self.tmdb_url
        }
        return config
    
    def get_kodi_config(self) -> KodiConfig:
        config: KodiConfig = {
            "movies_folder_name": self.kodi_folder_movies,
            "shows_folder_name": self.kodi_folder_shows
        }
        return config