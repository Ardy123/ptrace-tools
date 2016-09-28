#!/usr/bin/python
from PySide import QtGui, QtCore
import sys
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWnd = MainWindow()
    mainWnd.show()
    sys.exit(app.exec_())
