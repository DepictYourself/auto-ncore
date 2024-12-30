import os
from dotenv import load_dotenv
from typing import TypedDict

class TranmissionConfig(TypedDict):
    host: str
    port: int
    username: str
    password: str

class NcoreConfig(TypedDict):
    username: str
    password: str
    key: str


class ConfigService:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Transmission credentials
        self.transmission_host=os.getenv('TRANSMISSION_HOST', 'localhost'),
        self.transmission_port=int(os.getenv('TRANSMISSION_PORT', 9091)),
        self.transmission_username=os.getenv('TRANSMISSION_USER'),
        self.transmission_password=os.getenv('TRANSMISSION_PASS')

        # NCore credentials
        self.ncore_username = os.getenv('NCORE_USER')
        self.ncore_password = os.getenv('NCORE_PASS')
        self.ncore_key = os.getenv('NCORE_KEY')


    def get_tranmission_config(self) -> TranmissionConfig:
        return {
            "host": self.transmission_host,
            "port": self.transmission_port,
            "username": self.transmission_username,
            "password": self.transmission_password
        }

    def get_ncore_config(self) -> NcoreConfig:
        return {
            "username": self.ncore_username,
            "password": self.ncore_password,
            "key": self.ncore_key
        }
    
    

