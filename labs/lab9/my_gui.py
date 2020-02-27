#
# my_gui
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 25 February 2020
# 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class MainWidget(QWidget):
	"""gui with labels, image, and bttns"""
	def __init__(self):
		# inherents init from parent class
		super().__init__()

		# window title and label set
		self.setWindowTitle('Lab 9')
		self.label1 = QLabel('Nicolas & Rodrigo', self)
		self.label2=QLabel('Is this a good otterboi?',self)
		self.label3=QLabel('',self)

		# image set
		self.img = QLabel()
		self.pmap = QPixmap('otterboi.jpg')
		self.img.setPixmap(self.pmap)

		# btns set
		self.btn1 = QPushButton("YES", self) 
		self.btn1.clicked.connect(self.on_click) 
		self.btn2 = QPushButton("NO", self)
		self.btn2.clicked.connect(self.on_click2)
		
		# set the layout
		vbox = QVBoxLayout()
		vbox.addWidget(self.label1)
		vbox.addWidget(self.img)
		vbox.addWidget(self.label2)
		vbox.addWidget(self.btn1) 
		vbox.addWidget(self.btn2)
		vbox.addWidget(self.label3)

		self.setLayout(vbox)
		self.setGeometry(100,100,600,400)
		self.show()
		

	@pyqtSlot()
	def on_click(self):
		"""will change text if yes btn is pressed"""
		self.label3.setText('You are correct! He is a good boy.')
		self.label3.repaint() 
	
	def on_click2(self):
		"""will change text if no btn is pressed"""
		self.label3.setText('You are wrong! He is a good boy.')
		self.label3.repaint() 



app = QApplication(sys.argv)
# instantiation
ex = MainWidget()
sys.exit(app.exec_())