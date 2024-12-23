import json
import urllib.request
from pathlib import Path


class VersionGetter:
    def __init__(self, manifest_url: str, manifest_path: Path):
        self.manifest_url: str = manifest_url
        self.manifest_path: Path = manifest_path


    def get_version(self, v_type: str) -> list[str]:
        """
        下载 version_manifest.json 并获取版本列表的方法

        参数 v_type 接受一个类型为 str 的值，代表需要获取的版本类型

        返回一个版本列表，类型为 list[str]
        """
        urllib.request.urlretrieve(url=self.manifest_url, filename=self.manifest_path)

        with open(self.manifest_path) as version_file:
            version_load: dict = json.loads(version_file.read())

        version_list: list[str]= []

        for i in version_load["versions"]:
            if i["type"] == v_type:
                version_list.append(i["id"])

        return version_list


    def download_version_json(self, version_id: str, version_json: Path) -> None:
        """
        下载 版本 json 文件的方法

        参数 version_id 接受一个类型为 str 的值，代表需要下载的版本 id
        参数 version_json 接受一个类型为 Path 的值，代表下载的文件路径

        返回无
        """
        with open(self.manifest_path) as version_file:
            version_load: dict = json.loads(version_file.read())

        version_url = next((i["url"] for i in version_load["versions"] if i["id"] == version_id), None)

        urllib.request.urlretrieve(url=version_url, filename=version_json)

        return None
