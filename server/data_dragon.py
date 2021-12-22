import os
import tarfile

import requests


# Code from Roman Podlinov
def download_file(url):
    local_filename = "server/static/" + url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


class DataDragon:

    def __init__(self):
        url = "https://ddragon.leagueoflegends.com/api/versions.json"
        response = requests.get(url=url)
        if response.status_code != 200:
            exit(1)
        versions = response.json()
        if len(versions) <= 0:
            exit(1)
        self.version = versions[0]
        self.url = "https://ddragon.leagueoflegends.com/cdn/dragontail-" + self.version + ".tgz"

    def force_download(self):
        download_file(self.url)
        file = tarfile.open("server/static/dragontail-" + self.version + ".tgz")
        file.extractall("server/static/dragontail-" + self.version)
        file.close()

    def download_if_needed(self):
        if "dragontail-" + self.version not in os.listdir("server/static"):
            self.force_download()