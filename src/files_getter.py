import json
import urllib.request
from pathlib import Path
from types import NoneType

import path_list


class GetDownloadVersion:
    def __init__(self):
        self.url: str = 'https://piston-meta.mojang.com/mc/game/version_manifest.json'


    def get_version(self, v_type: str, manifest_path: Path) -> list[str]:
        """
        下载 version_manifest.json 并获取版本列表的方法

        参数 v_type 接受一个类型为 str 的值，代表需要获取的版本类型

        返回一个版本列表，类型为 list[str]
        """
        urllib.request.urlretrieve(url=self.url, filename=manifest_path)

        with open(manifest_path) as version_file:
            version_load: dict = json.loads(version_file.read())

        version_list: list[str]= []

        for i in version_load["versions"]:
            if i["type"] == v_type:
                version_list.append(i["id"])

        return version_list


    @staticmethod
    def download_version_json(manifest_path: Path, version_id: str, version_path: Path, version_name: str) -> None:
        # if version_id or version_name == '':
        #     print("test")
        #     return

        version_path_name = Path(version_path, version_name)
        version_json = Path(version_path_name, version_name + '.json')
        if not version_path_name.exists():
            version_path_name.mkdir()

        with open(manifest_path) as version_file:
            version_load: dict = json.loads(version_file.read())

        version_url = next((i["url"] for i in version_load["versions"] if i["id"] == version_id), None)

        urllib.request.urlretrieve(url=version_url, filename=version_json)
