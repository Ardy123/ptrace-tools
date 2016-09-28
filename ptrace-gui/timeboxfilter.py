from eventfilter import EventFilter


class TimeboxFilter:

    def __init__(self, source, end_time):
        self._source = source
        self._iter = iter(source)
        self._end_time = end_time

    def __iter__(self):
        return self

    def next(self):
        event = self._iter.next()
        if event[2] <= self._end_time:
            return event
        else:
            raise StopIteration

    def close(self):
        self._source.close()

    def source(self):
        return self._source

# Test Cases
if __name__ == "__main__":
    from threadsource import *
    from threadindexsource import *
    event_str = ["START_TAG", "END_TAG", "MARK_TAG", "UNKNOWN_TAG"]
    pretty_evt = lambda evt_type, tid, time, evt: (event_str[evt_type], tid, time, evt)
    tf = TimeboxFilter(EventFilter(ThreadIndexSource(ThreadSource(open('../samples/ptrace.log', 'r')))), 26325119L)
    itr = iter(tf)
    print "[Iterator Tests]"
    for evt in tf:
        print pretty_evt(*evt)
    tf.close()