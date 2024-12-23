import shutil
import sys
from PySide6.QtWidgets import QMessageBox

import window_features
from path_list import FolderPaths, FilePaths

"""
这个类是用来首次启动处理文件夹冲突的
写的依托构式，姑且先这么用着吧（
"""
class FirstStartLauncher:
    def __init__(self):
        # .minecraft文件夹路径
        self.mc_folder = FolderPaths.MC_FOLDER
        # .IML文件夹路径
        self.iml_folder = FolderPaths.IML_FOLDER
        # 首次启动标志文件
        self.fsf = FilePaths.FIRST_START_FLAG

    def first_start_launcher(self):
        # 判断首次启动的标志文件是否存在
        if self.fsf.exists():
            return
        # 检查文件夹是否存在
        if self.iml_folder.exists() or self.mc_folder.exists():
            # noinspection PyTypeChecker
            warn_msgbox = QMessageBox.warning(window_features.MainWindow(), '注意',
                                '文件夹内存在可能的冲突，是否继续初始化（冲突的文件夹将会被删除）\n'
                                '点击 是 自动处理冲突\n点击 忽略 忽略此警告（可能会引发错误）\n点击 否 退出程序',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore, QMessageBox.No)

            # 一堆构式逻辑，将就用吧
            if warn_msgbox == QMessageBox.Yes and self.iml_folder.exists():
                self._handle_folder_conflict(self.iml_folder)
            elif warn_msgbox == QMessageBox.Yes and not self.iml_folder.exists():
                self.iml_folder.mkdir()
            if warn_msgbox == QMessageBox.Yes and self.mc_folder.exists():
                self._handle_folder_conflict(self.mc_folder)
            elif warn_msgbox == QMessageBox.Yes and not self.mc_folder.exists():
                self.mc_folder.mkdir()

            if warn_msgbox == QMessageBox.Ignore:
                pass
            if warn_msgbox == QMessageBox.No:
                sys.exit(0)
        else:
            self.mc_folder.mkdir()
            self.iml_folder.mkdir()

        self.fsf.touch()


    @staticmethod
    def _handle_folder_conflict(path):
        # 文件夹冲突排查
        if not path.is_dir():
            path.unlink()
            path.mkdir()

        elif any(path.iterdir()):
            shutil.rmtree(path)
            path.mkdir()
