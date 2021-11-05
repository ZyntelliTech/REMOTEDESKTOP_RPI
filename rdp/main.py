# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1024, 768)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border-image: url(:/images/mdpZeroLogin.png);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.login_widget = QtWidgets.QWidget(self.centralwidget)
        self.login_widget.setGeometry(QtCore.QRect(30, 210, 301, 231))
        self.login_widget.setStyleSheet("border-image:none")
        self.login_widget.setObjectName("login_widget")
        self.username_lb = QtWidgets.QLabel(self.login_widget)
        self.username_lb.setGeometry(QtCore.QRect(20, 60, 77, 31))
        self.username_lb.setStyleSheet("border-image:none; \n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.username_lb.setObjectName("username_lb")
        self.username_text = QtWidgets.QLineEdit(self.login_widget)
        self.username_text.setGeometry(QtCore.QRect(10, 90, 281, 31))
        self.username_text.setStyleSheet("border-image:none; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(73, 74, 92);\n"
"border-radius:10px;")
        self.username_text.setObjectName("username_text")
        self.password_lb = QtWidgets.QLabel(self.login_widget)
        self.password_lb.setGeometry(QtCore.QRect(20, 120, 69, 31))
        self.password_lb.setStyleSheet("border-image:none; \n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.password_lb.setObjectName("password_lb")
        self.password_text = QtWidgets.QLineEdit(self.login_widget)
        self.password_text.setGeometry(QtCore.QRect(10, 150, 281, 31))
        self.password_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.password_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_text.setStyleSheet("border-image:none; \n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(73, 74, 92);\n"
"border-radius:10px;")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.pushButton = QtWidgets.QPushButton(self.login_widget)
        self.pushButton.setGeometry(QtCore.QRect(230, 190, 61, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(10000, 10000))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"border-radius: 10px;\n"
"")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.login_widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 24px;\n"
"line-height: 32px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.login_widget)
        self.label_2.setGeometry(QtCore.QRect(267, 159, 20, 13))
        self.label_2.setStyleSheet("border-image: url(:/images/hideicon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.restart_widget = QtWidgets.QWidget(self.centralwidget)
        self.restart_widget.setGeometry(QtCore.QRect(840, 650, 67, 68))
        self.restart_widget.setStyleSheet("border-image:none; background-color: transparent;")
        self.restart_widget.setObjectName("restart_widget")
        self.restart_button = QtWidgets.QPushButton(self.restart_widget)
        self.restart_button.setGeometry(QtCore.QRect(15, 22, 21, 20))
        self.restart_button.setMinimumSize(QtCore.QSize(0, 0))
        self.restart_button.setStyleSheet("border-image: url(:/images/restart.png);")
        self.restart_button.setText("")
        self.restart_button.setObjectName("restart_button")
        self.restart_lb = QtWidgets.QLabel(self.restart_widget)
        self.restart_lb.setGeometry(QtCore.QRect(6, 50, 51, 17))
        self.restart_lb.setStyleSheet("border-image: none; color: rgb(70, 99, 111);")
        self.restart_lb.setObjectName("restart_lb")
        self.shutdown_widget = QtWidgets.QWidget(self.centralwidget)
        self.shutdown_widget.setGeometry(QtCore.QRect(910, 650, 71, 61))
        self.shutdown_widget.setStyleSheet("border-image:none; background-color: transparent;")
        self.shutdown_widget.setObjectName("shutdown_widget")
        self.shutdown_button = QtWidgets.QPushButton(self.shutdown_widget)
        self.shutdown_button.setGeometry(QtCore.QRect(25, 21, 21, 21))
        self.shutdown_button.setMinimumSize(QtCore.QSize(0, 0))
        self.shutdown_button.setStyleSheet("border-image: url(:/images/shutdown.png);")
        self.shutdown_button.setText("")
        self.shutdown_button.setObjectName("shutdown_button")
        self.shutdown_lb = QtWidgets.QLabel(self.shutdown_widget)
        self.shutdown_lb.setGeometry(QtCore.QRect(9, 50, 71, 17))
        self.shutdown_lb.setStyleSheet("border-image: none; color: rgb(70, 99, 111);")
        self.shutdown_lb.setObjectName("shutdown_lb")
        self.settings_widget = QtWidgets.QWidget(self.centralwidget)
        self.settings_widget.setGeometry(QtCore.QRect(760, 650, 67, 68))
        self.settings_widget.setStyleSheet("border-image:none; background-color: transparent;")
        self.settings_widget.setObjectName("settings_widget")
        self.settings_button = QtWidgets.QPushButton(self.settings_widget)
        self.settings_button.setGeometry(QtCore.QRect(15, 10, 37, 37))
        self.settings_button.setMinimumSize(QtCore.QSize(0, 0))
        self.settings_button.setStyleSheet("border-image: url(:/images/settings.png);")
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.settings_lb = QtWidgets.QLabel(self.settings_widget)
        self.settings_lb.setGeometry(QtCore.QRect(6, 50, 57, 17))
        self.settings_lb.setStyleSheet("border-image: none; color: rgb(70, 99, 111);")
        self.settings_lb.setObjectName("settings_lb")
        self.blurFrame = QtWidgets.QFrame(self.settings_widget)
        self.blurFrame.setGeometry(QtCore.QRect(-750, -650, 1024, 768))
        self.blurFrame.setStyleSheet("border-image:none;")
        self.blurFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blurFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blurFrame.setObjectName("blurFrame")
        self.spinBox = QtWidgets.QSpinBox(self.blurFrame)
        self.spinBox.setGeometry(QtCore.QRect(150, 420, 42, 241))
        self.spinBox.setObjectName("spinBox")
        self.error_widget = QtWidgets.QWidget(self.centralwidget)
        self.error_widget.setGeometry(QtCore.QRect(310, 340, 391, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_widget.sizePolicy().hasHeightForWidth())
        self.error_widget.setSizePolicy(sizePolicy)
        self.error_widget.setMaximumSize(QtCore.QSize(500, 100))
        self.error_widget.setStyleSheet("border-image:none; background-color: rgba(255, 255, 255, 100)")
        self.error_widget.setObjectName("error_widget")
        self.error_content = QtWidgets.QLabel(self.error_widget)
        self.error_content.setGeometry(QtCore.QRect(60, 10, 436, 33))
        self.error_content.setMaximumSize(QtCore.QSize(500, 100))
        self.error_content.setStyleSheet("background-color: none")
        self.error_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.error_content.setText("")
        self.error_content.setTextFormat(QtCore.Qt.PlainText)
        self.error_content.setWordWrap(True)
        self.error_content.setIndent(-1)
        self.error_content.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.error_content.setObjectName("error_content")
        self.error_mark = QtWidgets.QGraphicsView(self.error_widget)
        self.error_mark.setGeometry(QtCore.QRect(9, 9, 40, 33))
        self.error_mark.setMaximumSize(QtCore.QSize(40, 40))
        self.error_mark.setStyleSheet("border-image: url(:/images/error.png); background-color: none;")
        self.error_mark.setObjectName("error_mark")
        self.internet_widget = QtWidgets.QWidget(self.centralwidget)
        self.internet_widget.setGeometry(QtCore.QRect(840, 40, 111, 24))
        self.internet_widget.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-width:1;\n"
"border-style:solid;\n"
"border-image:none;\n"
"border-radius:10;")
        self.internet_widget.setObjectName("internet_widget")
        self.internet_button = QtWidgets.QPushButton(self.internet_widget)
        self.internet_button.setGeometry(QtCore.QRect(10, 2, 21, 21))
        self.internet_button.setMinimumSize(QtCore.QSize(0, 0))
        self.internet_button.setStyleSheet("border-image: url(:/images/internet.png);")
        self.internet_button.setText("")
        self.internet_button.setObjectName("internet_button")
        self.internet_lb = QtWidgets.QLabel(self.internet_widget)
        self.internet_lb.setGeometry(QtCore.QRect(40, 3, 58, 19))
        self.internet_lb.setStyleSheet("border-image: none; color: rgb(70, 99, 111); border-style:none;")
        self.internet_lb.setObjectName("internet_lb")
##############################################################################################################
        self.settings_menu = QtWidgets.QWidget(self.centralwidget)
        self.settings_menu.setGeometry(QtCore.QRect(340, 130, 391, 431))
        self.settings_menu.setStyleSheet("border-image:transparent;\n"
"background-color:#ffffff;\n"
"border-radius:15px;")
        self.settings_menu.setObjectName("settings_menu")

        self.settings_menu_lb = QtWidgets.QLabel(self.settings_menu)
        self.settings_menu_lb.setGeometry(QtCore.QRect(30, 40, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.settings_menu_lb.setFont(font)
        self.settings_menu_lb.setObjectName("settings_menu_lb")

        self.line_1 = QtWidgets.QFrame(self.settings_menu)
        self.line_1.setGeometry(QtCore.QRect(30, 80, 321, 1))
        self.line_1.setStyleSheet("background-color: gray;")
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")

        self.settings_menu_close_bt = QtWidgets.QPushButton(self.settings_menu)
        self.settings_menu_close_bt.setGeometry(QtCore.QRect(350, 40, 16, 16))
        self.settings_menu_close_bt.setStyleSheet("border-image:url(:/images/closeicon.png);\n"
"width:24;\n"
"height:24;")
        self.settings_menu_close_bt.setObjectName("pushBsettings_menu_close_btutton_2")

        self.wifi_setting_lb = QtWidgets.QLabel(self.settings_menu)
        self.wifi_setting_lb.setGeometry(QtCore.QRect(30, 90, 351, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.wifi_setting_lb.setFont(font)
        self.wifi_setting_lb.setObjectName("wifi_setting_lb")

        self.ssid_lb = QtWidgets.QLabel(self.settings_menu)
        self.ssid_lb.setGeometry(QtCore.QRect(100, 130, 31, 17))
        self.ssid_lb.setObjectName("ssid_lb")
        self.wifipass_lb = QtWidgets.QLabel(self.settings_menu)
        self.wifipass_lb.setGeometry(QtCore.QRect(80, 170, 51, 17))
        self.wifipass_lb.setObjectName("wifipass_lb")

        self.ssid_combo = QtWidgets.QComboBox(self.settings_menu)
        self.ssid_combo.setGeometry(QtCore.QRect(140, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ssid_combo.setFont(font)
        self.ssid_combo.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.ssid_combo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.ssid_combo.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/images/down-arrow-icon.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.ssid_combo.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.ssid_combo.setEditable(False)
        self.ssid_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.ssid_combo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.ssid_combo.setFrame(True)
        self.ssid_combo.setObjectName("ssid_combo")
        self.ssid_combo.addItem("")
        self.ssid_combo.addItem("")
        self.ssid_combo.addItem("")
        self.ssid_combo.addItem("")
        self.ssid_combo.addItem("")
        self.ssid_combo.addItem("")

        self.wifipass_text = QtWidgets.QLineEdit(self.settings_menu)
        self.wifipass_text.setGeometry(QtCore.QRect(140, 164, 191, 31))
        self.wifipass_text.setStyleSheet(" border: 1px solid gray; border-radius: 5px;")
        self.wifipass_text.setObjectName("wifipass_text")

        self.line_2 = QtWidgets.QFrame(self.settings_menu)
        self.line_2.setGeometry(QtCore.QRect(30, 210, 321, 1))
        self.line_2.setStyleSheet("background-color: gray;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")


        self.rdp_setting_lb_2 = QtWidgets.QLabel(self.settings_menu)
        self.rdp_setting_lb_2.setGeometry(QtCore.QRect(30, 230, 96, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rdp_setting_lb_2.setFont(font)
        self.rdp_setting_lb_2.setObjectName("rdp_setting_lb_2")

        self.hostip_ld = QtWidgets.QLabel(self.settings_menu)
        self.hostip_ld.setGeometry(QtCore.QRect(90, 270, 41, 17))
        self.hostip_ld.setObjectName("hostip_ld")
        self.star = QtWidgets.QLabel(self.settings_menu)
        self.star.setGeometry(QtCore.QRect(70, 270, 20, 20))
        self.star.setStyleSheet("color: rgb(204, 0, 0);")
        self.star.setObjectName("star")

        self.hostip = QtWidgets.QLineEdit(self.settings_menu)
        self.hostip.setGeometry(QtCore.QRect(140, 264, 191, 31))
        self.hostip.setStyleSheet(" border: 1px solid gray; border-radius: 5px;")
        self.hostip.setObjectName("hostip")

        self.multimon_checkBox = QtWidgets.QCheckBox(self.settings_menu)
        self.multimon_checkBox.setEnabled(True)
        self.multimon_checkBox.setGeometry(QtCore.QRect(140, 320, 101, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multimon_checkBox.sizePolicy().hasHeightForWidth())
        self.multimon_checkBox.setSizePolicy(sizePolicy)
        self.multimon_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.multimon_checkBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.multimon_checkBox.setAutoFillBackground(False)
        self.multimon_checkBox.setStyleSheet("QCheckBox:indicator:checked\n"
"{\n"
"   image:url(:/images/checkicon.png);\n"
"  width:14;\n"
"  height:14;\n"
"}")
        self.multimon_checkBox.setCheckable(True)
        self.multimon_checkBox.setChecked(True)
        self.multimon_checkBox.setAutoRepeat(False)
        self.multimon_checkBox.setAutoExclusive(False)
        self.multimon_checkBox.setObjectName("multimon_checkBox")

        self.sound_checkBox = QtWidgets.QCheckBox(self.settings_menu)
        self.sound_checkBox.setGeometry(QtCore.QRect(140, 340, 81, 17))
        self.sound_checkBox.setStyleSheet("QCheckBox::indicator:unchecked\n"
"{\n"
"  border: 1px solid grey;\n"
"  border-radius:2;\n"
"}")
        self.sound_checkBox.setObjectName("sound_checkBox")


        self.settings_ok_button = QtWidgets.QPushButton(self.settings_menu)
        self.settings_ok_button.setGeometry(QtCore.QRect(160, 390, 89, 25))
        self.settings_ok_button.setStyleSheet("border: 2px solid black; border-radius: 5px;")
        self.settings_ok_button.setObjectName("settings_ok_button")
        self.settings_cancel_button = QtWidgets.QPushButton(self.settings_menu)
        self.settings_cancel_button.setGeometry(QtCore.QRect(260, 390, 89, 25))
        self.settings_cancel_button.setStyleSheet("background-color:red ;border-radius: 5px;")
        self.settings_cancel_button.setObjectName("settings_cancel_button")
        

       

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.username_lb.setText(_translate("MainWindow", "Username:"))
        self.password_lb.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
        self.label.setText(_translate("MainWindow", "Sign in"))
        self.restart_lb.setText(_translate("MainWindow", "Restart"))
        self.shutdown_lb.setText(_translate("MainWindow", "ShutDown"))
        self.settings_lb.setText(_translate("MainWindow", "Settings"))
        self.internet_lb.setText(_translate("MainWindow", "Internet"))
        self.wifi_setting_lb.setText(_translate("MainWindow", "Network Settings(option)"))
        self.ssid_lb.setText(_translate("MainWindow", "SSID:"))
        self.wifipass_lb.setText(_translate("MainWindow", "Password:"))
        self.rdp_setting_lb.setText(_translate("MainWindow", "RDP Settings"))
        self.hostip.setText(_translate("MainWindow", "HostIP:"))
        self.star.setText(_translate("MainWindow", "*"))
        self.settings_ok_button.setText(_translate("MainWindow", "OK"))
        self.settings_cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.ssid_combo.setItemText(0, _translate("MainWindow", "aaaa"))
        self.ssid_combo.setItemText(1, _translate("MainWindow", "bbbb"))
        self.ssid_combo.setItemText(2, _translate("MainWindow", "cccc"))
        self.ssid_combo.setItemText(3, _translate("MainWindow", "dddd"))
        self.ssid_combo.setItemText(4, _translate("MainWindow", "eeee"))
        self.ssid_combo.setItemText(5, _translate("MainWindow", "New Item"))
        self.multimon_checkBox.setText(_translate("MainWindow", "Multi-Monitors"))
        self.sound_checkBox.setText(_translate("MainWindow", "Sound"))
        self.settings_menu_lb.setText(_translate("MainWindow", "Settings"))
        self.settings_menu_close.setText(_translate("MainWindow", "X"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
