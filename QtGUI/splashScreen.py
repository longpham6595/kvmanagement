import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *


class LoadingGif(object):

    def mainUI(self, FrontWindow):
        FrontWindow.setObjectName("FTwindow")
        FrontWindow.resize(340, 60)
        self.centralwidget = QWidget(FrontWindow)
        self.centralwidget.setObjectName("main-widget")
        



        # Label Create
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(68, 20, 20, 20))
        self.label.setMinimumSize(QSize(250, 25))
        self.label.setMaximumSize(QSize(250, 25))
        self.label.setObjectName("lb1")
        FrontWindow.setCentralWidget(self.centralwidget)
  
        # Loading the GIF
        self.movie = QMovie("D:\CodingProjects\MyManageProject\kvmanagement\QtGUI\good.gif")
        self.label.setMovie(self.movie)
  
        self.startAnimation()
  
    # Start Animation
    def startAnimation(self):
        self.movie.start()
  
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    demo = LoadingGif()
    demo.mainUI(window)
    window.setWindowTitle("LOADING .. PLEASE WAIT ..")
    window.show()
    sys.exit(app.exec_())