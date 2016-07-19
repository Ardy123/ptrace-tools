class EventFilter:
    START_TAG = 0
    END_TAG = 1
    
    _startEventTbl = [
        'PROCESS_START', 
        'PTHREAD_START', 
        'PTHREAD_MUTEX_LOCK_LEAVE', 
        'PTHREAD_COND_WAIT_LEAVE',
        'PTHREAD_COND_WAIT_TIMEOUT']
    _endEventTbl = [
        'PROCESS_END',
        'PTHREAD_END',
        'PTHREAD_MUTEX_LOCK_ENTER',
        'PTHREAD_COND_WAIT_ENTER']
    
    def __init__(self, source):
        self._source = source
        self._iter = source.iter(EventFilter._startEventTbl + EventFilter._endEventTbl)
        self._eventTbl = dict(
            [(i, EventFilter.START_TAG) for i in EventFilter._startEventTbl] +
            [(j, EventFilter.END_TAG) for j in EventFilter._endEventTbl])
        
    def __iter__(self):
        return self
    
    def next(self):
        line = self._iter.next()
        event = self._filterEvent(*line.split())
        return event

    def close(self):
        self._source.close()
        
    def _filterEvent(self, event, tid, time):
        return (self._eventTbl[event], tid, EventFilter._calcUSec(time), event)

    @staticmethod
    def _calcUSec(time):
        sec_usec = map(long, time.split(':'))
        return (sec_usec[0] * 1000000000L) + sec_usec[1]
            
    
