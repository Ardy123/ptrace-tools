from threadrecord import *

class ThreadStatsSink:

    def __init__(self, source):
        self._source = source

    def __iter__(self):
        return self
        
    def next(self):
        threadTbl = {}
        for evt in self._source:
            evt_thid = int(evt[1])
            if evt_thid not in threadTbl:
                threadTbl[evt_thid] = ThreadRecord(evt_thid, evt[1], evt[2])
            threadTbl[evt_thid].addEvent(evt[0], evt[2])    
        return threadTbl.values()

    def close(self):
        self._source.close()

    
