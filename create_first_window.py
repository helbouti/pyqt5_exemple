import sys
from PyQt5 import QtWidgets
class  MainWindow:
	def __init__(self):
		self.app=QtWidgets.QApplication(sys.argv)
		self.window=QtWidgets.QMainWindow()
		self.window.setWindowTitle("our first form")
		#self.window.setGeometry(0,0,500,500)
		#self.window.showMaximized()
		self.window.show()
		sys.exit(self.app.exec_())
		
main=MainWindow()