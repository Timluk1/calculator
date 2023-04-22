# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 523)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 26, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: #161a1c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -30, 401, 191))
        self.frame.setStyleSheet("background-color: #2c3036")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.output_text = QtWidgets.QLabel(self.frame)
        self.output_text.setGeometry(QtCore.QRect(20, 110, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.output_text.setFont(font)
        self.output_text.setStyleSheet("QLabel{\n"
"  color: white;\n"
"}")
        self.output_text.setText("")
        self.output_text.setObjectName("output_text")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(-10, 80, 551, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.input_text = QtWidgets.QLabel(self.frame)
        self.input_text.setGeometry(QtCore.QRect(20, 50, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("QLabel{\n"
"  color: white;\n"
"}")
        self.input_text.setText("")
        self.input_text.setObjectName("input_text")
        self.button_c = QtWidgets.QPushButton(self.centralwidget)
        self.button_c.setGeometry(QtCore.QRect(0, 160, 101, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 135, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.button_c.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_c.setFont(font)
        self.button_c.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"    background-color: #878787;\n"
"}")
        self.button_c.setObjectName("button_c")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(0, 230, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_7.setObjectName("button_7")
        self.button_pr = QtWidgets.QPushButton(self.centralwidget)
        self.button_pr.setGeometry(QtCore.QRect(100, 160, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_pr.setFont(font)
        self.button_pr.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"    background-color: #878787;\n"
"}")
        self.button_pr.setObjectName("button_pr")
        self.button_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_del.setGeometry(QtCore.QRect(200, 160, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_del.setFont(font)
        self.button_del.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"    background-color: #878787;\n"
"}")
        self.button_del.setObjectName("button_del")
        self.button_umn = QtWidgets.QPushButton(self.centralwidget)
        self.button_umn.setGeometry(QtCore.QRect(300, 160, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_umn.setFont(font)
        self.button_umn.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"    background-color: #878787;\n"
"}")
        self.button_umn.setObjectName("button_umn")
        self.button_pl = QtWidgets.QPushButton(self.centralwidget)
        self.button_pl.setGeometry(QtCore.QRect(300, 230, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_pl.setFont(font)
        self.button_pl.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #ff9900\n"
"}")
        self.button_pl.setObjectName("button_pl")
        self.button_min = QtWidgets.QPushButton(self.centralwidget)
        self.button_min.setGeometry(QtCore.QRect(300, 300, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_min.setFont(font)
        self.button_min.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #ff9900\n"
"}")
        self.button_min.setObjectName("button_min")
        self.button_answer = QtWidgets.QPushButton(self.centralwidget)
        self.button_answer.setGeometry(QtCore.QRect(300, 370, 101, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.button_answer.setFont(font)
        self.button_answer.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #ff9900\n"
"}")
        self.button_answer.setObjectName("button_answer")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(0, 300, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_4.setObjectName("button_4")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(0, 370, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_1.setObjectName("button_1")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(100, 230, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(200, 230, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_9.setObjectName("button_9")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(100, 300, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(200, 300, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_6.setObjectName("button_6")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(100, 370, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(200, 370, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_3.setObjectName("button_3")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(0, 440, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_0.setObjectName("button_0")
        self.button_toch = QtWidgets.QPushButton(self.centralwidget)
        self.button_toch.setGeometry(QtCore.QRect(200, 440, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        self.button_toch.setFont(font)
        self.button_toch.setStyleSheet("QPushButton {\n"
"  color: white;\n"
"}")
        self.button_toch.setObjectName("button_toch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_c.setText(_translate("MainWindow", "C"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_pr.setText(_translate("MainWindow", "%"))
        self.button_del.setText(_translate("MainWindow", "/"))
        self.button_umn.setText(_translate("MainWindow", "x"))
        self.button_pl.setText(_translate("MainWindow", "+"))
        self.button_min.setText(_translate("MainWindow", "-"))
        self.button_answer.setText(_translate("MainWindow", "="))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_toch.setText(_translate("MainWindow", "."))
