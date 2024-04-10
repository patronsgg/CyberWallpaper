# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setMinimumSize(QtCore.QSize(900, 550))
        MainWindow.setMaximumSize(QtCore.QSize(900, 550))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setMouseTracking(False)
        self.main_frame.setAcceptDrops(False)
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.logo = QtWidgets.QLabel(self.main_frame)
        self.logo.setGeometry(QtCore.QRect(250, 30, 431, 201))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.logo.setFont(font)
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("image_program/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.layoutWidget = QtWidgets.QWidget(self.main_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 222, 261, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_lineedits = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout_lineedits.setContentsMargins(0, 0, 0, 0)
        self.layout_lineedits.setSpacing(1)
        self.layout_lineedits.setObjectName("layout_lineedits")
        self.login_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.login_line.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_line.setFont(font)
        self.login_line.setMouseTracking(False)
        self.login_line.setAcceptDrops(True)
        self.login_line.setStyleSheet("QLineEdit{\n"
"    border-radius: 2 px;\n"
"    border: 2px solid rgb(40, 40, 40);\n"
"    background-color: rgb(49, 49, 49);\n"
"    padding: 3px;\n"
"    color: rgb(131, 131, 131);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(123, 57, 145);\n"
"}")
        self.login_line.setFrame(True)
        self.login_line.setObjectName("login_line")
        self.layout_lineedits.addWidget(self.login_line)
        self.password_line = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_line.setFont(font)
        self.password_line.setStyleSheet("QLineEdit{\n"
"    border-radius: 2 px;\n"
"    border: 2px solid rgb(40, 40, 40);\n"
"    background-color: rgb(49, 49, 49);\n"
"    padding: 3px;\n"
"    color: rgb(131, 131, 131);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(123, 57, 145);\n"
"}")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.layout_lineedits.addWidget(self.password_line)
        self.forgotpass = QtWidgets.QPushButton(self.main_frame)
        self.forgotpass.setGeometry(QtCore.QRect(330, 300, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.forgotpass.setFont(font)
        self.forgotpass.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    padding: 0;\n"
"    color: rgb(131, 131, 131);\n"
"    pandding: 3px\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(123, 57, 145);\n"
"}")
        self.forgotpass.setObjectName("forgotpass")
        self.label = QtWidgets.QLabel(self.main_frame)
        self.label.setGeometry(QtCore.QRect(0, -8, 901, 541))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image_program/back_1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.layoutWidget_2 = QtWidgets.QWidget(self.main_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(330, 320, 261, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.layout_pushbuttons_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.layout_pushbuttons_2.setContentsMargins(0, 3, 0, 3)
        self.layout_pushbuttons_2.setSpacing(2)
        self.layout_pushbuttons_2.setObjectName("layout_pushbuttons_2")
        self.register_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("QPushButton{\n"
"    border-radius: 2 px;\n"
"    border: 2px solid rgb(40, 40, 40);\n"
"    background-color: rgb(49, 49, 49);\n"
"    padding: 3px;\n"
"    color: rgb(131, 131, 131);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(123, 57, 145);\n"
"}")
        self.register_2.setObjectName("register_2")
        self.layout_pushbuttons_2.addWidget(self.register_2)
        self.log_in = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.log_in.setFont(font)
        self.log_in.setStyleSheet("QPushButton{\n"
"    border-radius: 2 px;\n"
"    border: 2px solid rgb(40, 40, 40);\n"
"    background-color: rgb(49, 49, 49);\n"
"    padding: 3px;\n"
"    color: rgb(131, 131, 131);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(123, 57, 145);\n"
"}")
        self.log_in.setObjectName("log_in")
        self.layout_pushbuttons_2.addWidget(self.log_in)
        self.mistacke = QtWidgets.QFrame(self.main_frame)
        self.mistacke.setGeometry(QtCore.QRect(250, 0, 431, 31))
        self.mistacke.setStyleSheet("QFrame{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 84, 84);\n"
"}")
        self.mistacke.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mistacke.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mistacke.setObjectName("mistacke")
        self.name_error = QtWidgets.QLabel(self.mistacke)
        self.name_error.setGeometry(QtCore.QRect(20, 0, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name_error.setFont(font)
        self.name_error.setStyleSheet("")
        self.name_error.setObjectName("name_error")
        self.hide_error = QtWidgets.QPushButton(self.mistacke)
        self.hide_error.setGeometry(QtCore.QRect(390, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hide_error.setFont(font)
        self.hide_error.setStyleSheet("QPushButton{\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"    padding: 0;\n"
"    color:  rgb(49, 49, 49);\n"
"    pandding: 3px\n"
"    \n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    border: 2px solid rgb(123, 57, 145);\n"
"}")
        self.hide_error.setObjectName("hide_error")
        self.label.raise_()
        self.logo.raise_()
        self.layoutWidget.raise_()
        self.forgotpass.raise_()
        self.layoutWidget_2.raise_()
        self.mistacke.raise_()
        self.verticalLayout.addWidget(self.main_frame)
        self.creators_frame = QtWidgets.QFrame(self.centralwidget)
        self.creators_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.creators_frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(55, 55, 55);\n"
"}")
        self.creators_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.creators_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.creators_frame.setObjectName("creators_frame")
        self.layoutWidget1 = QtWidgets.QWidget(self.creators_frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, -3, 901, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.texts_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.texts_layout.setContentsMargins(3, 0, 5, 0)
        self.texts_layout.setSpacing(0)
        self.texts_layout.setObjectName("texts_layout")
        self.creator = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(12)
        self.creator.setFont(font)
        self.creator.setObjectName("creator")
        self.texts_layout.addWidget(self.creator)
        self.designer = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(12)
        self.designer.setFont(font)
        self.designer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.designer.setObjectName("designer")
        self.texts_layout.addWidget(self.designer)
        self.verticalLayout.addWidget(self.creators_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_line.setPlaceholderText(_translate("MainWindow", "login"))
        self.password_line.setPlaceholderText(_translate("MainWindow", "password"))
        self.forgotpass.setText(_translate("MainWindow", "i forgot my password"))
        self.register_2.setText(_translate("MainWindow", "register"))
        self.log_in.setText(_translate("MainWindow", "log in"))
        self.name_error.setText(_translate("MainWindow", "error"))
        self.hide_error.setText(_translate("MainWindow", "X"))
        self.creator.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#939393;\">  Create</span><span style=\" color:#939393;\"> by Patron</span></p></body></html>"))
        self.designer.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600; color:#939393;\">Design</span><span style=\" color:#939393;\"> by V0_1</span></p></body></html>"))