import array
import bisect


class ThreadIndexSource:
    class _IndexSink:
        def __init__(self, src):
            self._itr = self._line_start_generator(src)
            
        def __iter__(self):
            return self

        def next(self):
            return array.array('L', self._itr)

        @staticmethod
        def _line_start_generator(src):
            yield 0
            loc = src.find('\n', 0)
            while loc != -1:
                yield loc + 1
                loc = src.find('\n', loc + 1)

    class _ForwardIterator:
        def __init__(self, src):
            self._src = src
            self._pos = 0

        def __iter__(self):
            return self

        def next(self):
            pos = self._pos
            if 0 <= pos < len(self._src):
                self._pos += 1
                return self._src[pos]
            else:
                raise StopIteration()

        def seek(self, pos):
            self._pos = pos
            return self

    class _ReverseIterator:
        def __init__(self, src):
            self._src = src
            self._pos = len(self._src) - 1

        def __iter__(self):
            return self

        def __reversed__(self):
            return self
            
        def next(self):
            pos = self._pos
            if 0 <= pos < len(self._src):
                self._pos -= 1
                return self._src[pos]
            else:
                raise StopIteration()
            
        def seek(self, pos):
            self._pos = pos
            return self
            
            
    def __init__(self, source):
        self._source = source
        self._index = ThreadIndexSource._IndexSink(source).next()
            
    def __iter__(self):
        return ThreadIndexSource._ForwardIterator(self)

    def __reversed__(self):
        return ThreadIndexSource._ReverseIterator(self)

    def __len__(self):
        return len(self._index) - 1

    def __getitem__(self, pos):
        index = self._index
        if pos < 0: pos -= 1
        return self._source[index[pos]:index[pos + 1] - 1]
   
    def close(self):
        self._source.close()
        
    def size(self):
        return len(self._source)

    def source(self):
        return self._source

    def find(self, pattern, start=None):
        if None == start: start = iter(self)
        pos = self._source.find(pattern, self._index[start._pos])
        guess_loc = bisect.bisect_right(self._index, pos, 0) - 1
        return start.seek(guess_loc)

    def rfind(self, pattern, start=None):
        if None == start: start = reversed(self)
        pos = self._source.rfind(pattern, 0, self._index[start._pos + 1])
        guess_loc = bisect.bisect_right(self._index, pos, 0) - 1
        return start.seek(guess_loc)


# Test Cases
if __name__ == "__main__":
    from threadsource import *
    ts = ThreadIndexSource(ThreadSource(open('../samples/ptrace.log', 'r')))
    #ts = ThreadIndexSource(ThreadSource(open('../../task-dispatch/tests/ptrace.log', 'r')))
    itr = iter(ts)
    rItr = reversed(ts)
    print "[Index Tests]"
    print '1:' + ts[0]
    print '2:' + ts[1]
    print '-1:' + ts[-1]
    print '-2:' + ts[-2]
    print "len(...): " + str(len(ts))
    print "[Iterator Tests]"
    print itr.next()
    print itr.next()
    print itr.next()
    print rItr.next()
    print rItr.next()
    print rItr.next()
    itr.seek(len(ts) - 1)
    print itr.next()
    itr.seek(0)
    print itr.next()
    print "[Find Tests]"
    print ts.find("PROCESS_START").next()
    print ts.find("7239 0:114640").next()
    print ts.find("PTHREAD_MUTEX_LOCK_ENTER 7239").next()
    print ts.find("7239 0:25962973").next()
    print ts.find("PROCESS_END").next()
    print ts.find("5:726101942").next()
    print "[Reverse Find Tests]"
    print ts.rfind("PROCESS_START").next()
    print ts.rfind("7239 0:114640").next()
    print ts.rfind("PTHREAD_END 7241").next()
    print ts.rfind("7241 5:725983524").next()
    print ts.rfind("PROCESS_END").next()
    print ts.rfind("5:726101942").next()
    ts.close()

