#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

path = r'c:/stuff/png/'



class GridLayout2(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('grid layout')

        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)


        self.setLayout(grid)
        self.resize(350, 300)

class MyWindow(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QMainWindow.__init__(self, parent)
		
		self.setWindowTitle('Icon')
		self.setWindowIcon(QtGui.QIcon(path + 'Add.png'))
		self.setToolTip('This is <b>myWidget</b>')
		QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))			

		exit = QtGui.QAction(QtGui.QIcon(path + 'Cancel.png'), 'E&xit', self)
		exit.setShortcut('Ctrl+Q')
		exit.setStatusTip('Exit application')
		self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
		
		self.statusBar().showMessage('Ready')
		
		menubar = self.menuBar()
		file = menubar.addMenu('&File')
		file.addAction(exit)
		
		main = GridLayout2()
		self.setCentralWidget(main)


		
	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Message', \
		"Are you sure you want to quit?", QtGui.QMessageBox.Yes | \
		QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

		
		
app = QtGui.QApplication(sys.argv)

widget = MyWindow()

widget.show()

sys.exit(app.exec_())
