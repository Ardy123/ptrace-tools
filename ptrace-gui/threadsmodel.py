from PySide import QtCore, QtGui
from util import safe_next
from threadsource import *
from threadslistsink import ThreadsListSink
from threadindexsource import ThreadIndexSource
from timerangesink import TimeRangeSink
from eventsink import EventSink
from eventfilter import EventFilter
from waitsink import WaitSink


class _threadListModel(QtCore.QAbstractListModel):
    def __init__(self, thread_list):
        QtCore.QAbstractListModel.__init__(self)
        self._thread_list = thread_list

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._thread_list)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if QtCore.Qt.DisplayRole == role:
            return self._thread_list[index.row()]
        else:
            return None

class _eventTableView(QtCore.QAbstractTableModel):
    def __init__(self, event_list):
        QtCore.QAbstractTableModel.__init__(self)
        self._event_list = event_list

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._event_list)

    def columnCount(self, index):
        return 3

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if QtCore.Qt.DisplayRole == role:
            return self._event_list[index.row()][index.column() + 1]
        else:
            return None

class ThreadsModel:
    def __init__(self, strm):
        source = ThreadSource(strm)
        self._source = ThreadIndexSource(source)
        self._thread_list = ThreadsListSink(source).next()
        self._time_range = TimeRangeSink(self._source).next()
        self._global_wait_times = WaitSink(
            EventFilter(self._source),
            self._thread_list,
            self.start(),
            self.end()
        ).next()

    def close(self):
        self._source.close()

    def events(self, start_time, duration, thread_list=None):
        thread_list = thread_list if thread_list else self._thread_list
        return EventSink(EventFilter(self._source), thread_list, start_time, start_time + duration).next()

    def stats(self, start_time, duration, thread_id):
        if start_time == self.start() and duration == (self.end() - self.start()):
            return self._global_wait_times[thread_id]
        else:
            return WaitSink(
                EventFilter(self._source),
                [thread_id],
                start_time,
                start_time + duration
            ).next()[thread_id]

    def threadListModel(self):
        return _threadListModel(self._thread_list)

    def threadEventModel(self, start_time, duration, thread_id):
        event_list = EventSink(EventFilter(self._source), [thread_id], start_time, start_time + duration).next()[0][1]
        # remove gui/start events
        if event_list[0][3] == 'GUI/START':
            event_list = event_list[1:]
        if event_list[-1][3] == 'GUI/END':
            event_list = event_list[:-1]
        return _eventTableView(event_list)

    def start(self):
        return self._time_range[0]

    def end(self):
        return self._time_range[1]
