import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class MainWidget(QWidget):
	"""docstring for MainWidget"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Lab 9')
		self.label1 = QLabel('Nicolas & Rodrigo', self)
		self.img = QLabel()
		self.pmap = QPixmap('otter_boi.jpeg')
		self.img.setPixmap(self.pmap)
		vbox = QVBoxLayout()

		vbox.addWidget(self.label1)
		vbox.addWidget(self.img)

		
		self.setLayout(vbox)
		self.setGeometry(100,100,600,400)
		self.show()


app = QApplication(sys.argv)
ex = MainWidget()
sys.exit(app.exec_())