from eventfilter import *

class ThreadRecord:

    def __init__(self, thread_id, thread_name, thread_time):
        self._id = thread_id
        self._name = thread_name
        self._startEventTime = thread_time
        self._lastEventTime = None
        self._totalWaitTime = 0
        self._maxWaitTime = 0
        self._numberOfWaits = 0
        self._lastEndEvent = None
        
    def addEvent(self, evt_type, evt_time):
        self._lastEventTime = evt_time
        if EventFilter.END_TAG == evt_type and not self._lastEndEvent:
            self._lastEndEvent = evt_time
        elif EventFilter.START_TAG == evt_type and self._lastEndEvent:
            wait_time = (evt_time - self._lastEndEvent)
            self._totalWaitTime += wait_time
            self._numberOfWaits += 1
            self._maxWaitTime = max(wait_time, self._maxWaitTime)
            self._lastEndEvent = None
          

    def name(self):
        return self._name

    def id(self):
        return self._id

    def startTime(self):
        return long(self._startEventTime)

    def lastTime(self):
        return long(self._lastEventTime)
    
    def runTime(self):
        return long(self._lastEventTime - self._startEventTime)

    def averageWaitTime(self):
        return self._totalWaitTime / max(self._numberOfWaits, 1)

    def maxWaitTime(self):
        return self._maxWaitTime

    def percentWaitTime(self):
        return float(self._totalWaitTime * 100.0) / float(self.runTime())

    def totalWaitTime(self):
        return self._totalWaitTime


