from PySide import QtCore
from util import mil2NanoSec, nano2MilSec
from PySide import QtCore


class ThreadViewController(QtCore.QObject):
    Settings = {
        'Slider Range' : 10000,
        'Page Step' : 100
    }

    viewTimeChanged = QtCore.Signal(str)

    def __init__(self, model, view, duration, slider):
        QtCore.QObject.__init__(self)
        self._model = model
        self._view = view
        self._view_time = model.start()
        self.setDuration(duration)
        self._slider = slider

        # setup dependent widgets
        self._slider.setRange(0, self.Settings['Slider Range'])
        self._slider.setPageStep(self.Settings['Page Step'])
        # setup signals & slots
        self._slider.sliderMoved.connect(self._sliderSlot)

    def viewTime(self):
        return self._view_time

    def duration(self):
        return self._duration

    @QtCore.Slot(str)
    def setDuration(self, duration):
        self._duration = mil2NanoSec(int(duration))
        self._view.setModel(
            self._model.events(self._view_time, self._duration),
            self._view_time,
            self._view_time + self._duration
        )
        self._view.repaint()

    @QtCore.Slot(long)
    def setViewTime(self, view_time):
        self._view_time = view_time
        self._view.setModel(
            self._model.events(self._view_time, self._duration),
            self._view_time,
            self._view_time + self._duration
        )
        self.viewTimeChanged.emit(str(nano2MilSec(view_time)))
        self._view.repaint()

    @QtCore.Slot(int)
    def _sliderSlot(self, position):
        model_duration = self._model.end() - self._model.start()
        self.setViewTime((((long(position) * model_duration)) / long(self._slider.maximum())) + self._model.start())