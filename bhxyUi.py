# from maa.library import Library
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from ui.bhxy_UI import Ui_Form
from PySide6.QtCore import QThread, Signal
from bhxy import Bhxy
import os


class WorkThread(QThread):
    """
    解决扫描模块多线程时卡死
    """
    adb_device_signal = Signal(list)
    adb_connect_signal = Signal(int)

    def __init__(self, bhxy):
        """

        Args:
            bhxy: bhxy.py
        """
        super().__init__()
        self.adb_connect_index = None
        self.task_type = None
        self.adb_device = []
        self.bhxy = bhxy
        self.task_bool = False
        self.max_battle = 3
        self.double_bool = True

        self.adb_connect_signal.connect(self.get_adb_connect_signal)

    def set_task_type(self, task_type):
        self.task_type = task_type

    def set_task_bool(self, task_bool):
        self.task_bool = task_bool

    def set_max_battle(self, max_battle):
        self.max_battle = max_battle

    def set_double_bool(self, double_bool):
        self.double_bool = double_bool

    def get_adb_connect_signal(self, index):
        self.adb_connect_index = index

    def run(self):
        if self.task_type == 'scan_adb':
            self.adb_device = self.bhxy.get_adb_device()
            self.adb_device_signal.emit(self.adb_device)

        if self.task_type == 'connect_adb':
            print(self.adb_connect_index)
            print(self.adb_device)
            print(self.adb_device[self.adb_connect_index])
            self.bhxy.connect_adb(self.adb_device[self.adb_connect_index])

        if self.task_type == 'start_expedition':
            self.bhxy.start_expedition(task_bool=self.task_bool, max_battle=self.max_battle,
                                       double_bool=self.double_bool)

        if self.task_type == 'start_cycle_battle':
            self.bhxy.start_cycle_battle(self.max_battle, self.double_bool)


class MyWindow2(QMainWindow, Ui_Form):
    text_edit_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.thread = None
        self.adb_device = None
        self.setupUi(self)
        self.setWindowTitle('崩崩自动化小工具 by:MMDFTJ')
        self.setWindowIcon(QIcon("./images/icon.png"))
        # pixmap = QPixmap('./images/backgroundImage2.png')
        self.setStyleSheet("QMainWindow {background-image: url('./images/backgroundImage.png') no-repeat center center fixed;background-size: cover;background-position: center center;}")
        # 与bhxy.py中的callback绑定，从那边传回数据给logPlainTextEdit
        self.text_edit_signal.connect(lambda x: self.logPlainTextEdit.appendPlainText(x))
        self.bhxy = Bhxy(self.text_edit_signal)
        # 绑定点击事件
        self.scanAdbPushButton.clicked.connect(self.start_threading_from_scan_adb_button)
        self.adbConnectPushButton.clicked.connect(self.connect_adb_button)
        self.startPushButton.clicked.connect(self.start_task)
        self.clearLogPushButton.clicked.connect(self.clear_log)
        self.screenshotPushButton.clicked.connect(self.open_screenshot)
        self.stopPushButton.clicked.connect(self.stop_task)
        # 监听下选框的变化 修改另一个下选框
        self.adbAddressEditableComboBox.currentIndexChanged.connect(self.update_adb_ip_port_editable_combo_box)
        self.tasksComboBox.currentIndexChanged.connect(self.update_setting_scroll_area)
        # 往任务列表中添加任务名字
        self.tasksComboBox.addItems(['清日常', '重复刷关卡'])

    def start_threading_from_scan_adb_button(self):
        """
        从线程中启动扫描adb接口，防止点击扫描后界面卡死

        self.thread.adb_device_signal.connect(self.scan_adb_button)是把signal.emit参数返回给self.scan_adb_button
        Returns:

        """
        self.thread = WorkThread(self.bhxy)
        self.thread.set_task_type('scan_adb')
        self.thread.adb_device_signal.connect(self.scan_adb_button)
        self.thread.start()

    def scan_adb_button(self, adb_device):
        """
        接收来至adb_device_signal.emit的参数，处理self.adb_device
        Args:
            adb_device: 模拟器端口列表

        Returns:

        """
        self.adb_device = adb_device
        self.adbAddressEditableComboBox.clear()
        self.adbIpPortEditableComboBox.clear()
        for i in range(len(self.adb_device)):
            print(f'序号{i}:模拟器{self.adb_device[i].name} {self.adb_device[i].address}')

        # 往下拉框中添加参数
        self.adbAddressEditableComboBox.addItems(
            [str(i) + ':' + self.adb_device[i].name for i in range(len(self.adb_device))])
        self.adbIpPortEditableComboBox.addItems([self.adb_device[i].address for i in range(len(self.adb_device))])

    def connect_adb_button(self):
        """
        连接adb，往QThread.adb_connect_signal传递参数，用来选择用户选择的哪个接口
        Returns:

        """
        self.thread.adb_connect_signal.emit(self.adbAddressEditableComboBox.currentIndex())
        self.thread.set_task_type('connect_adb')
        self.thread.start()

    def update_adb_ip_port_editable_combo_box(self):
        """
        监听下选框变化
        Returns:

        """
        self.adbIpPortEditableComboBox.setCurrentIndex(self.adbAddressEditableComboBox.currentIndex())

    def update_setting_scroll_area(self, index):
        """
        监听下选框变化
        Returns:

        """
        self.settingStackedWidget.setCurrentIndex(index)

    def start_task(self):
        """
        启动，判断下选框的index是多少判断是哪个任务。
        Returns:

        """
        self.bhxy.tasker.set_a(0)
        if self.tasksComboBox.currentIndex() == 0:
            task_bool = self.clearPhysicalStrengthCheckBox.isChecked()
            double_bool = self.doubleCheckBox_clear.isChecked()
            max_battle = int(self.repetitionsLineEdit_clear.text())
            # self.thread = WorkThread(self.bhxy, task_bool, max_battle, double_bool)
            self.thread.set_task_type('start_expedition')
            self.thread.set_task_bool(task_bool)
            self.thread.set_double_bool(double_bool)
            self.thread.set_max_battle(max_battle)
            self.thread.start()
        if self.tasksComboBox.currentIndex() == 1:
            double_bool = self.dobleCheckBox.isChecked()
            max_battle = int(self.repetitionsLineEdit.text())
            # self.thread = WorkThread(self.bhxy, max_battle=max_battle, double_bool=double_bool)
            self.thread.set_task_type('start_cycle_battle')
            self.thread.set_double_bool(double_bool)
            self.thread.set_max_battle(max_battle)
            self.thread.start()

    def stop_task(self):
        """
        停止函数
        Returns:

        """
        self.logPlainTextEdit.appendPlainText('强制中断')
        self.bhxy.tasker.set_a(1)

    def clear_log(self):
        self.logPlainTextEdit.clear()

    def open_screenshot(self):
        exe = r'.\ImageCropper'
        self.logPlainTextEdit.appendPlainText('打开截图工具文件夹')
        os.startfile(exe)


if __name__ == '__main__':
    app = QApplication()
    window = MyWindow2()
    window.show()
    app.exec()
