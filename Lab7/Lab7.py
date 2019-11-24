import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()

    def initUI(self):
        names = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '+', '0', '=']
        grid = QGridLayout()
        textbox = QLineEdit()

        grid.addWidget(textbox, 0, 0, 1, 3)
        j = 0
        pos = [(1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2),
               (3, 0), (3, 1), (3, 2),
               (4, 0), (4, 1), (4, 2)]
        for i in names:
            button = QPushButton(i)
            button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1


        self.setLayout(grid)
        self.move(300, 150)
        self.show()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        calculator = Calculator()
        self.setCentralWidget(calculator)
        exitAction = QAction(QIcon('exit_icon.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Calculator')
        self.statusBar().showMessage('Input number:')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
