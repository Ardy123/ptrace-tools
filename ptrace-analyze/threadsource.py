import mmap
import os
import re

class ThreadSource:
    class _ForwardIterator:
        def __init__(self, src):
            self._src = src
        
        def __iter__(self):
            return self;
        
        def next(self):
            line = self._src.readNextLine()
            if line:
                return line
            else:
                raise StopIteration()

    class _ForwardPatternIterator:
        def __init__(self, src, event_list):
            self._src = src
            self._iter = re.finditer('.*|'.join(event_list) + '.*', src._memmap)

        def __iter__(self):
            return self

        def next(self):
            return self._iter.next().group(0)
                                     
    class _ReverseIterator:
        def __init__(self, src):
            self._src = src

        def __iter__(self):
            return self
        
        def next(self):
            line = self._src.readPrevLine()
            if line:
                return line
            else:
                raise StopIteration()

    def __init__(self, strm):
        self._memmap = mmap.mmap(strm.fileno(), 0, prot=mmap.PROT_READ)

    def __iter__(self):
        return ThreadSource._ForwardIterator(self)

    def iter(self, event_list = None):
        if event_list:
            return ThreadSource._ForwardPatternIterator(self, event_list)
        else:
            return ThreadSource._ForwardIterator(self)
    
    def reverseIter(self):
        return ThreadSource._ReverseIterator(self)

    def close(self):
        self._memmap.close()

    def readNextLine(self):
        return self._memmap.readline()

    def readPrevLine(self):
        prev_line_end = self._memmap.rfind('\n', 0, self._memmap.tell())
        if prev_line_end > -1:
            prev_line_start = self._memmap.rfind('\n', 0, prev_line_end)
            self._memmap.seek(prev_line_start + 1, os.SEEK_SET)
            return self._memmap[prev_line_start + 1: prev_line_end + 1]
        else:
            return ''
