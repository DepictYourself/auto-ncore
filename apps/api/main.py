import time
from fastapi import FastApi
from transmission_rpc import Client

# host = "192.168.0.1"
# port = 9091
# username = ""
# password = ""

# test_torrent_url = ""

# print('started')
# transmission_client = Client(host=host, port=port, username=username, password = password)
# torrents = transmission_client.get_torrents()
# for i in torrents:
#     print(i)


app = FastApi()


print('ending..')
