
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import *




class Simple_drawing_window(QWidget):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.points = []
        self.resize(400, 330)
        self.label = QLabel(self)
        self.label.setText("Drag the mouse to draw")
        self.label.move(140, 260)
        self.button = QPushButton(self)
        self.button.setText("Clear")
        self.button.move(160, 280)
        self.button.clicked.connect(self.clear_points)



    def clear_points(self):

        self.points = []
        self.update()



    def mouseMoveEvent(self, event):

        self.points.append(event.pos())
        self.update()

    

    def paintEvent(self, e):

        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 0))
        for point in self.points:
            p.drawPie(point.x(), point.y(), 10, 10, 0, 180 * 32)
        p.end()

        

def main():

    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()



if __name__ == "__main__":

    sys.exit(main())