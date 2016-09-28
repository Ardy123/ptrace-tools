from timeboxfilter import *


class WaitSink:
    def __init__(self, source, thread_list, start_time, end_time):
        self._iter = TimeboxFilter(source.seek(start_time), end_time)
        self._thread_list = thread_list
        self._start_time = start_time
        self._end_time = end_time

    def __iter__(self):
        return self

    def next(self):
        # (<last end event time>, <total_wait_time>, <start_time>, <end_time>)
        thread_cache = { tid: [0, 0, 0, 0] for tid in self._thread_list }
        for evt_type, evt_id, evt_time, evt_string in self._iter:
            # add accumulated wait time
            if evt_id in thread_cache:
                if evt_type == EventFilter.START_TAG and thread_cache[evt_id][0]:
                    thread_cache[evt_id][1] += evt_time - thread_cache[evt_id][0]
                    thread_cache[evt_id][0] = 0
                elif evt_type == EventFilter.END_TAG and not thread_cache[evt_id][0]:
                    thread_cache[evt_id][0] = evt_time
                # add accumulated time
                if 0 == thread_cache[evt_id][2]:
                    thread_cache[evt_id][2] = evt_time
                thread_cache[evt_id][3] = evt_time
        return {x : (float(y[1] * 100.0) / (float(y[3] - y[2]) + .01), y[1]) for x, y in thread_cache.items()}

if __name__ == "__main__":
    from threadsource import *
    from threadindexsource import *
    from eventfilter import *
    from util import calcNanoSec
    ef = EventFilter(ThreadIndexSource(ThreadSource(open('../samples/ptrace.log', 'r'))))
    print '[thread percent test]'
    thread_wait_times = WaitSink(ef, [7239, 7240, 7241], 114640L, calcNanoSec("5:726101942")).next()
    for thrd_id, (percent_wait, total_wait) in thread_wait_times.items():
        print "thread(%d): wait: %f total wait: %d" % (thrd_id, percent_wait, total_wait)
