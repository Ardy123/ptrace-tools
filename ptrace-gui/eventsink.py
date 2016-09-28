from timeboxfilter import *
from util import safe_next

class EventSink:
    def __init__(self, source, thread_list, start_time, end_time):
        self._iter = TimeboxFilter(source.seek(start_time), end_time)
        self._thread_list = thread_list
        self._start_time = start_time
        self._end_time = end_time

    def __iter__(self):
        return self

    def next(self):
        # build list of events within time window
        thread_cache = {tid: [] for tid in self._thread_list}
        for event in self._iter:
            if thread_cache.has_key(event[1]):
                thread_cache[event[1]].append(event)
        # account for events that happen outside of time window
        for thrd, events in thread_cache.items():
            if not len(events):
                # account then the thread events are outside the bounds of the time window
                source = self._iter.source().source()
                prev_evt = safe_next(EventFilter(source, source.rfind(str(thrd), self._iter._iter._iter)))
                if prev_evt and EventFilter.END_TAG != prev_evt[0]:
                    events.insert(0, (EventFilter.START_TAG, thrd, self._start_time, 'GUI/START'))
                    events.insert(1, (EventFilter.END_TAG, thrd, self._end_time, 'GUI/END'))
            elif len(events) and EventFilter.END_TAG == events[0][0]:
                # account when the first thread event is an end event
                events.insert(0, (EventFilter.START_TAG, thrd, self._start_time, 'GUI/START'))
        return [(x, y) for x, y in thread_cache.items()]




# Test Cases
if __name__ == "__main__":
    from threadsource import *
    from threadindexsource import *
    event_str = ["START_TAG", "END_TAG", "MARK_TAG", "UNKNOWN_TAG"]
    pretty_evt = lambda evt_type, tid, time, evt: (event_str[evt_type], tid, time, evt)
    ef = EventFilter(ThreadIndexSource(ThreadSource(open('../samples/ptrace.log', 'r'))))
    print '[thread event test]'
    thread_events = EventSink(ef, [7239, 7240, 7241], 29129905L, 29191549L).next()
    for thrd_id, evt_list in thread_events:
        print "[thread(%d)]" % (thrd_id)
        for events in evt_list:
            print "\t", pretty_evt(*events)