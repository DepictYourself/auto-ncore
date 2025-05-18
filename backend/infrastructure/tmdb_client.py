from infrastructure.config_service import ConfigService
import requests


class TmdbClient:
    def __init__(self, config_service: ConfigService):
        self.config = config_service.get_tmdb_config()


    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.config['jwt']}",
            "Content-Type": "application/json;charset=utf-8"
        }
    

    def search_show(self, query_string, include_adult=False, language="en-US", result_page=1):
        url = self.config["url"]
        headers = self._get_headers()
        response = requests.get(
            url+"/search/tv",
            params={
                "query":query_string,
                "include_adult": include_adult,
                "language": language,
                "page": result_page
            },
            headers=headers
        )
        return response.json()
    

    def get_show_details(self, id, language="en-US"):
        url = self.config["url"]
        response = requests.get(
            url+f"/tv/{id}",
            params={
                "language": language
            },
            headers=self._get_headers()
        )
        return response.json()
