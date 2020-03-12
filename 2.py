from PyQt5.QtCore import *


class simple_paint_program(QWidget):
    def __init__(self):
        QWidget.__init__(self,None):
        self.setWindowTitle("Simple Drawing")
        self.asd = QPixmap(400,400)
        
    def paintEvent(self, e):
        p = QPainter(self)
        p.begin(self)


        
    def reset(self):




if __name__ == '__main__'
    simple_paint_program()