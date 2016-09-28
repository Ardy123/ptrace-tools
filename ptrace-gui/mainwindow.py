from PySide import QtGui, QtCore
from ui_ptrace import Ui_MainWindow
from threadsmodel import ThreadsModel
from threadviewcontroller import ThreadViewController
from util import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self._view_start_time = 0

    @QtCore.Slot("")
    def on_actionO_pen_triggered(self):
        filename = QtGui.QFileDialog.getOpenFileName(
            self, "FileDialog", ".log", "ptrace log files (*.log)")[0]
        if filename:
            self._model = ThreadsModel(open(filename, 'r'))
            # update Ui
            self.globalStartTime.setText(str(nano2MilSec(self._model.start())))
            self.globalDuration.setText(str(nano2MilSec(self._model.end() - self._model.start())))
            self.threadListView.setModel(self._model.threadListModel())
            self.threadListView.clicked.connect(self._threadSelected)
            # wire up controllers
            self._threadViewController = ThreadViewController(
                self._model,
                self.timelineView,
                self.viewDuration.text(),
                self.timelinetScrollBar
            )
            self.viewStartTime.setText(str(nano2MilSec(self._threadViewController.viewTime())))
            self._threadViewController.viewTimeChanged.connect(self.viewStartTime.setText)
            self._threadViewController.viewTimeChanged.connect(self._viewTimeChanged)
            self.viewDuration.textChanged.connect(self._threadViewController.setDuration)

    @QtCore.Slot(str)
    def _viewTimeChanged(self, time_str):
        self._threadSelected(self.threadListView.currentIndex())

    @QtCore.Slot(QtCore.QModelIndex)
    def _threadSelected(self, index):
        thread_id = self.threadListView.model().data(index)
        view_time = self._threadViewController.viewTime()
        duration = self._threadViewController.duration()
        # update event table, global & local thread stats
        self.eventTableView.setModel(self._model.threadEventModel(view_time, duration, thread_id))
        # update global thread stats
        globalStats = self._model.stats(self._model.start(), self._model.end() - self._model.start(), thread_id)
        self.totalWaitTimeLabel.setText(str(globalStats[1]))
        self.globalPieChartView.setModel((thread_id, globalStats[0]))
        # update local thread stats
        localStats = self._model.stats(view_time, duration, thread_id)
        self.localTotalWaitTimeLabel.setText(str(localStats[1]))
        self.localPieChartView.setModel((thread_id, localStats[0]))