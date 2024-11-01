import json
import pathlib
import urllib.request
from typing import TextIO, List

import path_list


class GetDownloadVersion:
    def __init__(self):
        self.url = 'https://piston-meta.mojang.com/mc/game/version_manifest.json'
        self.tempcache = pathlib.Path(path_list.TMP_CACHE)
        self.filepath= pathlib.Path(self.tempcache, 'version_manifest.json')

    def get_version(self) -> List[str]:
        if not self.tempcache.exists():
            self.tempcache.mkdir()

        urllib.request.urlretrieve(url=self.url, filename=self.filepath)

        version_file: TextIO = open(self.filepath)
        version_load = json.loads(version_file.read())
        version_list = []

        for i in version_load["versions"]:
            if i["type"] == "release":
                version_list.append(i["id"])

        return version_list
