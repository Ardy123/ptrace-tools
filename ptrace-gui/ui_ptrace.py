# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ptrace.ui'
#
# Created: Sat Sep 24 23:58:17 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 919)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1028, 421))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timelineView = TimelineView(self.scrollAreaWidgetContents)
        self.timelineView.setObjectName("timelineView")
        self.verticalLayout_2.addWidget(self.timelineView)
        self.timelinetScrollBar = QtGui.QScrollBar(self.scrollAreaWidgetContents)
        self.timelinetScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.timelinetScrollBar.setObjectName("timelinetScrollBar")
        self.verticalLayout_2.addWidget(self.timelinetScrollBar)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 300))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.timeLineViewTab = QtGui.QWidget()
        self.timeLineViewTab.setObjectName("timeLineViewTab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.timeLineViewTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_13 = QtGui.QLabel(self.timeLineViewTab)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.threadListView = QtGui.QListView(self.timeLineViewTab)
        self.threadListView.setObjectName("threadListView")
        self.verticalLayout_3.addWidget(self.threadListView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.line_3 = QtGui.QFrame(self.timeLineViewTab)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtGui.QLabel(self.timeLineViewTab)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.timeLineViewTab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.globalStartTime = QtGui.QLabel(self.timeLineViewTab)
        self.globalStartTime.setObjectName("globalStartTime")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.globalStartTime)
        self.label_11 = QtGui.QLabel(self.timeLineViewTab)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.globalDuration = QtGui.QLabel(self.timeLineViewTab)
        self.globalDuration.setObjectName("globalDuration")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.globalDuration)
        self.label_14 = QtGui.QLabel(self.timeLineViewTab)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.viewStartTime = QtGui.QLabel(self.timeLineViewTab)
        self.viewStartTime.setObjectName("viewStartTime")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.viewStartTime)
        self.label_2 = QtGui.QLabel(self.timeLineViewTab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.viewDuration = QtGui.QLineEdit(self.timeLineViewTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewDuration.sizePolicy().hasHeightForWidth())
        self.viewDuration.setSizePolicy(sizePolicy)
        self.viewDuration.setInputMask("")
        self.viewDuration.setMaxLength(5)
        self.viewDuration.setObjectName("viewDuration")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.viewDuration)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(327, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.timeLineViewTab, "")
        self.threadInfoTab = QtGui.QWidget()
        self.threadInfoTab.setObjectName("threadInfoTab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.threadInfoTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtGui.QLabel(self.threadInfoTab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.eventTableView = QtGui.QTableView(self.threadInfoTab)
        self.eventTableView.setObjectName("eventTableView")
        self.verticalLayout_7.addWidget(self.eventTableView)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.line = QtGui.QFrame(self.threadInfoTab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtGui.QLabel(self.threadInfoTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtGui.QLabel(self.threadInfoTab)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.localTotalWaitTimeLabel = QtGui.QLabel(self.threadInfoTab)
        self.localTotalWaitTimeLabel.setObjectName("localTotalWaitTimeLabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.localTotalWaitTimeLabel)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.localPieChartView = PieChartView(self.threadInfoTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localPieChartView.sizePolicy().hasHeightForWidth())
        self.localPieChartView.setSizePolicy(sizePolicy)
        self.localPieChartView.setMinimumSize(QtCore.QSize(128, 128))
        self.localPieChartView.setSizeIncrement(QtCore.QSize(0, 0))
        self.localPieChartView.setObjectName("localPieChartView")
        self.verticalLayout.addWidget(self.localPieChartView)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.threadInfoTab)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtGui.QLabel(self.threadInfoTab)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtGui.QLabel(self.threadInfoTab)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.totalWaitTimeLabel = QtGui.QLabel(self.threadInfoTab)
        self.totalWaitTimeLabel.setObjectName("totalWaitTimeLabel")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.totalWaitTimeLabel)
        self.verticalLayout_6.addLayout(self.formLayout_3)
        self.globalPieChartView = PieChartView(self.threadInfoTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.globalPieChartView.sizePolicy().hasHeightForWidth())
        self.globalPieChartView.setSizePolicy(sizePolicy)
        self.globalPieChartView.setMinimumSize(QtCore.QSize(128, 128))
        self.globalPieChartView.setSizeIncrement(QtCore.QSize(0, 0))
        self.globalPieChartView.setObjectName("globalPieChartView")
        self.verticalLayout_6.addWidget(self.globalPieChartView)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.threadInfoTab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionO_pen = QtGui.QAction(MainWindow)
        self.actionO_pen.setObjectName("actionO_pen")
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menuFile.addAction(self.actionO_pen)
        self.menuFile.addAction(self.actionE_xit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionE_xit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pTrace Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Thread Display Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Thread View Position", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "start time (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.globalStartTime.setText(QtGui.QApplication.translate("MainWindow", "N/A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "duration (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.globalDuration.setText(QtGui.QApplication.translate("MainWindow", "N/A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "view position (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.viewStartTime.setText(QtGui.QApplication.translate("MainWindow", "N/A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "view duration (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.viewDuration.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.timeLineViewTab), QtGui.QApplication.translate("MainWindow", "Timeline View", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Thread Events", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Local Thread Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "total wait time:", None, QtGui.QApplication.UnicodeUTF8))
        self.localTotalWaitTimeLabel.setText(QtGui.QApplication.translate("MainWindow", "N/A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Global Thread Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "total wait time:", None, QtGui.QApplication.UnicodeUTF8))
        self.totalWaitTimeLabel.setText(QtGui.QApplication.translate("MainWindow", "N/A", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.threadInfoTab), QtGui.QApplication.translate("MainWindow", "Thread Info", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionO_pen.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

from piechartview import PieChartView
from timelineview import TimelineView
