# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import os, time
import subprocess
import threading
from subprocess import check_output
import urllib
import  json
import time
import string

global browser_flag, RDPBinary, RDPDomain, RDPServer, RDPDomainFlags, RDPServerFlags, RDPMultiScreenFlags, RDPUserFlags, RDPPasswordFlags, RDPFullScreenFlags, screenWidth, screenHeight, ssid, ssid_pass, hostip, multi_mode, ssids, monitorInfo, chrome_flag, rdpsoundFlag, odroidC2
RDPBinary = "xfreerdp"
RDPDomain = "" 
RDPServer = ""
RDPDomainFlags = "/d:"
RDPServerFlags = "/v:"
RDPUserFlags = "/u:"
RDPPasswordFlags = "/p:"
RDPFullScreenFlags = "/f"
RDPMultiScreenFlags = 1
screenWidth = 0
screenHeight = 0
ssid = ""
ssid_pass = ""
config = {}
multi_mode = 2
browser_flag = 0
ssids = []
monitorInfo = []
chrome_flag = 0
rdpsoundFlag = 0


def disableMouseClick():
    proc = subprocess.Popen("xmodmap -e \"pointer = 1 2 0\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (out, err) = proc.communicate()
    #proc = subprocess.Popen("xmodmap -e \"keycode 64 = \"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #(out, err) = proc.communicate()
    #proc = subprocess.Popen("xmodmap -e \"keycode 108 = \"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #(out, err) = proc.communicate()
def resetMouseKeyboard():
    proc = subprocess.Popen("xmodmap -e \"pointer = default\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #(out, err) = proc.communicate()
    #proc = subprocess.Popen("setxkbmap -layout us", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #(out, err) = proc.communicate()

def checkSpecialCharacter(str):
    retstr=""
    for c in str:
        if c in string.punctuation:
            retstr = retstr + '\\'
        retstr = retstr + c
    return retstr

class mainwindowapp(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=None)
    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            print('KeyPress: %s [%r]' % (event.key(), source))
            return True
            #event.ignore()
    def closeEvent(self, event):
        event.ignore()

class QDoublePushButton(QPushButton):
    doubleClicked = pyqtSignal()
    clicked = pyqtSignal()
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.clicked.emit)
        super().clicked.connect(self.checkDoubleClick)
    @pyqtSlot()
    def checkDoubleClick(self):
        if self.timer.isActive():
            self.doubleClicked.emit()
            self.timer.stop()
        else:
            self.timer.start(250)

class MyQLabel(QLabel):
    # Custom click signal
    clicked = pyqtSignal()
    # Custom double click signal
    DoubleClicked = pyqtSignal()

    def __int__(self):
        super().__init__()

    # Override mouse click event
    def mousePressEvent(self, QMouseEvent):  # Click
        self.clicked.emit()

    # Override mouse double click event
    def mouseDoubleClickEvent(self, e):  # Double click
        self.DoubleClicked.emit()

class Ui_MainWindow(object):
    def __init__(self):
        global RDPServer, RDPMultiScreenFlags
        self.primaryscreen = {
        "width": 1920, 
        "height": 1080, 
        "sign_label_x":80,
        "sign_label_y":400, 
        "username_x_pos":80, 
        "username_y_pos":490, 
        "username_width":350,
        "username_height": 40,
        "pass_x_pos":80, 
        "pass_y_pos":570,
        "pass_width": 350,
        "pass_height": 40,
        "sign_button_x": 340,
        "sign_button_y": 630,
        "sign_button_width":150,
        "sign_button_height": 40
        }
        self.showPass = 0
        self.y_rate = 1.000; #vertical rate
        self.x_rate = 1.000; #horizental rate
        #self.settingsinfo = {"address" : " ", "multiscreen": 0}
        with open('/home/odroid/settings.dat') as json_file:
            data = json.load(json_file)
        RDPServer = data["address"]
        self.username = data["username"]
        #RDPMultiScreenFlags = data["multiscreen"]
        self.blur_effect_settings = QGraphicsBlurEffect()
        self.blur_effect_settings.setBlurRadius(20)
        self.blur_effect_settings.setEnabled(False)

        #disableMouseClick()
        # config = json.loads(readFromFile())
        # print("config file:", config)
    def checkBrowser(self):
        global chrome_flag
        commandline = "ps aux | grep chromium-browser"
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out, err) = proc.communicate()
        print(out)
        result = out.decode("utf-8")
        rows = result.split('\n')
        print(rows)
        chrome_flag = len(rows)

    def getWIFIList(self):
        commandline = "wpa_cli scan_result" 
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out, err) = proc.communicate()
        print(out)
        result = out.decode("utf-8")
        rows = result.split('\n')
        rows_num = len(rows)
        cells = []
        ssids = []
        for row in rows:
            print(row)
        for index in range(2, (len(rows) - 1)):
            cell = rows[index].split('\t')
            cells.append(cell)
            ssids.append(cell[len(cell) - 1])
        print(ssids)
        return ssids
    def setwifinetwork(self, ssid, password):
        commandline = "wpa_cli list_network | grep " + ssid 
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out, err) = proc.communicate()
        result = out.decode("utf-8")
        print(result)
        if len(result) > 0:
            cell = result.split('\t')
            commandline = "wpa_cli -i wlan0 select_network " + cell[0] 
            proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out, err) = proc.communicate()
            print(cell)
        else:
            commandline = "wpa_cli -i wlan0 add_network"
            proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out, err) = proc.communicate()
            result = out.decode("utf-8")
            result = result.split('\n')
            print(result)
            network_id = result[0]
            commandline = "wpa_cli -i wlan0 set_network " + network_id + " ssid " + "'\"" + ssid + "\"'"
            print(commandline)
            proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out, err) = proc.communicate()
            print(out)
            commandline = "wpa_cli -i wlan0 set_network " + network_id + " psk " + "'\"" + password + "\"'"
            proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out, err) = proc.communicate()
            print(out)
            commandline = "wpa_cli -i wlan0 select_network " + network_id
            proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (out, err) = proc.communicate()

    def onClickOkButton(self):
        global RDPServer, RDPMultiScreenFlags, multi_mode, ssids
        self.blur_effect_settings.setEnabled(False)
        self.settings_menu.hide()
        RDPServer = self.hostip_text.text()
        print("Host IP:", RDPServer)
        #ssid = str(self.ssid_combo.currentText())
        #password = str(self.wifipass_text.text())
        #print("wifi info:",ssid, password)
        error_text = ""
        #print(ssids)
        data = {"address": RDPServer, "username": self.username}
        with open('/home/odroid/settings.dat', 'w') as outfile:
            json.dump(data, outfile)

        #if len(ssid) > 0 and len(password) > 0:
        #    self.setwifinetwork(ssid, password)
        #    t_end = time.time() + 15
        #    while time.time() < t_end:
        #        try:
        #            if (wireless.current() is not None):
        #                self.error_widget.show()
        #                error_text = "wifi is connected."
        #                break
        #            else:
        #                self.error_widget.show()
        #                error_text = "wifi is not connected."
                    # print(wifipath)
        #        except:
        #            print('Wifi Status checking failed')
        #    self.error_content.setText(error_text)
        #else:
        #    print('NOT CONNECTING')

    def onClickCancelButton(self):
        self.blur_effect_settings.setEnabled(False)
        self.settings_menu.hide()
    @pyqtSlot()
    def settingsHandler(self):
        print(">>> settings")
        self.blur_effect_settings.setEnabled(True)
        self.settings_menu.show()
    @pyqtSlot()
    def shutdownHandler(self):
        print(">>> Shutting Down......")
        os.system('sudo poweroff')

    @pyqtSlot()
    def restartHandler(self):
        print(">>> Restarting .....")
        commandline = "sudo reboot"
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out, err) = proc.communicate()
        
        print("-------------------------------------------------------------")
    @pyqtSlot()
    def onClickInternetButton(self):
        global monitorInfo
        self.main_widget.setCursor(Qt.WaitCursor)
        #commandline = "chromium-browser --start-maximized"
        commandline = "chromium-browser --window-position=0,0 --window-size=" + str(screenWidth) + "," +str(screenHeight)
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(proc)
        time.sleep(4)
        self.main_widget.setCursor(Qt.ArrowCursor)
        
    def isMultiScreenClone(self):
        global RDPMultiScreenFlags, multi_mode
        if self.multiscreen_clone.isChecked():
            RDPMultiScreenFlags = 1
            multi_mode = 1
        else:
            RDPMultiScreenFlags = 0
            multi_mode = 0
        print("multi_mode:", multi_mode)

    def isMultiScreenExtended(self, state):
        global RDPMultiScreenFlags, multi_mode
        if state == QtCore.Qt.Checked:
            RDPMultiScreenFlags = 1
            multi_mode = 2
        else:
            RDPMultiScreenFlags = 0
            multi_mode = 0
        print("multi_mode:", multi_mode)
    def setRDPSound(self, state):
        global rdpsoundFlag
        if state == QtCore.Qt.Checked:
            rdpsoundFlag = 1
        else:
            rdpsoundFlag = 0
        print("Sound Enable:", rdpsoundFlag) 
  
    def isMultiScreenSingle(self):
        global RDPMultiScreenFlags, multi_mode
        if self.multiscreen_single.isChecked():
            RDPMultiScreenFlags = 0
            multi_mode = 0
        print("multi_mode:", multi_mode)

    def buttonClickHandler(self):
        print(">>>>>>>>>>>>>>>>>>")
        global RDPBinary, RDPDomain, RDPServer, RDPDomainFlags, RDPServerFlags, RDPUserFlags, RDPPasswordFlags, RDPFullScreenFlags, RDPMultiScreenFlags, chrome_flag, rdpsoundFlag
        self.checkBrowser()
        resetMouseKeyboard()
        print(chrome_flag)
        username = self.username_text.text()
        print("user name: ", username)
        password = self.password_text.text()
        print("password: ", password)

        #  xfreerdp /v:192.168.3.100 /u:pi /p:12345678 /f
        commandline = ""
        userinfo = username.split('\\')
        if len(userinfo) > 1:
            username = checkSpecialCharacter(userinfo[1])
            print("user info:", username)
            RDPDomain = checkSpecialCharacter(userinfo[0])
            print("domain info:", RDPDomain)
            password = checkSpecialCharacter(password)
            print("password info:", password)
            commandline = RDPBinary + " " + RDPServerFlags + RDPServer + " " + RDPUserFlags + username + " " + RDPPasswordFlags + password + " " + RDPDomainFlags + RDPDomain + " " + "/f /cert-ignore /usb:auto /sound /microphone /gdi:hw /rfx /network:auto -bitmap-cache -glyph-cache -fonts -offscreen-cache"
        else:
            commandline = RDPBinary + " " + RDPServerFlags + RDPServer + " " + RDPUserFlags + username + " " + RDPPasswordFlags + password + " " + "/f /cert-ignore /usb:auto /sound /microphone /gdi:hw /rfx /network:auto -bitmap-cache -glyph-cache -fonts -offscreen-cache"
        #commandline = RDPBinary + " " + RDPServerFlags + RDPServer + " " + RDPUserFlags + username + " " + RDPPasswordFlags + password + " " + "/f /cert-ignore /usb:auto /sound /microphone /gdi:hw /rfx /network:auto -bitmap-cache -glyph-cache -fonts -offscreen-cache"   

        print("commandline: ", commandline)
        #run script
        proc = subprocess.Popen(commandline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.main_widget.setCursor(Qt.WaitCursor)
        (out, err) = proc.communicate()
        print(">>> out: \n")
        print(out)
        print(">>> error: \n")
        print(err)
        str_out = out.decode("utf-8")
        self.main_widget.setCursor(Qt.ArrowCursor)
        if "ERRCONNECT_LOGON_FAILURE" in str_out:
            self.warning_widgt.show()
            self.warning_content.setText("Wrong username or password. Please try again")
        elif "ERRCONNECT_CONNECT_FAILED" in str_out:
            self.warning_widgt.show()
            self.warning_content.setText("Could not connect to cloud server")
        elif "ERRCONNECT_SECURITY_NEGO_CONNECT_FAILED" in str_out:
            self.warning_widgt.show()
            self.warning_content.setText("Could not connect to cloud server")
        else:
            self.warning_widgt.hide()
            self.warning_content.setText(" ")

        self.password_text.setText("")
        self.username = self.username_text.text()
        data = {"address": RDPServer, "username": self.username}
        with open('/home/odroid/settings.dat', 'w') as outfile:
            json.dump(data, outfile)
        disableMouseClick()
        # self.error_content.adjustSize()

    def chooseBackground(self, w):
        print("screenWidth: ", screenWidth)
        print("screenHeight:", screenHeight)
        if screenWidth == 640 and screenHeight == 360:
            w.setStyleSheet("border-image: url(:/images/background/background_640X360.png);")
        elif screenWidth == 640 and screenHeight == 480:
            w.setStyleSheet("border-image: url(:/images/background/background_640X480.png);")
        elif screenWidth == 720 and screenHeight == 480:
            w.setStyleSheet("border-image: url(:/images/background/background_720X480.png);")
        elif screenWidth == 720 and screenHeight == 576:
            w.setStyleSheet("border-image: url(:/images/background/background_720X576.png);")
        elif screenWidth == 800 and screenHeight == 600:
            w.setStyleSheet("border-image: url(:/images/background/background_800X600.png);")
        elif screenWidth == 1024 and screenHeight == 768:
            w.setStyleSheet("border-image: url(:/images/background/background_1024X768.png);")
        elif screenWidth == 1280 and screenHeight == 720:
            w.setStyleSheet("border-image: url(:/images/background/background_1280X720.png);")
        elif screenWidth == 1280 and screenHeight == 800:
            w.setStyleSheet("border-image: url(:/images/background/background_1280X800.png);")
        elif screenWidth == 1280 and screenHeight == 960:
            w.setStyleSheet("border-image: url(:/images/background/background_1280X960.png);")
        elif screenWidth == 1280 and screenHeight == 1024:
            w.setStyleSheet("border-image: url(:/images/background/background_1280X1024.png);")
        elif screenWidth == 1360 and screenHeight == 768:
            w.setStyleSheet("border-image: url(:/images/background/background_1360X768.png);")
        elif screenWidth == 1366 and screenHeight == 768:
            w.setStyleSheet("border-image: url(:/images/background/background_1366X768.png);")
        elif screenWidth == 1440 and screenHeight == 900:
            w.setStyleSheet("border-image: url(:/images/background/background_1440X900.png);")
        elif screenWidth == 1536 and screenHeight == 864:
            w.setStyleSheet("border-image: url(:/images/background/background_1536X864.png);")
        elif screenWidth == 1600 and screenHeight == 900:
            w.setStyleSheet("border-image: url(:/images/background/background_1600X900.png);")
        elif screenWidth == 1680 and screenHeight == 1050:
            w.setStyleSheet("border-image: url(:/images/background/background_1680X1050.png);")
        elif screenWidth == 1920 and screenHeight == 1080:
            w.setStyleSheet("border-image: url(:/images/background/background_1920X1080.png);")
        elif screenWidth == 1920 and screenHeight == 1200:
            w.setStyleSheet("border-image: url(:/images/background/background_1920X1200.png);")
        elif screenWidth == 2048 and screenHeight == 1152:
            w.setStyleSheet("border-image: url(:/images/background/background_2048X1152.png);")
        elif screenWidth == 2560 and screenHeight == 1080:
            w.setStyleSheet("border-image: url(:/images/background/background_2560X1080.png);")
        elif screenWidth == 2560 and screenHeight == 1440:
            w.setStyleSheet("border-image: url(:/images/background/background_2560X1440.png);")
        elif screenWidth == 3440 and screenHeight == 1440:
            w.setStyleSheet("border-image: url(:/images/background/background_3440X1440.png);")
        elif screenWidth == 3840 and screenHeight == 2160:
            w.setStyleSheet("border-image: url(:/images/background/background_3840X2160.png);")
        else:
            print(" !!! The background image is not existed for current resolution. !!! ")
            w.setStyleSheet("border-image: url(:/images/background/background_1920X1080.png);")
    def showpassword(self):
        if self.showPass == 0:
            self.password_text.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.eyeicon.setStyleSheet("border-image: url(:/images/showicon.png);")
            self.showPass = 1
        else:
            self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
            self.eyeicon.setStyleSheet("border-image: url(:/images/hideicon.png);")
            self.showPass = 0
    def onWarningCancelButton(self):
        self.warning_content.setText("")
        self.warning_widgt.hide()

    def setupUi(self, MainWindow):
        global RDPServer, browser_flag, screenWidth, screenHeight
        self.x_rate = screenWidth / 1920
        self.y_rate = screenHeight / 1080
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(self.primaryscreen["width"], self.primaryscreen["height"]) #Main Window Size
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(0,0, screenWidth,screenHeight))
        self.chooseBackground(self.main_widget) #self.main_widget.setStyleSheet()
        self.main_widget.setObjectName("main_widget")
        self.main_widget.setGraphicsEffect(self.blur_effect_settings)
        self.main_widget.setCursor(Qt.ArrowCursor)

        self.login_widget = QtWidgets.QWidget(self.main_widget)
        self.login_widget.setGeometry(QtCore.QRect(int(self.x_rate * 80), int(self.y_rate * 256), int(self.x_rate * 360), int(self.y_rate * 420)))
        self.login_widget.setStyleSheet("border-image:none")
        self.login_widget.setObjectName("login_widget")

        self.warning_widgt = QtWidgets.QWidget(self.login_widget)
        self.warning_widgt.setGeometry(QtCore.QRect(0, 0, 360, 100))
        self.warning_widgt.setStyleSheet("background-color: #F24361; border-radius: 8px;")

        self.warningicon = MyQLabel(self.warning_widgt)
        self.warningicon.setGeometry(QtCore.QRect(16, 16, 20, 20))
        self.warningicon.setStyleSheet("border-image: url(:/images/warning.png); border-width: 0;")
        self.warningicon.setText("")
        self.warningicon.setObjectName("warningicon")

        self.warning_label = QtWidgets.QLabel(self.warning_widgt)
        self.warning_label.setGeometry(QtCore.QRect(52, 16, 256, 20))
        self.warning_label.setStyleSheet("color: rgb(255, 255, 255); font-family: Poppins; font-style: normal; font-weight: 600; font-size: 14px; line-height: 20px;")
        self.warning_label.setObjectName("warning_label")

        self.warning_close_button = QtWidgets.QPushButton(self.warning_widgt)
        self.warning_close_button.setGeometry(QtCore.QRect(324, 16, 20, 20))
        self.warning_close_button.setCheckable(False)
        self.warning_close_button.setStyleSheet("border-image:url(:/images/warning_close.png);")
        self.warning_close_button.setObjectName("warning_close_button")
        self.warning_close_button.clicked.connect(lambda: self.onWarningCancelButton())

        self.warning_content = QtWidgets.QLabel(self.warning_widgt)
        self.warning_content.setGeometry(QtCore.QRect(52, 44, 256, 40))
        self.warning_content.setStyleSheet("color: rgb(255, 255, 255); font-family: Poppins; font-style: normal; font-weight: 400; font-size: 14px; line-height: 20px;")
        self.warning_content.setObjectName("warning_content")
        self.warning_content.setText("Please try again")
        self.warning_widgt.hide()

        self.username_lb = QtWidgets.QLabel(self.login_widget)
        self.username_lb.setGeometry(QtCore.QRect(0, int(self.y_rate * 180), 360, 20))
        self.username_lb.setStyleSheet("border-image:none; background-color: transparent; color: rgba(255, 255, 255,0.8); font-family: Poppins; font-style: normal;font-weight: 600; font-size: 14px; line-height: 20px;")
        self.username_lb.setObjectName("username_lb")

        self.username_text = QtWidgets.QLineEdit(self.login_widget)
        self.username_text.setGeometry(QtCore.QRect(0, int(self.y_rate * 208), int(self.x_rate * 360), int(self.y_rate * 40)))
        self.username_text.setStyleSheet("border-image:none; color: rgb(255, 255, 255); background-color: rgb(73, 74, 92); border-radius:8px;\n")
        self.username_text.setObjectName("username_text")
        self.username_text.setText(self.username)

        self.password_lb = QtWidgets.QLabel(self.login_widget)
        self.password_lb.setGeometry(QtCore.QRect(0, int(self.y_rate * 264), 360, 20))
        self.password_lb.setStyleSheet("border-image:none; background-color: transparent; color: rgba(255, 255, 255,0.8); font-family: Poppins; font-style: normal;font-weight: 600; font-size: 14px; line-height: 20px;")
        self.password_lb.setObjectName("password_lb")

        self.password_text = QtWidgets.QLineEdit(self.login_widget)
        self.password_text.setGeometry(QtCore.QRect(0, int(self.y_rate * 292), int(self.x_rate * 360), int(self.y_rate * 40)))
        self.password_text.setStyleSheet("border-image:none; color: rgb(255, 255, 255); background-color: rgb(73, 74, 92); border-radius:8px;")
        self.password_text.setObjectName("password_text")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.login_button = QtWidgets.QPushButton(self.login_widget)
        self.login_button.setGeometry(QtCore.QRect(int(self.x_rate * 264), int(self.y_rate * 380), int(self.x_rate * 96), int(self.y_rate * 40)))
        self.login_button.setMinimumSize(QtCore.QSize(0, 0))
        self.login_button.setMaximumSize(QtCore.QSize(10000, 10000))
        self.login_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.login_button.setStyleSheet("background-color: #F24361; color: rgb(255, 255, 255); border-radius: 8px;font-family: Poppins; font-style: normal;font-weight: 600; font-size: 14px; line-height: 20px;")
        self.login_button.setCheckable(True)
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(lambda: self.buttonClickHandler())

        self.sign_label = QtWidgets.QLabel(self.login_widget)
        self.sign_label.setGeometry(QtCore.QRect(0, 124, 360, 32))
        self.sign_label.setStyleSheet("color: rgb(255, 255, 255); font-family: Poppins; font-style: normal; font-weight: 600; font-size: 24px; line-height: 32px;")
        self.sign_label.setObjectName("sign_label")

        self.eyeicon = MyQLabel(self.login_widget)
        self.eyeicon.setGeometry(QtCore.QRect(int(self.x_rate * 325), int(self.y_rate * 304), 20, 20))
        self.eyeicon.setStyleSheet("border-image: url(:/images/hideicon.png);")
        self.eyeicon.setText("")
        self.eyeicon.setObjectName("eyeicon")
        self.eyeicon.clicked.connect(lambda: self.showpassword())

        self.shutdown_widget = QtWidgets.QWidget(self.main_widget)
        self.shutdown_widget.setGeometry(QtCore.QRect(1814, 988, 70, 52))
        self.shutdown_widget.setStyleSheet("border-image:none; background-color: transparent;")
        self.shutdown_widget.setObjectName("shutdown_widget")
        self.shutdown_button = QDoublePushButton(self.shutdown_widget)
        self.shutdown_button.setGeometry(QtCore.QRect(17, 0, 32, 32))
        self.shutdown_button.setMinimumSize(QtCore.QSize(0, 0))
        self.shutdown_button.setStyleSheet("border-image: url(:/images/shutdown.png);")
        self.shutdown_button.setText("")
        self.shutdown_button.setObjectName("shutdown_button")
        self.shutdown_button.doubleClicked.connect(lambda: self.shutdownHandler())
        self.shutdown_lb = QtWidgets.QLabel(self.shutdown_widget)
        self.shutdown_lb.setGeometry(QtCore.QRect(0, 36, 70, 16))
        self.shutdown_lb.setStyleSheet("border-image: none; color: rgba(255, 255, 255, 0.8); font-family: Poppins; font-style: normal; font-weight: 600; font-size: 12px; line-height: 16px;")
        self.shutdown_lb.setObjectName("shutdown_lb")

        self.restart_widget = QtWidgets.QWidget(self.main_widget)
        self.restart_widget.setGeometry(QtCore.QRect(1727, 988, 60, 52))
        self.restart_widget.setStyleSheet("border-image:none; background-color: transparent;")
        self.restart_widget.setObjectName("restart_widget")
        self.restart_button = QDoublePushButton(self.restart_widget)
        self.restart_button.setGeometry(QtCore.QRect(8, 0, 32, 32))
        self.restart_button.setMinimumSize(QtCore.QSize(0, 0))
        self.restart_button.setStyleSheet("border-image: url(:/images/restart.png);")
        self.restart_button.setText("")
        self.restart_button.setObjectName("restart_button")
        self.restart_button.doubleClicked.connect(lambda: self.restartHandler())
        self.restart_lb = QtWidgets.QLabel(self.restart_widget)
        self.restart_lb.setGeometry(QtCore.QRect(0, 36, 60, 16))
        self.restart_lb.setStyleSheet("border-image: none; color: rgba(255, 255, 255, 0.8); font-family: Poppins; font-style: normal; font-weight: 600; font-size: 12px; line-height: 16px;")
        self.restart_lb.setObjectName("restart_lb")

        self.settings_widget = QtWidgets.QWidget(self.main_widget)
        self.settings_widget.setGeometry(QtCore.QRect(1633, 988, 60, 52))
        self.settings_widget.setStyleSheet("border-image:none; background-color: transparent;")
        self.settings_widget.setObjectName("settings_widget")
        self.settings_button = QDoublePushButton(self.settings_widget)
        self.settings_button.setGeometry(QtCore.QRect(11, 0, 32, 32))
        self.settings_button.setMinimumSize(QtCore.QSize(0, 0))
        self.settings_button.setStyleSheet("border-image: url(:/images/settings.png);")
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.settings_button.doubleClicked.connect(lambda: self.settingsHandler())
        self.settings_lb = QtWidgets.QLabel(self.settings_widget)
        self.settings_lb.setGeometry(QtCore.QRect(0, 36, 60, 16))
        self.settings_lb.setStyleSheet("border-image: none; color: rgba(255, 255, 255, 0.8); font-family: Poppins; font-style: normal; font-weight: 600; font-size: 12px; line-height: 16px;")
        self.settings_lb.setObjectName("settings_lb")

        self.internet_widget = QtWidgets.QWidget(self.main_widget)
        self.internet_widget.setGeometry(QtCore.QRect(int(self.x_rate * 1700), int(self.y_rate * 40), 145, 40))
        self.internet_widget.setStyleSheet("border-image:none; border-width:1; border-style:solid; border-color:rgb(255,255,255); border-radius:8px;")
        self.internet_widget.setObjectName("internet_widget")
        self.internet_button = QDoublePushButton(self.internet_widget)
        self.internet_button.setGeometry(QtCore.QRect(24, 10, 20, 20))
        self.internet_button.setMinimumSize(QtCore.QSize(0, 0))
        self.internet_button.setStyleSheet("border-image: url(:/images/internet.png);")
        self.internet_button.setText("")
        self.internet_button.setObjectName("internet_button")
        self.internet_button.doubleClicked.connect(lambda: self.onClickInternetButton())
        self.internet_lb = MyQLabel(self.internet_widget)
        self.internet_lb.setGeometry(QtCore.QRect(48, 10, 70, 20))
        self.internet_lb.setStyleSheet("border-image: none; color: rgb(255, 255, 255); border-style:none; font-family: Poppins; font-style: normal; font-weight: 600; font-size: 14px; line-height: 20px;")
        self.internet_lb.setObjectName("internet_lb")
        self.internet_lb.DoubleClicked.connect(lambda: self.onClickInternetButton())

        self.settings_menu = QtWidgets.QWidget(self.centralwidget)
        self.settings_menu.setGeometry(QtCore.QRect((screenWidth * 0.5 - int(self.x_rate * 372)), (screenHeight * 0.5 - int(self.y_rate * 177)), int(self.x_rate * 744), int(self.y_rate * 355)))
        self.settings_menu.setStyleSheet("border-image:transparent;background-color:#ffffff; border-radius:16px;")
        self.settings_menu.setObjectName("settings_menu")

        self.rdp_setting_lb = QtWidgets.QLabel(self.settings_menu)
        self.rdp_setting_lb.setGeometry(QtCore.QRect(int(self.x_rate * 24), int(self.y_rate * 105), int(self.x_rate * 696), 24))
        self.rdp_setting_lb.setStyleSheet("color: #121212; font-family: Poppins; font-style: normal; font-weight:600; font-size: 16px; line-height: 24px;")
        self.rdp_setting_lb.setObjectName("rdp_setting_lb")

        self.hostip_lb = QtWidgets.QLabel(self.settings_menu)
        self.hostip_lb.setGeometry(QtCore.QRect(int(self.x_rate * 178), int(self.y_rate * 158), int(self.x_rate * 78), 24))
        self.hostip_lb.setObjectName("hostip_lb")
        self.hostip_lb.setStyleSheet("color: #505050; font-family: Poppins; font-style: normal; font-weight:normal; font-size: 16px; line-height: 24px;")
        self.hostip_lb.setAlignment(QtCore.Qt.AlignRight)

        self.star = QtWidgets.QLabel(self.settings_menu)
        self.star.setGeometry(QtCore.QRect(int(self.x_rate * 24),int(self.y_rate * 158), int(self.x_rate * 154), 24))
        self.star.setStyleSheet("color: #F24361; font-family: Poppins; font-style: normal; font-weight:normal; font-size: 16px; line-height: 24px;")
        self.star.setObjectName("star")
        self.star.setAlignment(QtCore.Qt.AlignRight)

        self.settings_ok_button = QtWidgets.QPushButton(self.settings_menu)
        self.settings_ok_button.setGeometry(QtCore.QRect(int(self.x_rate * 416), int(self.y_rate * 283), int(self.x_rate * 144), int(self.y_rate * 48)))
        self.settings_ok_button.setStyleSheet("border: 1.5px solid #121212; border-radius: 8px;color:#121212; font-family: Poppins; font-style:normal; font-weight:600; font-size:16px; line-height:24px")
        self.settings_ok_button.setObjectName("settings_ok_button")
        self.settings_ok_button.clicked.connect(lambda: self.onClickOkButton())

        self.settings_cancel_button = QtWidgets.QPushButton(self.settings_menu)
        self.settings_cancel_button.setGeometry(QtCore.QRect(int(self.x_rate * 576), int(self.y_rate * 283), int(self.x_rate * 144), int(self.y_rate * 48)))
        self.settings_cancel_button.setStyleSheet("border: 1.5px solid #F24361; background-color: #F24361; border-radius: 8px; color:#121212; font-family: Poppins; font-style:normal; font-weight:600; font-size:16px; line-height:24px")
        self.settings_cancel_button.setObjectName("settings_cancel_button")
        self.settings_cancel_button.clicked.connect(lambda: self.onClickCancelButton())

        self.line = QtWidgets.QFrame(self.settings_menu)
        self.line.setGeometry(QtCore.QRect(int(self.x_rate * 24), int(self.x_rate * 258), int(self.x_rate * 696), 1))
        self.line.setStyleSheet("background-color: #E0E0E0;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.hostip_text = QtWidgets.QLineEdit(self.settings_menu)
        self.hostip_text.setGeometry(QtCore.QRect(int(self.x_rate * 272), int(self.y_rate * 146), int(self.x_rate * 448), int(self.y_rate * 48)))
        self.hostip_text.setStyleSheet("    background: #FFFFFF; combobox-popup: 0;\n"
"    border: 1px solid #CBCBCB; \n"
"    color:#505050; font-family: Poppins; font-style:normal; font-weight:normal; font-size:16px; line-height:24px;\n"
"    border-radius: 8px;\n")
        self.hostip_text.setText(RDPServer)
        self.hostip_text.setObjectName("hostip_text")

        self.line_2 = QtWidgets.QFrame(self.settings_menu)
        self.line_2.setGeometry(QtCore.QRect(int(self.x_rate * 24), int(self.y_rate * 81), int(self.x_rate * 696), 1))
        self.line_2.setStyleSheet("background-color: #E0E0E0;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.wifi_setting_lb_3 = QtWidgets.QLabel(self.settings_menu)
        self.wifi_setting_lb_3.setGeometry(QtCore.QRect(int(self.x_rate * 24), int(self.y_rate * 24), int(self.x_rate * 200), 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wifi_setting_lb_3.setFont(font)
        self.wifi_setting_lb_3.setObjectName("wifi_setting_lb_3")

        self.settings_close_button = QtWidgets.QPushButton(self.settings_menu)
        self.settings_close_button.setGeometry(QtCore.QRect(int(self.x_rate * 696), int(self.y_rate * 28), 24, 24))
        self.settings_close_button.setStyleSheet("border-image:url(:/images/closeicon.png);\n"
"width:24;\n"
"height:24;")
        self.settings_close_button.setObjectName("settings_close_button")
        self.settings_close_button.clicked.connect(lambda: self.onClickCancelButton())

        self.loading_widget = QtWidgets.QWidget(self.centralwidget)
        self.loading_widget.setGeometry(QtCore.QRect(0,0, screenWidth,screenHeight))
        self.loading_widget.setStyleSheet("border-image: none;")
        self.loading_widget.setObjectName("loading_widget")

        self.settings_menu.hide()
        self.main_widget.raise_()
        self.settings_menu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_lb.setText(_translate("MainWindow", "User name"))
        self.password_lb.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Sign in"))
        self.sign_label.setText(_translate("MainWindow", "Sign in"))
        self.warning_label.setText(_translate("MainWindow", "Error!"))
        self.shutdown_lb.setText(_translate("MainWindow", "Shutdown"))
        self.restart_lb.setText(_translate("MainWindow", "Restart"))
        self.settings_lb.setText(_translate("MainWindow", "Settings"))
        self.internet_lb.setText(_translate("MainWindow", "Internet"))
        self.rdp_setting_lb.setText(_translate("MainWindow", "RDP Settings"))
        self.hostip_lb.setText(_translate("MainWindow", "HostIP:"))
        self.star.setText(_translate("MainWindow", "*"))
        self.settings_ok_button.setText(_translate("MainWindow", "OK"))
        self.settings_cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.wifi_setting_lb_3.setText(_translate("MainWindow", "Settings"))


class ScrollLabel(QScrollArea): 
  
    # contructor 
    def __init__(self, *args, **kwargs): 
        QScrollArea.__init__(self, *args, **kwargs) 
  
        # making widget resizable 
        self.setWidgetResizable(True) 
  
        # making qwidget object 
        content = QWidget(self) 
        self.setWidget(content) 
  
        # vertical box layout 
        lay = QVBoxLayout(content) 
  
        # creating label 
        self.label = QLabel(content) 
  
        # setting alignment to the text 
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop) 
  
        # making label multi-line 
        self.label.setWordWrap(True) 
  
        # adding label to the layout 
        lay.addWidget(self.label) 
  
    # the setText method 
    def setText(self, text): 
        # setting text to the label 
        self.label.setText(text)

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #RectScreen0 = QDesktopWidget().screenGeometry (0);
    #screenWidth = RectScreen0.right();
    #screenHeight = RectScreen0.bottom();
    screen = app.primaryScreen()
    size = screen.size()
    screenWidth = size.width()
    screenHeight = size.height()
    print(screenWidth, screenHeight)
    MainWindow = mainwindowapp()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

