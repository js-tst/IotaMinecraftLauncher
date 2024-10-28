import sys

from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication, QMainWindow

import first_start
import main_window


# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup pyside6-uic生成的窗口
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)


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
