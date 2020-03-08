#
# my_gui
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 25 February 2020
# 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QComboBox ,QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import pyqtSlot

# list for dropdown menu
my_list=['none','sepia','negative','grayscale','thumbnail']

class colorWideget(QWidget):
	"""color widget that shows the color on a new window"""
	def __init__(self):
		super().__init__()
		
class MainWidget(QWidget):
	"""Main window that dispalys widgets """
	def __init__(self):
		super().__init__()
		self.setStyleSheet("QLabel{ color: white; margin:none; text-align:center;}");
		# Background color declaration
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(0,0,0))
		self.setPalette(p) 
		
		# Label Declarations
		self.setWindowTitle('Image Search')
		self.label1 = QLabel('      Welcome to Rodrigo & Nicoolas\'s Enhanced Image Search', self)
		self.line = QLineEdit(self)
		self.filterLabel = QLabel('Filter:')
		self.tagLabel = QLabel('Tags:')

		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)
		

		# Button that opens window with current color as the background
		self.btn = QPushButton("Go!", self)
		self.btn.clicked.connect(self.newWindow) 

		# Widgets added to main window
		vbox = QVBoxLayout()
		vbox.addWidget(self.label1)

		hbox = QHBoxLayout()
		hbox.addWidget(self.filterLabel)
		hbox.addWidget(self.my_combo_box)
		hbox.addWidget(self.tagLabel)
		hbox.addWidget(self.line)
		

		mbox = QVBoxLayout()
		mbox.addLayout(vbox)
		mbox.addLayout(hbox)
		mbox.addWidget(self.btn)

		self.setLayout(mbox)
		self.my_combo_box.currentIndexChanged.connect(self.update_ui)
		
		# instatiation of second window


	@pyqtSlot()
	def update_ui(self):
		"""Updates the Rgb and Hex text"""
		my_index=self.my_combo_box.currentIndex()
		
	def newWindow(self):
		"""opens new window with the current color index as the background"""
		my_index=self.my_combo_box.currentIndex()


app = QApplication(sys.argv)
main = MainWidget()
main.show()
sys.exit(app.exec_())