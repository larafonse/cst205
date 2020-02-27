#
# my_gui
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 25 February 2020
# 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QHBoxLayout,QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
my_list=['red','blue','green','yellow','black']
dic = {
'red':[(0,0,0),'#e234r2'],
'blue':[(0,0,0),'#e234r2'],
'green':[(0,0,0),'#e234r2'],
'yellow':[(0,0,0),'#e234r2'],
'black':[(0,0,0),'#e234r2']
}

class MainWidget(QWidget):
	"""docstring for MainWidget"""
	def __init__(self):
		super().__init__()
		

		self.setWindowTitle('Colors')
		self.label1 = QLabel('CST 205 Color Exchange', self)
		self.label2 = QLabel('RGB:', self)
		self.label3 = QLabel('HEX:', self)

		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)
		self.my_label = QLabel("")

		vbox = QVBoxLayout()
		vbox.addWidget(self.label1)
		vbox.addWidget(self.my_combo_box)
		vbox.addWidget(self.label2)
		vbox.addWidget(self.label3)
		vbox.addWidget(self.my_label)

		self.setLayout(vbox)
		self.my_combo_box.currentIndexChanged.connect(self.update_ui)

	@pyqtSlot()
	def update_ui(self):
		my_text=self.my_combo_box.currentText()
		my_index=self.my_combo_box.currentIndex()
		self.label2.setText(f'RGB: {dic[my_list[my_index]][0]}')
		self.label3.setText(f'HEX: {dic[my_list[my_index]][1]}')

app = QApplication(sys.argv)
main = MainWidget()
main.show()
sys.exit(app.exec_())