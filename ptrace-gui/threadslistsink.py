class ThreadsListSink:
    def __init__(self, source):
        self._source = source
        self._iter = source.regexIter('(PROCESS_START|PTHREAD_START) ([0-9]*)')
        
    def __iter__(self):
        return self._iter

    def next(self):
        return [int(t.group(2)) for t in self._iter]

    def close(self):
        self._source.close()        


# Test Cases
if __name__ == "__main__":
    from threadsource import *
    t_lst = ThreadsListSink(ThreadSource(open('../samples/ptrace.log', 'r'))).next()
    for i in t_lst:
        print i