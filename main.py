# coding: utf8
import win32clipboard as wc
import win32con

## win32api
# import win32api
# import json
import baidu_fanyi_spider as bfs
import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, pyqtSignal
from untitled import Ui_MainWindow

from system_hotkey import SystemHotkey


class Translater(QMainWindow, Ui_MainWindow):
    # 定义一个热键信号
    sig_keyhot = pyqtSignal(str)

    def __init__(self, parent=None):
        # 继承主窗口类
        super(Translater, self).__init__(parent)
        # 设置应用图标
        # self.setWindowIcon(QIcon('source/book.png'))
        # 获取屏幕对象
        self.screen = QDesktopWidget().screenGeometry()
        self.setupUi(self)
        # 仅支持最小化以及关闭按钮
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        # 去掉 toolbar 右键菜单
        self.setContextMenuPolicy(Qt.NoContextMenu)

        # self.textEdit.text()
        self.textEdit.setText("test value")

        self.translate.clicked.connect(self.translate_click)

        self.sig_keyhot.connect(self.translate_click)
        self.hk = SystemHotkey()
        self.hk.register(('control', 'shift', 'c'), callback=lambda x: self.send_key_event("start"))

    def translate_click(self):
        if self.checkBox.checkState() == Qt.Checked:
            rawtext = format_str(getCopyText())
        else:
            rawtext = self.textEdit.toPlainText()
        content = bfs.translate1(rawtext, 'en', 'zh')
        content = content['trans_result'][0]['dst']
        self.textEdit_2.setText(content)

    # 热键信号发送函数(将外部信号，转化成qt信号)
    def send_key_event(self, i_str):
        self.sig_keyhot.emit(i_str)


def getCopyText():
    wc.OpenClipboard()
    copytext = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return str(copytext)


def format_str(str):
    str = str.replace('\\x00', '')
    str = str.replace('\\r', '')
    str = str.replace('\\n', '')
    str = str.replace('\\xa1\\xb0', '"')
    str = str.replace('\\xa1\\xb1', '"')
    str = str.replace('\\xa8C', '-')
    str = str.replace('\\xa1\\xaf', "'")
    return str


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Translater = Translater()
    Translater.show()
    sys.exit(app.exec_())
