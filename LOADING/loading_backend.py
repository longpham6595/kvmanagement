import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.resize(QSize(600, 750))
        #self.ToolsBTN = QPushButton('tab', self)
        #self.ToolsBTN.resize(100, 40)
        #self.ToolsBTN.move(60, 300)

        #self.CPS = QPushButton('tab1', self)
        #self.CPS.resize(100, 40)
        #self.CPS.move(130, 600)

        #self.Creator = QPushButton('tab2', self)
        #self.Creator.resize(100, 40)
        #self.Creator.move(260, 50)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(500, 200)
        self.startUIWindow()

        #Tạo file load trên dev
        self.movie = QMovie("id-loading-5.gif")
        #Tạo load trong software cài đặt
        #self.movie = QMovie('\link')
         
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("Processing database, please wait ...")
        self.show()

    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
