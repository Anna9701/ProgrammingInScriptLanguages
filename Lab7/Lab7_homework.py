import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QAction, QApplication, QVBoxLayout, QRadioButton, QButtonGroup, \
    QWidget, QSlider, QLineEdit, QLabel, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        bl = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(bl)
        self.setCentralWidget(widget)

        cb = QCheckBox('Show title', self)
        cb.stateChanged.connect(self.changeTitle)
        bl.addWidget(cb)

        options = ['Czerwony', 'Żółty', 'Zielony']
        rb = [QRadioButton(o) for o in options]
        cbg = QButtonGroup(self)
        cbg.setExclusive(True)
        for id, ch in enumerate(options):
            rb = QRadioButton(ch)
            cbg.addButton(rb)
            cbg.setId(rb, id)
            bl.addWidget(rb)
        cbg.buttonClicked.connect(self.nowyKolor)

        self.lineEdit = QLineEdit('0')
        objValidator = QIntValidator(self)
        objValidator.setRange(0, 255)
        self.lineEdit.setValidator(objValidator)
        self.lineEdit.textChanged.connect(self.lineEdit_change)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(255)
        self.slider.setMinimum(0)
        self.slider.valueChanged.connect(self.slider_change)

        self.rectangle = QLabel()
        self.rectangle.setGeometry(QRect(0, 550, 150, 31))

        bl.addWidget(self.rectangle)
        bl.addWidget(self.slider)
        bl.addWidget(self.lineEdit)

        exitAction = QAction('Exit', self)
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
        self.setWindowTitle('Sample')
        self.show()

    def changeTitle(self, state):
        # odczytanie stanu obiektu
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')

    def nowyKolor(self, button):
        self.statusBar().showMessage(button.text() + " " + str(self.sender().checkedId()))

    def lineEdit_change(self, value):
        if not value:
            return
        self.slider.setValue(int(value))

    def slider_change(self, v):
        self.lineEdit.setText(str(v))
        self.rectangle.setStyleSheet("QWidget {background-color:rgb(%s,%s,%s)}" % (v, v, v))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
