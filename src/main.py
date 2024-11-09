import sys
from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtWidgets import QApplication

import first_start
import window_features


# 主函数
def main():
    app = QApplication(sys.argv)

    # 加载中文语言包
    translator = QTranslator()
    translator.load("qt_zh_CN", QLibraryInfo.path(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    # 首次启动
    fs = first_start.FirstStartLauncher()
    fs.first_start_launcher()

    # 窗口显示
    window = window_features.MainWindow()
    window.show()
    sys.exit(app.exec())


# 主程序
if __name__ == '__main__':
    main()
