class EventFilter:

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

    def __iter__(self):
        return self
    
    def next(self):
        line = self._source.iter().next()
        # print "eventfilter:" + line[:-1]
        record = line.strip("\n").split(" ")
        event = self._filterEvent(record[1], record[2], record[0])
        if not event:
            return self.next()
        return event

    def close(self):
        self._source.close()
        
    def _filterEvent(self, tid, time, event):
        # convert time string to a usec value
        uSec = self._calcUSec(time)
        # update thread with record
        if event in EventFilter._startEventTbl:   
            return ("START", tid, uSec, event)
        if event in EventFilter._endEventTbl:
            return ("END", tid, uSec, event)

    def _calcUSec(self, time):
        sec_usec = time.split(':')
        return (long(sec_usec[0]) * 1000000000L) + long(sec_usec[1])
            
    
