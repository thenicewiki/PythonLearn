import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

# ----------------------------------------------#
# 简单pyqt5
# ----------------------------------------------#


def create_ui():
    app = QApplication(sys.argv)    # 所有pyqt5必须创建一个QApplication对象

    w = QWidget()   # 没有父类的widget将被作为窗口使用
    w.resize(550, 150)  # 大小
    w.move(300, 300)    # 起始坐标
    w.setWindowTitle('GUI')  # 标题
    w.show()
    # 应用进入主循环。在这个地方，事件处理开始执行。
    # 主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理。
    # 如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出。
    # 系统环境将会被通知应用是怎样被结束的
    sys.exit(app.exec_())


# ----------------------------------------------#
# pyqt5修改显示图标
# ----------------------------------------------#
class Example1(QWidget):

    def __init__(self):
        super().__init__()
        # super()方法返回了父类对象并调用了父类的构造方法
        self.__init_ui()

    def __init_ui(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('GUI')
        self.setWindowIcon(QIcon('f.ico'))

        self.show()

# ----------------------------------------------#
# pyqt5显示提示框
# ----------------------------------------------#


class Example2(QWidget):

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):

        # 设置提示框的字体和大小
        QToolTip.setFont(QFont('SansSerif', 20))

        # 用于显示组件的提示框
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个按键
        btn = QPushButton('Button', self)

        # 为按键创建提示框
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # setHint()方法给了按钮一个推荐的大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

# ----------------------------------------------#
# 关闭窗口
# ----------------------------------------------#


class Example3(QWidget):

    def __init__(self):
        super().__init__()

        self.__init_ui()

    def __init_ui(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

# 测试简单的创建ui


# create_ui()

app = QApplication(sys.argv)

# pyqt5修改显示图标
# ex = Example1()

# pyqt5显示提示框
# ex1 = Example2()

# pyqt5退出命令，理解信号与槽
ex2 = Example3()
sys.exit(app.exec_())