from threadrecord import *


class ThreadStatsSink:
    _eventTbl = {
        'PROCESS_START' : ThreadRecord.construct,  
        'PTHREAD_START' : ThreadRecord.construct, 
        'PTHREAD_MUTEX_LOCK_LEAVE' : ThreadRecord.addStartEvent, 
        'PTHREAD_COND_WAIT_LEAVE' : ThreadRecord.addStartEvent,
        'PTHREAD_COND_WAIT_TIMEOUT' : ThreadRecord.addStartEvent,
        'PROCESS_END' : ThreadRecord.addEndEvent,
        'PTHREAD_END' : ThreadRecord.addEndEvent,
        'PTHREAD_MUTEX_LOCK_ENTER' : ThreadRecord.addEndEvent,
        'PTHREAD_COND_WAIT_ENTER' : ThreadRecord.addEndEvent
    }

    def __init__(self, source):
        self._source = source
        self._iter = source.regexIter(
            '(' + '|'.join(ThreadStatsSink._eventTbl.keys()) + ') (.*) (.*):(.*)'
        )        

    def __iter__(self):
        return self

    def next(self):
        threadTbl = {}        
        for line in self._iter:
            thread_id = int(line.group(2))
            usec = (long(line.group(3)) * 1000000000L) + long(line.group(4))
            threadTbl[thread_id] = ThreadStatsSink._eventTbl[line.group(1)](
                threadTbl.get(thread_id),
                usec
            )
        return threadTbl.items()

    def close(self):
        self._source.close()
    

