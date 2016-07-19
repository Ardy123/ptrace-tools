from threadrecord import *

class ThreadStatsSink:

    def __init__(self, source):
        self._source = source
        self._threaddb = {}

    def __iter__(self):
        return self
        
    def next(self):
        for evt in self._source:
            evt_type = evt[0]
            evt_thid = int(evt[1])
            evt_name = evt[1]
            evt_time = evt[2]
            evt_event= evt[3]
            if evt_thid not in self._threaddb:
                self._threaddb[evt_thid] = ThreadRecord(evt_thid, evt_name)
            self._threaddb[evt_thid].addEvent(evt_type, evt_time, evt_event)    
        return [i[1] for i in self._threaddb.iteritems()]

    def close(self):
        self._source.close()

    
