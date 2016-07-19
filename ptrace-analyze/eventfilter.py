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
        self._iter = source.iter()

    def __iter__(self):
        return self
    
    def next(self):
        while True:
            line = self._iter.next()
            event = self._filterEvent(*line.split())
            if event:
                return event

    def close(self):
        self._source.close()
        
    def _filterEvent(self, event, tid, time):
        # convert time string to a usec value
        uSec = self._calcUSec(time)
        # update thread with record
        if event in EventFilter._startEventTbl:   
            return (EventFilter.START_TAG, tid, uSec, event)
        if event in EventFilter._endEventTbl:
            return (EventFilter.END_TAG, tid, uSec, event)

    def _calcUSec(self, time):
        sec_usec = map(long, time.split(':'))
        return (sec_usec[0] * 1000000000L) + sec_usec[1]
            
    
