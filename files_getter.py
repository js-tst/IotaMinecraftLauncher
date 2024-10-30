import urllib.request


class GetDownloadVersion:
    def __init__(self):
        self.url = 'https://piston-meta.mojang.com/mc/game/version_manifest.json'
        self.filename= 'version_manifest.json'

    def get_version(self):
        version_manifest = urllib.request.urlretrieve(url=self.url, filename=self.filename)
