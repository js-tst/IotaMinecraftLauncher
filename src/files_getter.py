import json
import pathlib
import urllib.request

import path_list


class GetDownloadVersion:
    def __init__(self):
        self.url = 'https://piston-meta.mojang.com/mc/game/version_manifest.json'
        self.tempcache: pathlib.Path = pathlib.Path(path_list.TMP_CACHE)
        self.filepath: pathlib.Path = pathlib.Path(self.tempcache, 'version_manifest.json')


    def get_version(self) -> list[str]:
        """
        下载 version_manifest.json 并获取版本列表的方法

        返回一个版本列表，类型为 list[str]
        """
        if not self.tempcache.exists():
            self.tempcache.mkdir()

        urllib.request.urlretrieve(url=self.url, filename=self.filepath)

        with open(self.filepath) as version_file:
            version_load: dict = json.loads(version_file.read())
        version_list: list[str]= []

        for i in version_load["versions"]:
            if i["type"] == "release":
                version_list.append(i["id"])

        return version_list
