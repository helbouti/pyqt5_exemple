import sys
from PyQt5 import QtWidgets,QtGui
class  MainWindow:
	def __init__(self):
		self.app=QtWidgets.QApplication(sys.argv)
		self.window=QtWidgets.QMainWindow()
		
		self.initGui()
		self.window.setWindowTitle("our first form")
		self.window.setGeometry(400,100,300,500)
		#self.window.showMaximized()
		self.window.setStyleSheet("""background:#333;
			border:3px solid #4e4e4e;
			""")
		self.window.show()
		sys.exit(self.app.exec_())
		
	def initGui(self):
		#button1
		self.displayImage1Btn=QtWidgets.QPushButton("displayImage1",self.window)
		self.displayImage1Btn.setGeometry(170,420,120,30)
		self.displayImage1Btn.setStyleSheet("""background
			:#4e4e4e; color:#7f7f7f
			""")
		self.displayImage1Btn.clicked.connect(self.displayImage1)

		#button2
		self.displayImage2Btn=QtWidgets.QPushButton("displayImage2",self.window)
		self.displayImage2Btn.setGeometry(10,420,120,30)
		self.displayImage2Btn.setStyleSheet("""background
			:#4e4e4e; color:#7f7f7f
			""")
		self.displayImage2Btn.clicked.connect(self.displayImage2)

		self.label=QtWidgets.QLabel(self.window)
		self.label.setGeometry(0,0,300,400)
		self.label.setStyleSheet("background:#111")

		
		
		
	def displayImage1(self):
		self.imagePath1="cute_girl1.png"
		self.image1=QtGui.QImage(self.imagePath1)
		self.pixmap1=QtGui.QPixmap.fromImage(self.image1)
		self.label.setPixmap(self.pixmap1)
		self.label.setScaledContents(True)

	def displayImage2(self):
		self.imagePath2="cute_girl2.png"
		self.image2=QtGui.QImage(self.imagePath2)
		self.pixmap2=QtGui.QPixmap.fromImage(self.image2)
		self.label.setPixmap(self.pixmap2)
		self.label.setScaledContents(True)
main=MainWindow()