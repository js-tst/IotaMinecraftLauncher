from concurrent.futures.thread import ThreadPoolExecutor
from PySide6.QtWidgets import QMainWindow

import files_getter
import main_window


# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup pyside6-uic生成的窗口
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        # 刷新按钮
        self.refresh = self.ui.refresh
        # 下载版本按钮
        self.download_version = self.ui.download_version
        # 版本列表选择框
        self.version_list = self.ui.version_list

        self.tpe = ThreadPoolExecutor(max_workers=1)

        self.refresh.clicked.connect(self.refresh_version_list)

        self.download_version.clicked.connect(self.download_select_version)


    def refresh_version_list(self):
        def get_list():
            fg = files_getter.GetDownloadVersion()
            v_list = fg.get_version()

            self.version_list.addItems(v_list)

            self.refresh.setEnabled(True)

        self.refresh.setEnabled(False)
        self.version_list.clear()
        self.tpe.submit(get_list)


    def download_select_version(self):
        print(self.version_list.currentText())
