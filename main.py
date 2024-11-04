import sys

from concurrent.futures.thread import ThreadPoolExecutor
from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication, QMainWindow

import files_getter
import first_start
import main_window


# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup pyside6-uic生成的窗口
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.refresh = self.ui.refresh
        t = ThreadPoolExecutor(max_workers=1)
        self.refresh.clicked.connect(lambda :t.submit(self.refresh_version_list))

        self.version_list = self.ui.version_list


    def refresh_version_list(self):
        fg = files_getter.GetDownloadVersion()
        v_list = fg.get_version()

        self.version_list.clear()

        self.version_list.addItems(v_list)


# 主函数
def main():
    app = QApplication(sys.argv)

    # 加载中文语言包
    translator = QTranslator()
    translator.load("qt_zh_CN", QLibraryInfo.path(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    fs = first_start.FirstStartLauncher()
    fs.first_start_launcher()

    # 窗口显示
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# 主程序
if __name__ == '__main__':
    main()
