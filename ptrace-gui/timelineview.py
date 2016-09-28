from PySide import QtGui, QtCore
from eventfilter import *
from util import nano2MilSec


class TimelineView(QtGui.QWidget):
    NUM_GRIDMARKS = 10
    Settings = {
        'colors' : {
            'background' : QtGui.QColor(240,240,240),
            'grid_lines' : QtGui.QColor(150,150,150),
            # Format: Pen Color, Brush Color
            'threads' : [
                (QtGui.QColor('darkCyan'), QtGui.QColor('cyan')),
                (QtGui.QColor('darkGreen'), QtGui.QColor('green')),
                (QtGui.QColor('darkRed'), QtGui.QColor('red')),
                (QtGui.QColor('darkBlue'), QtGui.QColor('blue')),
                (QtGui.QColor('darkGray'), QtGui.QColor('gray')),
                (QtGui.QColor('darkMagenta'), QtGui.QColor('magenta'))
            ],
            'thread-background' : QtGui.QColor('lightGray')
        },
        'margins' : {
            'left' : 20,
            'top' : 20,
            'right' : 20,
            'bottom' : 20
        },
        'threads' : {
            'thickness' : 15,
            'spacing' : 15,
        }        
    }
    # The format of this event is (thread id, start time, end time)
    signal_thread_clicked = QtCore.Signal(int, long, long)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._model = None
        self._start_time = None
        self._end_time = None

    @QtCore.Slot('bool')
    def showEventsLabels(self, enable):
        self._show_events = enable
        self.repaint()

    # the model is [(tid, [events..]),...]
    def setModel(self, model, start_time, end_time):
        self._model = model
        self._start_time = start_time
        self._end_time = end_time

    def range(self):
        if self._model:
            return (self._start_time, self._end_time)
        else:
            return (0,0)

    def paintEvent(self, evt):
        qpaint = QtGui.QPainter(self)
        if self._model:
            self._drawBackground(qpaint)
            self._drawThreads(qpaint)
        qpaint.setClipRect(self.geometry())
        qpaint.end()

    def mouseReleaseEvent(self, evt):
        #figure out thread that was clicked
        display_rect = self._getDisplayRect()
        min_time, max_time = self.range()
        delta_Time = max_time - min_time
        thrd_height = self.Settings['threads']['thickness']
        thrd_spacing = self.Settings['threads']['spacing']
        y_iter = self._thread_y_generator(display_rect.top() + (thrd_spacing / 2), thrd_height + thrd_spacing)
        for thrd, _ in self._model:
            thrd_top = y_iter.next()
            if thrd_top <= evt.y() < (thrd_top + thrd_height) and \
                display_rect.left() <= evt.x() < display_rect.right():
                start_time = max(self._calcUSecFromX(evt.x() - .5, display_rect, min_time, delta_Time), min_time)
                end_time = min(self._calcUSecFromX(evt.x() + .5, display_rect, min_time, delta_Time), max_time)
                self.signal_thread_clicked.emit(thrd, start_time, end_time)
                return

    def _drawBackground(self, qpainter):        
        # draw background color
        background_color = self.Settings['colors']['background']
        qpainter.setBrush(QtGui.QBrush(background_color))
        qpainter.drawRect(0, 0, self.width(), self.height())
        # draw grid marks
        gridline_color = self.Settings['colors']['grid_lines']
        display_rect = self._getDisplayRect()
        start_time, end_time = self.range()
        delta_time = end_time - start_time
        num_gridlines = self.NUM_GRIDMARKS
        y_top = display_rect.top()
        y_bottom = display_rect.bottom()
        qpainter.setPen(QtGui.QPen(gridline_color))
        font_mets = QtGui.QFontMetrics(qpainter.font())
        font_height = font_mets.height()
        for t in range(start_time, end_time, delta_time / num_gridlines):
            time = self._convertNanoSecToMilliSec(t)
            x = self._calcXFromUSec(t, display_rect, start_time, delta_time)
            label_width = font_mets.width(time)
            qpainter.drawLine(x, y_top, x, y_bottom)
            qpainter.drawText(
                x - (label_width / 2),
                y_bottom + font_height,
                time
            )

    def _drawThreads(self, qpainter):
        # draw threads
        display_rect = self._getDisplayRect()
        start_time, end_time = self.range()
        delta_time = end_time - start_time
        thrd_height = self.Settings['threads']['thickness']
        thrd_spacing = self.Settings['threads']['spacing']
        display_rect = self._getDisplayRect()
        y_iter = self._thread_y_generator(display_rect.top() + (thrd_spacing / 2), thrd_height + thrd_spacing)
        thread_text_pen = QtGui.QPen(QtGui.QColor('black'))
        qpainter.setFont(QtGui.QFont('san-serif', 10))
        font_mets = QtGui.QFontMetrics(qpainter.font())
        font_height = font_mets.height()
        for thrd, events in self._model:
            thread_y = y_iter.next()
            thread_color = self._thread_color(self.Settings['colors']['threads'], thrd)
            thread_bk_brush = QtGui.QBrush(self.Settings['colors']['thread-background'], QtCore.Qt.Dense4Pattern)
            thread_fg_brush = QtGui.QBrush(thread_color[0])
            thread_hl_brush = QtGui.QBrush(thread_color[1], QtCore.Qt.Dense6Pattern)
            # draw background bar
            rect = QtCore.QRect(display_rect.x(), thread_y, display_rect.width(), thrd_height)
            qpainter.fillRect(rect, thread_bk_brush)
            # draw thread bars
            for evt_type, evt_tid, evt_time, evt_data in events:
                if evt_type == EventFilter.START_TAG:
                    start_x = self._calcXFromUSec(evt_time, display_rect, start_time, delta_time)
                elif evt_type == EventFilter.END_TAG:
                    rect = QtCore.QRect(
                        start_x,
                        thread_y,
                        self._calcXFromUSec(evt_time, display_rect, start_time, delta_time) - start_x,
                        thrd_height
                    )
                    qpainter.fillRect(rect, thread_fg_brush)
                    qpainter.fillRect(rect, thread_hl_brush)
            # draw thread id
            qpainter.setPen(thread_text_pen)
            x = self._calcXFromUSec(start_time, display_rect, start_time, delta_time)
            text_y = thread_y + (thrd_height + font_height) / 2
            qpainter.drawText(x, text_y, 'thread(%s)' %(thrd))

    def _getDisplayRect(self):
        width = self.width()
        height = self.height()
        mrg_left = self.Settings['margins']['left']
        mrg_top = self.Settings['margins']['top']
        return QtCore.QRect(
            mrg_left,
            mrg_top,
            width - (self.Settings['margins']['right'] + mrg_left),
            height - (self.Settings['margins']['bottom'] + mrg_top)
        )

    @staticmethod
    def _thread_y_generator(start_y, spacing):
        while 1:
            yield start_y
            start_y += spacing

    @staticmethod
    def _thread_color(color_lst, thread_id):
        return color_lst[thread_id % len(color_lst)]

    @staticmethod
    def _calcXFromUSec(usec, display_rect, start_time, delta_time):
        usecOffset = usec - start_time
        width = display_rect.width()
        return int(((usecOffset * width) / delta_time) + display_rect.left())

    @staticmethod
    def _calcUSecFromX(x, display_rect, start_time, delta_time):
        x_offset = x - display_rect.left()
        width = long(display_rect.width())
        return ((long(x_offset * delta_time)) / width) + start_time

    @staticmethod
    def _convertNanoSecToMilliSec(ns, fracSz=2):
        return '%.3f ms' % (nano2MilSec(ns))



if __name__ == "__main__":
    import sys
    model = [
        (7239, [
            (EventFilter.START_TAG, 7239, 114640, "PROCESS_START"),
            (EventFilter.END_TAG, 7239, 25962973, "PTHREAD_MUTEX_LOCK_ENTER"),
            (EventFilter.START_TAG, 7239, 25966578, "PTHREAD_MUTEX_LOCK_LEAVE"),
            (EventFilter.END_TAG, 7239, 26325117, "PTHREAD_MUTEX_LOCK_ENTER"),
            (EventFilter.START_TAG, 7239, 26326155, "PTHREAD_MUTEX_LOCK_LEAVE")]),
        (7240, [
            (EventFilter.START_TAG, 7240, 2590000, "PROCESS_START"),
            (EventFilter.END_TAG, 7240, 26326155, "PTHREAD_MUTEX_LOCK_ENTER")])
    ]
    app = QtGui.QApplication(sys.argv)
    tlv = TimelineView()
    tlv.setModel(model, 114640, 26326155)
    tlv.show()
    sys.exit(app.exec_())
