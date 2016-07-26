class ThreadRecord:

    def __init__(self, evt_time):
        self._startEventTime = self._lastEventTime = evt_time   
        self._totalWaitTime = 0L
        self._maxWaitTime = 0L
        self._numberOfWaits = 0L
        self._lastEndEventTime = 0L

    def addStartEvent(self, evt_time):
        self._lastEventTime  = evt_time
        if self._lastEndEventTime:
            wait_time = (evt_time - self._lastEndEventTime)
            self._totalWaitTime += wait_time
            self._numberOfWaits += 1
            self._maxWaitTime = max(wait_time, self._maxWaitTime)
            self._lastEndEventTime ^= self._lastEndEventTime
        return self

    def addEndEvent(self, evt_time):        
        self._lastEventTime  = evt_time
        if not self._lastEndEventTime:
            self._lastEndEventTime = evt_time
        return self
                

    @staticmethod
    def construct(_, evt_time):
        return ThreadRecord(evt_time)

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


