from PySide import QtGui, QtCore
from eventfilter import *


class PieChartView(QtGui.QWidget):
    Settings = {
        'colors': {
            'run'  : (QtGui.QColor('green'), QtGui.QColor('black')),
            'sleep': (QtGui.QColor('red'), QtGui.QColor('black')),
        },
        'margins' : {
          'left'  : 10,
          'top'   : 10,
          'right' : 10,
          'bottom': 10
        },
    }
    PIE_HEIGHT_SKEW = 0.4

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self._model = None

    # the model is (tid, percent wait time)
    def setModel(self, model):
        self._model = model

    def paintEvent(self, evt):
        if not self._model:
            return
        run_color_fill = self.Settings['colors']['run'][0]
        run_color_edge = self.Settings['colors']['run'][1]
        sleep_color_fill = self.Settings['colors']['sleep'][0]
        sleep_color_edge = self.Settings['colors']['sleep'][1]
        text_color = QtGui.QApplication.palette().text().color()
        qpaint = QtGui.QPainter(self)
        qpaint.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        qpaint.setRenderHint(QtGui.QPainter.Antialiasing, True)
        # draw 3d pie
        fillRng = self._calcPercentRange()
        run_gradient = self._createGradient(run_color_fill)
        sleep_gradient = self._createGradient(sleep_color_fill)
        for y in range(self._calcPieHeight(), 0, -1):
            qpaint.setBrush(QtGui.QBrush(sleep_gradient))
            qpaint.drawPie(self._calcRect(0,y), 0, fillRng[0])
            qpaint.setBrush(QtGui.QBrush(run_gradient))
            qpaint.drawPie(self._calcRect(0,y), fillRng[0], fillRng[1])
        qpaint.setBrush(QtCore.Qt.NoBrush)
        qpaint.setPen(QtGui.QPen(sleep_color_edge))
        qpaint.drawPie(self._calcRect(), 0, fillRng[0])
        qpaint.setPen(QtGui.QPen(run_color_edge))
        qpaint.drawPie(self._calcRect(),fillRng[0], fillRng[1])
        # draw stats
        qpaint.setPen(QtGui.QPen(text_color, 1))
        qpaint.drawText(
            self.Settings['margins']['left'],
            self.height() - self.Settings['margins']['bottom'],
            "utilization: %0.2f%s" % (self._percent(), "%"))
        # draw key
        font_mets = QtGui.QFontMetrics(qpaint.font())
        font_height = font_mets.height()
        qpaint.setBrush(run_color_fill)
        item1 = self._calcKeyRect(-((font_height * 2) + 5))
        item2 = self._calcKeyRect(-(font_height + 5))
        qpaint.drawRect(item1)
        qpaint.drawText(item1.x() + item1.width() + 3, item1.y() + 7, "percent running")
        qpaint.setBrush(sleep_color_fill)
        qpaint.drawRect(item2)
        qpaint.drawText(item2.x() + item2.width() + 3, item2.y() + 7, "percent blocked")
        qpaint.end()

    def heightForWidth(self, width):
        return width

    def _calcMarginRect(self):
        return QtCore.QRect(
            self.Settings['margins']['left'],
            self.Settings['margins']['top'],
            self.width() - (self.Settings['margins']['left'] + self.Settings['margins']['right']),
            self.height() - (self.Settings['margins']['top'] + self.Settings['margins']['bottom']),
        )

    def _calcRect(self, x_offset=0, y_offset=0):
        height_skew = self.PIE_HEIGHT_SKEW
        margin_height = self.height() - (self.Settings['margins']['top'] + self.Settings['margins']['bottom'])
        width = (self.width() - (self.Settings['margins']['left'] + self.Settings['margins']['right']))
        height = width * height_skew
        if height > margin_height:
            width = margin_height / height_skew
            height = margin_height
        return QtCore.QRect(
            self.Settings['margins']['left'] + x_offset,
            self.Settings['margins']['top'] + y_offset,
            width,
            height
        )

    def _calcPercentRange(self):
        rng = int((5760.0 * (100.0 - self._percent())) / 100.0)
        return (rng, 5760 - rng)

    def _calcPieHeight(self):
        height = int(self.width() * (self.PIE_HEIGHT_SKEW / 10.0))
        return min(height, 16)

    def _createGradient(self, baseColor):
        pie_rect = self._calcRect()
        x_margin = pie_rect.width() * 0.1
        y_margin = pie_rect.height() * 0.1
        x_start = pie_rect.x() + x_margin
        x_end = pie_rect.x() + (pie_rect.width() - x_margin)
        gradient = QtGui.QLinearGradient(x_start, y_margin, x_end, y_margin)
        gradient.setColorAt(0, baseColor.lighter(30))
        gradient.setColorAt(1, baseColor.lighter(120))
        return gradient

    def _calcKeyRect(self, y_offset=0):
        return QtCore.QRect(
            self.Settings['margins']['left'],
            (self.height() - self.Settings['margins']['bottom']) + y_offset,
            7,
            7
        )

    def _percent(self):
        return self._model[1]


if __name__ == "__main__":
    import sys
    model = (7239, 75.342)
    app = QtGui.QApplication(sys.argv)
    tlv = PieChartView()
    tlv.setModel(model)
    tlv.show()
    sys.exit(app.exec_())