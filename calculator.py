from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from file4 import Ui_MainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setFixedSize(401, 523)
        self.ui.setupUi(self)
        self.ui.button_0.clicked.connect(self.button_0)
        self.ui.button_1.clicked.connect(self.button_1)
        self.ui.button_2.clicked.connect(self.button_2)
        self.ui.button_3.clicked.connect(self.button_3)
        self.ui.button_4.clicked.connect(self.button_4)
        self.ui.button_5.clicked.connect(self.button_5)
        self.ui.button_6.clicked.connect(self.button_6)
        self.ui.button_7.clicked.connect(self.button_7)
        self.ui.button_8.clicked.connect(self.button_8)
        self.ui.button_9.clicked.connect(self.button_9)
        self.ui.button_toch.clicked.connect(self.button_toch)
        self.ui.button_umn.clicked.connect(self.button_umn)
        self.ui.button_pr.clicked.connect(self.button_pr)
        self.ui.button_del.clicked.connect(self.button_del)
        self.ui.button_c.clicked.connect(self.button_c)
        self.ui.button_answer.clicked.connect(self.button_answer)
        self.ui.button_pl.clicked.connect(self.button_pl)
        self.ui.button_min.clicked.connect(self.button_min)

    def button_0(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "0")

    def button_1(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "1")

    def button_2(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "2")

    def button_3(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "3")

    def button_4(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "4")

    def button_5(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "5")

    def button_6(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "6")

    def button_7(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "7")

    def button_8(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "8")

    def button_9(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "9")

    def button_toch(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + ".")

    def button_umn(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "*")

    def button_pr(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "%")

    def button_del(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "/")

    def button_c(self):
        self.ui.output_text.setText("")
        self.ui.input_text.setText("")

    def button_answer(self):
        try:
            self.ui.output_text.setText(str(eval(self.ui.input_text.text())))
        except Exception:
            self.ui.output_text.setText("OШИБКА!!")

    def button_pl(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "+")

    def button_min(self):
        operation = self.ui.input_text.text()
        self.ui.input_text.setText(operation + "-")


app2 = QtWidgets.QApplication([])
app = MainWindow()
app.show()
sys.exit(app2.exec())
