from eventfilter import EventFilter


class TimeRangeSink:

    def __init__(self, source):
        self._source = EventFilter(source)

    def __iter__(self):
        return self

    def next(self):
        return self._source[0][2], self._source[-1][2]

    def close(self):
        self._source.close()
