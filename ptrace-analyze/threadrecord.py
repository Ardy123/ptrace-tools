class ThreadRecord:

    def __init__(self, thread_id, thread_name):
        self._id = thread_id
        self._name = thread_name
        self._startEventTime = None
        self._lastEventTime = None
        self._totalWaitTime = 0
        self._maxWaitTime = 0
        self._numberOfWaits = 0
        self._lastEndEvent = None
        self._lastStartEvent = None
        
    def addEvent(self, evt_type, evt_time, event):
        self._startEventTime = evt_time if not self._startEventTime else self._startEventTime
        self._lastEventTime = evt_time
        if not self._lastEndEvent:
            if "END" == evt_type:
                self._lastEndEvent = (evt_type, evt_time, event)
        else:
            if "START" == evt_type:
                self._lastStartEvent = (evt_type, evt_time, event)
                wait_time = (self._lastStartEvent[1] - self._lastEndEvent[1])
                self._totalWaitTime += wait_time
                self._numberOfWaits += 1
                self._maxWaitTime = wait_time if wait_time > self._maxWaitTime else self._maxWaitTime
                self._lastEndEvent = None
                self._lastStartEvent = None        

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
        return (self._totalWaitTime / self._numberOfWaits) if self._numberOfWaits > 0 else 0

    def maxWaitTime(self):
        return self._maxWaitTime

    def percentWaitTime(self):
        return float(self._totalWaitTime * 100.0) / float(self.runTime())

    def totalWaitTime(self):
        return self._totalWaitTime


