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
        evt = self._iter.next().split()
        sec_usec = evt[2].split(':')
        sec_usec = (long(sec_usec[0]) * 1000000000L) + long(sec_usec[1])        
        return (EventFilter._eventTbl[evt[0]], evt[1], sec_usec)

    def close(self):
        self._source.close()
