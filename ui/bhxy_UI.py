# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bhxy2重新设计后.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, ComboBox, EditableComboBox,
    LineEdit, PlainTextEdit, PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(772, 406)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 725, 361))
        self.gridLayout_4 = QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BodyLabel = BodyLabel(self.layoutWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1)

        self.scanAdbPushButton = PushButton(self.layoutWidget)
        self.scanAdbPushButton.setObjectName(u"scanAdbPushButton")

        self.gridLayout.addWidget(self.scanAdbPushButton, 0, 1, 1, 1)

        self.adbAddressEditableComboBox = EditableComboBox(self.layoutWidget)
        self.adbAddressEditableComboBox.setObjectName(u"adbAddressEditableComboBox")

        self.gridLayout.addWidget(self.adbAddressEditableComboBox, 0, 2, 1, 1)

        self.adbIpPortEditableComboBox = EditableComboBox(self.layoutWidget)
        self.adbIpPortEditableComboBox.setObjectName(u"adbIpPortEditableComboBox")

        self.gridLayout.addWidget(self.adbIpPortEditableComboBox, 0, 3, 1, 1)

        self.adbConnectPushButton = PushButton(self.layoutWidget)
        self.adbConnectPushButton.setObjectName(u"adbConnectPushButton")

        self.gridLayout.addWidget(self.adbConnectPushButton, 0, 4, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.layoutWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout.addWidget(self.BodyLabel_2, 0, 5, 1, 1)

        self.startPushButton = PushButton(self.layoutWidget)
        self.startPushButton.setObjectName(u"startPushButton")

        self.gridLayout.addWidget(self.startPushButton, 0, 6, 1, 1)

        self.stopPushButton = PushButton(self.layoutWidget)
        self.stopPushButton.setObjectName(u"stopPushButton")

        self.gridLayout.addWidget(self.stopPushButton, 0, 7, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.screenshotPushButton = PushButton(self.layoutWidget)
        self.screenshotPushButton.setObjectName(u"screenshotPushButton")

        self.gridLayout_2.addWidget(self.screenshotPushButton, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_3 = BodyLabel(self.layoutWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout.addWidget(self.BodyLabel_3)

        self.tasksComboBox = ComboBox(self.layoutWidget)
        self.tasksComboBox.setObjectName(u"tasksComboBox")

        self.horizontalLayout.addWidget(self.tasksComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.settingStackedWidget = QStackedWidget(self.layoutWidget)
        self.settingStackedWidget.setObjectName(u"settingStackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.layoutWidget_2 = QWidget(self.page_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(40, 0, 258, 221))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.clearPhysicalStrengthCheckBox = CheckBox(self.layoutWidget_2)
        self.clearPhysicalStrengthCheckBox.setObjectName(u"clearPhysicalStrengthCheckBox")

        self.verticalLayout.addWidget(self.clearPhysicalStrengthCheckBox)

        self.doubleCheckBox_clear = CheckBox(self.layoutWidget_2)
        self.doubleCheckBox_clear.setObjectName(u"doubleCheckBox_clear")
        self.doubleCheckBox_clear.setCheckable(True)
        self.doubleCheckBox_clear.setChecked(False)

        self.verticalLayout.addWidget(self.doubleCheckBox_clear)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_5 = BodyLabel(self.layoutWidget_2)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout_4.addWidget(self.BodyLabel_5)

        self.repetitionsLineEdit_clear = LineEdit(self.layoutWidget_2)
        self.repetitionsLineEdit_clear.setObjectName(u"repetitionsLineEdit_clear")

        self.horizontalLayout_4.addWidget(self.repetitionsLineEdit_clear)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.PlainTextEdit = PlainTextEdit(self.layoutWidget_2)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")
        self.PlainTextEdit.setEnabled(False)
        self.PlainTextEdit.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-co"
                        "lor: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.PlainTextEdit)

        self.settingStackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.layoutWidget_3 = QWidget(self.page_6)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(40, 0, 258, 158))
        self.gridLayout_6 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.repetitionsLineEdit = LineEdit(self.layoutWidget_3)
        self.repetitionsLineEdit.setObjectName(u"repetitionsLineEdit")

        self.gridLayout_5.addWidget(self.repetitionsLineEdit, 1, 1, 1, 1)

        self.BodyLabel_6 = BodyLabel(self.layoutWidget_3)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.gridLayout_5.addWidget(self.BodyLabel_6, 1, 0, 1, 1)

        self.dobleCheckBox = CheckBox(self.layoutWidget_3)
        self.dobleCheckBox.setObjectName(u"dobleCheckBox")

        self.gridLayout_5.addWidget(self.dobleCheckBox, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.PlainTextEdit_2 = PlainTextEdit(self.layoutWidget_3)
        self.PlainTextEdit_2.setObjectName(u"PlainTextEdit_2")
        self.PlainTextEdit_2.setEnabled(False)
        self.PlainTextEdit_2.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-co"
                        "lor: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.PlainTextEdit_2, 1, 0, 1, 1)

        self.settingStackedWidget.addWidget(self.page_6)

        self.gridLayout_2.addWidget(self.settingStackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel_4 = BodyLabel(self.layoutWidget)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.horizontalLayout_2.addWidget(self.BodyLabel_4)

        self.clearLogPushButton = PushButton(self.layoutWidget)
        self.clearLogPushButton.setObjectName(u"clearLogPushButton")

        self.horizontalLayout_2.addWidget(self.clearLogPushButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.logPlainTextEdit = PlainTextEdit(self.layoutWidget)
        self.logPlainTextEdit.setObjectName(u"logPlainTextEdit")
        self.logPlainTextEdit.setEnabled(False)
        self.logPlainTextEdit.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-co"
                        "lor: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.logPlainTextEdit, 1, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.settingStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"Adb\u8fde\u63a5\uff1a", None))
        self.scanAdbPushButton.setText(QCoreApplication.translate("Form", u"\u626b\u63cf\u8bbe\u5907", None))
        self.adbAddressEditableComboBox.setInputMask("")
        self.adbAddressEditableComboBox.setText("")
        self.adbAddressEditableComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"adb\u5730\u5740", None))
        self.adbIpPortEditableComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"adb ip:port", None))
        self.adbConnectPushButton.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u8c03\u5ea6\u5668\uff1a", None))
        self.startPushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.stopPushButton.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.screenshotPushButton.setText(QCoreApplication.translate("Form", u"\u622a\u56fe\u5de5\u5177", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1\uff1a", None))
        self.tasksComboBox.setText("")
        self.clearPhysicalStrengthCheckBox.setText(QCoreApplication.translate("Form", u"\u6e05300\u4f53\u529b", None))
        self.doubleCheckBox_clear.setText(QCoreApplication.translate("Form", u"\u53cc\u500d\u5377", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5237\u53d6\u6b21\u6570\uff1a", None))
        self.repetitionsLineEdit_clear.setText(QCoreApplication.translate("Form", u"6", None))
        self.PlainTextEdit.setPlainText(QCoreApplication.translate("Form", u"\u52fe\u9009\u6e05300\u4f53\u529b\u4f1a\u5728\u5b8c\u6210\u5d29\u79d1\u540e\u81ea\u52a8\u627e\u5230\u6d3b\u52a8\u5173\u5361\u5237\u4e09\u6b21bouns\u5173\n"
"\n"
"\u5982\u679c\u60f3\u7528\u53cc\u500d\u5377\u7684\u8bdd\u628a\u5237\u53d6\u6b21\u6570\u586b\u62103", None))
        self.repetitionsLineEdit.setText(QCoreApplication.translate("Form", u"30", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u5237\u53d6\u6b21\u6570\uff1a", None))
        self.dobleCheckBox.setText(QCoreApplication.translate("Form", u"\u53cc\u500d\u5377", None))
        self.PlainTextEdit_2.setPlainText(QCoreApplication.translate("Form", u"\u91cd\u590d\u5237bouns\u5173\n"
"\n"
"\u53ef\u9009\u62e9\u662f\u5426\u4f7f\u7528\u53cc\u500d\u5377", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
        self.clearLogPushButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.logPlainTextEdit.setPlainText("")
    # retranslateUi

