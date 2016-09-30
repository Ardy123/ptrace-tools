import mmap
import re
import functools

class ThreadSource:
    
    def __init__(self, strm):
        self._strm = strm
        self._memmap = mmap.mmap(strm.fileno(), 0, prot=mmap.PROT_READ)
        # setup methods
        self.find = self._memmap.find
        self.rfind = self._memmap.rfind
        self.__getitem__ = self._memmap.__getitem__
        self.__len__ = self._memmap.size

    def __iter__(self):
        return self.findIter('\n')

    def regexIter(self, pattern):
        return re.finditer(pattern, self._memmap)

    def findIter(self, pattern):
        return self._findGenerator(pattern)

    def close(self):
        self._memmap.close()
        self._strm.close()

    def _findGenerator(self, pattern):
        pattern_len = len(pattern)
        loc = self._memmap.find(pattern, 0)
        while loc != -1:
            yield loc
            loc = self._memmap.find(pattern, loc + pattern_len)


