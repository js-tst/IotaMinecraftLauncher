from pathlib import Path

"""
----------FolderPaths----------
PathName          Type   Path
"""
MC_FOLDER:        Path = Path('.minecraft')
IML_FOLDER:       Path = Path('.IML')
TEMP_CACHE:       Path = Path(IML_FOLDER, 'cache')
FIRST_START_FLAG: Path = Path(IML_FOLDER, 'FSF')
VERSION_FOLDER:   Path = Path(MC_FOLDER, 'versions')

"""
----------FilePaths------------
PathName          Type   Path
"""
VERSION_MANIFEST: Path = Path(TEMP_CACHE, 'version_manifest.json')
