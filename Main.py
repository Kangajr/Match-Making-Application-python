import sys
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from welcome import WelcomeScreen

##########################################
##  RUNNING THE APPLICATION             ##
##########################################

app = QApplication(sys.argv)  #yuertjhr
widget = QStackedWidget()
welcomewindow = WelcomeScreen(widget)
widget.addWidget(welcomewindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())

#this is kizer

#this is Anthony 
#This is a modification




