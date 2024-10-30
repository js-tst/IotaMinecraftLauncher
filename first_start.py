import pathlib
import shutil
import sys

from PySide6.QtWidgets import QMessageBox

import path_list


class FirstStartLauncher:
    def __init__(self):
        # .minecraft文件夹路径
        self.mc_folder = pathlib.Path(path_list.MC_FOLDER)
        # .IML文件夹路径
        self.iml_folder = pathlib.Path(path_list.IML_FOLDER)

    def first_start_launcher(self):
        # 检查文件夹是否存在
        if self.iml_folder.exists() or self.mc_folder.exists():
            # noinspection PyTypeChecker
            warn_msgbox = QMessageBox.warning(None, '注意',
                                '文件夹内存在可能的冲突，是否继续初始化（冲突的文件夹将会被删除）',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore, QMessageBox.No)

            if warn_msgbox == QMessageBox.Yes and self.iml_folder.exists():
                self.handle_folder_conflict(self.iml_folder)
            elif warn_msgbox == QMessageBox.Yes and not self.iml_folder.exists():
                self.iml_folder.mkdir()
            if warn_msgbox == QMessageBox.Yes and self.mc_folder.exists():
                self.handle_folder_conflict(self.mc_folder)
            elif warn_msgbox == QMessageBox.Yes and not self.mc_folder.exists():
                self.mc_folder.mkdir()

            if warn_msgbox == QMessageBox.Ignore:
                pass
            if warn_msgbox == QMessageBox.No:
                sys.exit(0)
        else:
            self.mc_folder.mkdir()
            self.iml_folder.mkdir()


    @staticmethod
    def handle_folder_conflict(path):
        # 文件夹冲突排查
        if not path.is_dir():
            path.unlink()
            path.mkdir()

        elif any(path.iterdir()):
            shutil.rmtree(path)
            path.mkdir()
