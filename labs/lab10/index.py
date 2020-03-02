#
# my_gui
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 25 February 2020
# 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QHBoxLayout,QComboBox
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import pyqtSlot

# list for dropdown menu
my_list=['Pick a color','red','blue','green','yellow','black']

# dictionary that holds the rgb and hex variables of the colors
dic = {
'Pick a color':['',''],
'red':[(255,0,0),'#FF0000'],
'blue':[(0,0,255),'#0000FF'],
'green':[(0,255,0),'#00FF00'],
'yellow':[(255,255,0),'#FFFF00'],
'black':[(0,0,0),'#000000']
}

class colorWideget(QWidget):
	"""color widget that shows the color on a new window"""
	def __init__(self):
		super().__init__()
		
		
	
	def setColor(self,color):
		"""sets the color of the background"""
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(color[0],color[1],color[2]))
		self.setPalette(p) 

class MainWidget(QWidget):
	"""Main window that dispalys widgets """
	def __init__(self):
		super().__init__()
		# Background color declaration
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(0,0,0))
		self.setPalette(p) 
		
		# Label Declarations
		self.setWindowTitle('Colors')
		self.label1 = QLabel('<font color="white">CST 205 Color Exchange</font>', self)
		self.label2 = QLabel('<font color="white">RGB: </font>', self)
		self.label3 = QLabel('<font color="white">HEX: </font>', self)

		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)
		self.my_label = QLabel("")

		# Button that opens window with current color as the background
		self.btn = QPushButton("See Color!", self)
		self.btn.clicked.connect(self.newWindow) 

		# Widgets added to main window
		vbox = QVBoxLayout()
		vbox.addWidget(self.label1)
		vbox.addWidget(self.my_combo_box)
		vbox.addWidget(self.label2)
		vbox.addWidget(self.label3)
		vbox.addWidget(self.my_label)
		vbox.addWidget(self.btn)

		self.setLayout(vbox)
		self.my_combo_box.currentIndexChanged.connect(self.update_ui)
		
		# instatiation of second window
		self.second = colorWideget()

	@pyqtSlot()
	def update_ui(self):
		"""Updates the Rgb and Hex text"""
		my_index=self.my_combo_box.currentIndex()
		self.label2.setText(f'<font color="white">RGB: {dic[my_list[my_index]][0]}</font>')
		self.label3.setText(f'<font color="white">HEX: {dic[my_list[my_index]][1]}</font>')

	def newWindow(self):
		"""opens new window with the current color index as the background"""
		my_index=self.my_combo_box.currentIndex()
		self.second.setColor(dic[my_list[my_index]][0])
		self.second.show()


app = QApplication(sys.argv)
main = MainWidget()
main.show()
sys.exit(app.exec_())