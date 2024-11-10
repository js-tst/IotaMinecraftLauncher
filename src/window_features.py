from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path
from PySide6.QtWidgets import QMainWindow

import files_getter
import main_window
import path_list


# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup pyside6-uic 生成的窗口
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        # 版本文件夹路径
        self.version_folder: Path = path_list.VERSION_FOLDER
        # 缓存文件路径
        self.tempcache: Path = path_list.TEMP_CACHE
        # 版本清单路径
        self.manifest_path: Path = path_list.VERSION_MANIFEST

        # 实例化线程池
        self.tpe = ThreadPoolExecutor(max_workers=1)
        # 实例化 GetDownloadVersion 类
        self.get = files_getter.GetDownloadVersion()

        # 刷新按钮
        self.refresh = self.ui.refresh
        # 下载版本按钮
        self.download_version = self.ui.download_version
        # 版本列表选择框
        self.version_list = self.ui.version_list
        # 版本类型选择框
        self.version_type = self.ui.version_type
        # 版本名称输入框
        self.version_name = self.ui.version_name
        # 信号
        self.refresh.clicked.connect(self.refresh_version_list)

        self.download_version.clicked.connect(self.download_select_version)

        self.version_list.currentTextChanged.connect(lambda :self.version_name.setText(self.version_list.currentText()))


    def refresh_version_list(self):
        v_type = self.version_type.currentText().lower()

        def get_list():
            if not self.tempcache.exists():
                self.tempcache.mkdir()

            v_list = self.get.get_version(v_type, self.manifest_path)

            self.version_list.addItems(v_list)

            self.refresh.setEnabled(True)

        self.refresh.setEnabled(False)
        self.version_list.clear()
        self.tpe.submit(get_list)


    def download_select_version(self):
        if not self.version_folder.exists():
            self.version_folder.mkdir()

        self.get.download_version_json(self.manifest_path, self.version_list.currentText(), self.version_folder, self.version_name.text())
