from threadrecord import *

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

    
    def __init__(self):
        self._threadTbl = {}

    def addEvent(self, tid, event, time):
        # add tid if it does not exist
        if tid not in self._threadTbl:
            self._threadTbl[tid] = ThreadRecord(tid, str(tid))
        # convert time string to a usec value
        uSec = self._calcUSec(time)
        # update thread with record
        if event in EventFilter._startEventTbl:   
            self._threadTbl[tid].addEvent("START", uSec, event)
        if event in EventFilter._endEventTbl:
            self._threadTbl[tid].addEvent("END", uSec, event)

    def threadList(self):
        return [thr[1] for thr in self._threadTbl.iteritems()]
        
    def _calcUSec(self, time):
        sec_usec = time.split(':')
        return (long(sec_usec[0]) * 1000000000L) + long(sec_usec[1])
            
    
