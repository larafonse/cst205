# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# class Example(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.label1 = QLabel('Label 1', self)
# 		self.label2 = QLabel('Label 2', self)
# 		vbox = QVBoxLayout()
# 		vbox.addWidget(self.label1)
# 		vbox.addWidget(self.label2)
# 		self.setLayout(vbox)
# 		self.setGeometry(100,100,600,400)
# 		self.show() 


# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# app = QApplication(sys.argv)
# class MainWindow(QMainWindow):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('CST 205 Main Window')

# mainWin = MainWindow()
# mainWin.show()
# status = app.exec_()
# sys.exit(status)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		vbox = QVBoxLayout()

		self.my_btn = QPushButton("Button 1", self)
		self.my_lbl = QLabel('Button not clicked')
		self.my_btn.clicked.connect(self.on_click)

		vbox.addWidget(self.my_btn)
		vbox.addWidget(self.my_lbl)

		self.setLayout(vbox)

	@pyqtSlot()
	def on_click(self):
		self.my_lbl.setText('Button clicked')
		self.my_lbl.repaint()
		print('CLicked')

app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())