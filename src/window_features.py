from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path
from PySide6.QtWidgets import QMainWindow, QMessageBox

import files_getter
import main_window
from path_list import FolderPaths, FilePaths, URLPaths


# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup pyside6-uic 生成的窗口
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        # 版本文件夹路径
        self.version_folder: Path = FolderPaths.VERSION_FOLDER
        # 缓存文件路径
        self.tempcache: Path = FolderPaths.TEMP_CACHE
        # 版本清单路径
        self.manifest_path: Path = FilePaths.VERSION_MANIFEST
        # 版本清单网络地址
        self.manifest_url: str = URLPaths.VERSION_MANIFEST_URL

        # 实例化线程池
        self.tpe = ThreadPoolExecutor(max_workers=1)
        # 实例化 VersionGetter 类
        self.get = files_getter.VersionGetter(self.manifest_url, self.manifest_path)

        """
        BT: Button
        CB: ComboBox
        LE: LineEdit
        """
        # 刷新下载列表按钮
        self.BT_refresh_download_list = self.ui.refresh_download_list
        # 刷新选择列表按钮
        self.BT_refresh_select_list = self.ui.refresh_select_list
        # 下载版本按钮
        self.BT_download_version = self.ui.download_version
        # 下载版本列表选择框
        self.CB_download_version_list = self.ui.download_version_list
        # 版本类型选择框
        self.CB_version_type = self.ui.version_type
        # 选择版本列表选择框
        self.CB_select_version_list = self.ui.select_version_list
        # 版本名称输入框
        self.LE_version_name = self.ui.version_name

        # 刷新下载列表按钮信号
        self.BT_refresh_download_list.clicked.connect(self.refresh_download_list)
        # 刷新选择列表按钮信号
        self.BT_refresh_select_list.clicked.connect(self.refresh_select_list)
        # 下载版本按钮信号
        self.BT_download_version.clicked.connect(self.download_select_version)
        # 版本列表改动信号
        self.CB_download_version_list.currentTextChanged.connect(lambda :self.LE_version_name.setText(self.CB_download_version_list.currentText()))


    def refresh_download_list(self):
        v_type = self.CB_version_type.currentText().lower()

        def get_list():
            if not self.tempcache.exists():
                self.tempcache.mkdir()

            v_list = self.get.get_version(v_type)

            self.CB_download_version_list.addItems(v_list)

            self.BT_refresh_download_list.setEnabled(True)

        self.BT_refresh_download_list.setEnabled(False)
        self.CB_download_version_list.clear()
        self.tpe.submit(get_list)


    def refresh_select_list(self):
        def get_list():
            v_list = [f.name for f in self.version_folder.iterdir() if f.is_dir()]

            self.CB_select_version_list.addItems(v_list)

            self.BT_refresh_select_list.setEnabled(True)

        self.BT_refresh_select_list.setEnabled(False)
        self.CB_select_version_list.clear()
        self.tpe.submit(get_list)


    def download_select_version(self):
        if self.LE_version_name.text() == '' or self.CB_download_version_list.currentText() == '':
            QMessageBox.warning(self, '警告', '版本或版本名称不能为空', QMessageBox.Ok, QMessageBox.Ok)
            return

        version_path_name = Path(self.version_folder, self.LE_version_name.text())
        version_json = Path(version_path_name, self.LE_version_name.text() + '.json')

        if not self.version_folder.exists():
            self.version_folder.mkdir()
        if not version_path_name.exists():
            version_path_name.mkdir()

        self.get.download_version_json(self.CB_download_version_list.currentText(), version_json)
