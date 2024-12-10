from pathlib import Path


class FolderPaths:
    """
    ----------FolderPaths----------
    PathName          Type   Path
    """
    MC_FOLDER:        Path = Path('.minecraft')
    IML_FOLDER:       Path = Path('.IML')
    TEMP_CACHE:       Path = Path(IML_FOLDER, 'cache')
    VERSION_FOLDER:   Path = Path(MC_FOLDER, 'versions')

class FilePaths:
    """
    ----------FilePaths------------
    PathName          Type   Path
    """
    FIRST_START_FLAG: Path = Path(FolderPaths.IML_FOLDER, 'FSF')
    VERSION_MANIFEST: Path = Path(FolderPaths.TEMP_CACHE, 'version_manifest.json')

class URLPaths:
    """
    --------------URLPaths-------------
    PathName              Type   Path
    """
    VERSION_MANIFEST_URL: str = r'https://piston-meta.mojang.com/mc/game/version_manifest.json'
