import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QVBoxLayout, QRadioButton, QButtonGroup, \
    QWidget, QMessageBox, QHBoxLayout, QTextEdit, QFileDialog, \
    QComboBox


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        self.fileName = None
        self.fontSize = 12
        self.fontType = 'Arial'

    def initUI(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        hboxLayout = QHBoxLayout()
        widget.setLayout(hboxLayout)

        vboxWidget = QWidget()
        vboxLayout = QVBoxLayout()
        vboxWidget.setLayout(vboxLayout)
        hboxLayout.addWidget(vboxWidget)

        self.textField = QTextEdit()
        hboxLayout.addWidget(self.textField)

        fontSizeCb = QComboBox()
        for i in range(1, 42):
            fontSizeCb.addItem(str(i))
        fontSizeCb.setCurrentText(str(12))
        fontSizeCb.currentTextChanged.connect(self.changeFontSize)

        vboxLayout.addWidget(fontSizeCb)

        options = ['Times New Roman', 'Arial', 'Courier New']
        rb = [QRadioButton(o) for o in options]
        cbg = QButtonGroup(self)
        cbg.setExclusive(True)
        for id, ch in enumerate(options):
            rb = QRadioButton(ch)
            if id == 1:
                rb.setChecked(True)
            cbg.addButton(rb)
            cbg.setId(rb, id)
            vboxLayout.addWidget(rb)
        cbg.buttonClicked.connect(self.changeFontType)
        self.textField.setFont(QFont('Arial', 12))

        # colorGrid = QGridLayout()
        # colorPallete = QWidget()
        # colorPallete.setLayout(colorGrid)
        # vboxLayout.addWidget(colorPallete)
        # pb = [QPushButton(str(i)) for i in range(1, 20)]
        # for i in range(0, 3):
        #     colorGrid.addWidget(pb[i * 5], i, 0)
        #     colorGrid.addWidget(pb[i * 5 + 1], i, 1)
        #     colorGrid.addWidget(pb[i * 5 + 2], i, 2)
        #     colorGrid.addWidget(pb[i * 5 + 3], i, 3)
        #     colorGrid.addWidget(pb[i * 5 + 4], i, 4)


        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open file')
        openAction.triggered.connect(self.openFile)

        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New')
        newAction.triggered.connect(self.newFile)

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save')
        saveAction.triggered.connect(self.saveFile)

        saveAsAction = QAction('Save As', self)
        saveAsAction.setStatusTip('Save As')
        saveAsAction.triggered.connect(self.saveFileDialog)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(exitAction)

        cutAction = QAction('Cut', self)
        cutAction.setStatusTip('Cut')
        cutAction.setShortcut('Ctrl+X')
        cutAction.triggered.connect(self.cut)

        copyAction = QAction('Copy', self)
        cutAction.setStatusTip('Copy')
        cutAction.setShortcut('Ctrl+C')
        cutAction.triggered.connect(self.copy)

        editionMenu = menubar.addMenu('&Edition')
        editionMenu.addAction(cutAction)
        editionMenu.addAction(copyAction)

        toolbar = self.addToolBar('')
        toolbar.addAction(newAction)
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(saveAsAction)
        toolbar.addAction(exitAction)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Notepad')
        self.show()

    def changeFontSize(self, value):
        self.fontSize = value
        self.textField.setFont(QFont(self.fontType, int(self.fontSize)))

    def changeFontType(self, button):
        self.fontType = button.text()
        self.textField.setFont(QFont(self.fontType, int(self.fontSize)))

    def newFile(self):
        self.textField.clear()
        self.fileName = None
        self.statusBar().showMessage("New note opened")

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                       "All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            self.textField.setText(open(self.fileName, "rt").read())
            self.statusBar().showMessage("Opened " + self.fileName)

    def saveFile(self):
        if self.fileName is None:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                           "All Files (*);;Text Files (*.txt)", options=options)
        if self.fileName:
            open(self.fileName, "wt").write(self.textField.toPlainText())
            self.statusBar().showMessage("Saved " + self.fileName)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                       "All Files (*);;Text Files (*.txt)", options=options)
        if self.fileName:
            open(self.fileName, "wt").write(self.textField.toPlainText())
            self.statusBar().showMessage("Saved " + self.fileName)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def copy(self):
        selected = self.textField.textCursor().selectedText()
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(selected, mode=cb.Clipboard)
        self.statusBar().showMessage("Copied to clipboard")

    def cut(self):
        cursor = self.textField.textCursor()
        selected = cursor.selectedText()
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(selected, mode=cb.Clipboard)
        text = self.textField.toPlainText()
        self.textField.setText(text[:cursor.selectionStart()] + text[cursor.selectionEnd():])
        self.statusBar().showMessage("Cut to clipboard")

def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
