class EventFilter:
    START_TAG = 0
    END_TAG = 1
    _eventTbl = {
        'PROCESS_START' : 0,  
        'PTHREAD_START' : 0, 
        'PTHREAD_MUTEX_LOCK_LEAVE' : 0, 
        'PTHREAD_COND_WAIT_LEAVE' : 0,
        'PTHREAD_COND_WAIT_TIMEOUT': 0,
        'PROCESS_END' : 1,
        'PTHREAD_END' : 1,
        'PTHREAD_MUTEX_LOCK_ENTER' : 1,
        'PTHREAD_COND_WAIT_ENTER' : 1}
    
    def __init__(self, source):
        self._source = source
        self._iter = source.iter(EventFilter._eventTbl.keys())
        
    def __iter__(self):
        return self
    
    def next(self):
        event = self._filterEvent(*self._iter.next().split())
        return event

    def close(self):
        self._source.close()
        
    def _filterEvent(self, event, tid, time):
        return (EventFilter._eventTbl[event], tid, EventFilter._calcUSec(time), event)

    @staticmethod
    def _calcUSec(time):
        sec_usec = map(long, time.split(':'))
        return (sec_usec[0] * 1000000000L) + sec_usec[1]
            
    
