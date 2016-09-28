import bisect
import collections
from util import calcNanoSec


class EventFilter:
    START_TAG, END_TAG, MARK_TAG, UNKNOWN_TAG = range(4)

    _eventTbl = collections.defaultdict(
        lambda: EventFilter.UNKNOWN_TAG,
        **{
            'PROCESS_START'             : START_TAG,
            'PTHREAD_START'             : START_TAG,
            'PTHREAD_MUTEX_LOCK_LEAVE'  : START_TAG,
            'PTHREAD_COND_WAIT_LEAVE'   : START_TAG,
            'PTHREAD_COND_WAIT_TIMEOUT' : START_TAG,
            'PROCESS_END'               : END_TAG,
            'PTHREAD_END'               : END_TAG,
            'PTHREAD_MUTEX_LOCK_ENTER'  : END_TAG,
            'PTHREAD_COND_WAIT_ENTER'   : END_TAG,
            'PTHREAD_CREATE'            : MARK_TAG,
            'PTHREAD_JOIN'              : MARK_TAG,
            'PTHRAD_CANCEL'             : MARK_TAG,
            'PTHREAD_MUTEX_UNLOCK'      : MARK_TAG,
            'PTHREAD_COND_SIGNAL'       : MARK_TAG,
            'PTHREAD_COND_BROADCAST'    : MARK_TAG
        }
    )

    class _BisectCmp:
        class _BisectCmpIndex:
            def __init__(self, usec=None, line=None):
                self._time = calcNanoSec(line.split()[2]) if line is not None else usec

            def __lt__(self, other):
                return self._time < other._time

            def __gt__(self, other):
                return self._time > other._time

            def __eq__(self, other):
                return self._time == other._time

        def __init__(self, index):
            self._index = index

        def __getitem__(self, index):
            return EventFilter._BisectCmp._BisectCmpIndex(line=self._index[index])

        def __len__(self):
            return len(self._index)

    def __init__(self, source, itr=None):
        self._source = source
        self._iter = itr if itr is not None else iter(source)

    def __iter__(self):
        return self

    def __reversed__(self):
        return EventFilter(self._source, reversed(self._source))

    def __len__(self):
        return len(self._source)

    def __getitem__(self, index):
        return EventFilter._filter_event(*self._source[index].split())

    def next(self):
        return EventFilter._filter_event(*self._iter.next().split())

    def seek(self, time):
        guess_loc = bisect.bisect_left(
            EventFilter._BisectCmp(self._source),
            EventFilter._BisectCmp._BisectCmpIndex(usec=time)
        )
        return EventFilter(self._source, self._iter.seek(guess_loc))

    def close(self):
        self._source.close()

    def source(self):
        return self._source

    @staticmethod
    def _filter_event(event, tid, time):
        return EventFilter._eventTbl[event], int(tid), calcNanoSec(time), event

# Test Cases
if __name__ == "__main__":
    from threadsource import *
    from threadindexsource import *
    event_str = ["START_TAG", "END_TAG", "MARK_TAG", "UNKNOWN_TAG"]
    pretty_evt = lambda evt_type, tid, time, evt: (event_str[evt_type], tid, time, evt)
    #ef = EventFilter(ThreadIndexSource(ThreadSource(open('../../task-dispatch/tests/ptrace.log', 'r'))))
    ef = EventFilter(ThreadIndexSource(ThreadSource(open('../samples/ptrace.log', 'r'))))
    itr = iter(ef)
    rItr = reversed(ef)
    print "[Index Test]"
    print pretty_evt(*ef[0])
    print pretty_evt(*ef[1])
    print pretty_evt(*ef[-1])
    print pretty_evt(*ef[-2])
    print pretty_evt(*ef[len(ef) / 2])
    print "len(...): " + str(len(ef))
    print "[Iterator Tests]"
    print pretty_evt(*itr.next())
    print pretty_evt(*itr.next())
    print pretty_evt(*itr.next())
    print pretty_evt(*rItr.next())
    print pretty_evt(*rItr.next())
    print pretty_evt(*rItr.next())
    print "[Seek Tests]"
    print pretty_evt(*ef.seek(ef[0][2]).next())
    print pretty_evt(*ef.seek(ef[-1][2]).next())
    print pretty_evt(*ef.seek(ef[len(ef) / 2][2]).next())
    print pretty_evt(*ef.seek(ef[len(ef) / 2][2] - (ef[len(ef) / 2][2] / 2)).next())
    print pretty_evt(*ef.seek(0).next())
    #print pretty_evt(*ef.seek(ef[-1][2] + 10).next())
    ef.close()