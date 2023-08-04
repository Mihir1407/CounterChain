# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(1000, 800)
        loginWindow.setMinimumSize(QtCore.QSize(1000, 800))
        loginWindow.setMaximumSize(QtCore.QSize(1000, 800))
        loginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 460, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/Icons/passwd.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 360, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/Icons/username.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(370, 610, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(570, 610, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.register_2.setFont(font)
        self.register_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_2.setObjectName("register_2")
        self.paswd_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.paswd_lineEdit.setGeometry(QtCore.QRect(400, 470, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.paswd_lineEdit.setFont(font)
        self.paswd_lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.paswd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.paswd_lineEdit.setObjectName("paswd_lineEdit")
        self.id_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_lineEdit.setGeometry(QtCore.QRect(400, 370, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.id_lineEdit.setFont(font)
        self.id_lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.id_lineEdit.setObjectName("id_lineEdit")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(60, 310, 871, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 381, 281))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.aboutus = QtWidgets.QPushButton(self.centralwidget)
        self.aboutus.setGeometry(QtCore.QRect(840, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.aboutus.setFont(font)
        self.aboutus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutus.setObjectName("aboutus")
        loginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuCounterChain = QtWidgets.QMenu(self.menubar)
        self.menuCounterChain.setObjectName("menuCounterChain")
        loginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginWindow)
        self.statusbar.setObjectName("statusbar")
        loginWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(loginWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(loginWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(loginWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionNew = QtWidgets.QAction(loginWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionQuit = QtWidgets.QAction(loginWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(loginWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(loginWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(loginWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionExit = QtWidgets.QAction(loginWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuCounterChain.addAction(self.actionExit)
        self.menubar.addAction(self.menuCounterChain.menuAction())

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.login.setText(_translate("loginWindow", "Login"))
        self.register_2.setText(_translate("loginWindow", "Register"))
        self.aboutus.setText(_translate("loginWindow", "About Us"))
        self.menuCounterChain.setTitle(_translate("loginWindow", "CounterChain"))
        self.actionOpen.setText(_translate("loginWindow", "Open"))
        self.actionSave.setText(_translate("loginWindow", "Save"))
        self.actionSave_As.setText(_translate("loginWindow", "Save As"))
        self.actionNew.setText(_translate("loginWindow", "New"))
        self.actionQuit.setText(_translate("loginWindow", "Quit"))
        self.actionCut.setText(_translate("loginWindow", "Cut"))
        self.actionCopy.setText(_translate("loginWindow", "Copy"))
        self.actionPaste.setText(_translate("loginWindow", "Paste"))
        self.actionExit.setText(_translate("loginWindow", "Exit"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
