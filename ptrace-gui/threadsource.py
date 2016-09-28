import mmap
import re
import functools

class ThreadSource:
    
    def __init__(self, strm):
        self._strm = strm
        self._memmap = mmap.mmap(strm.fileno(), 0, prot=mmap.PROT_READ)
        self.find = self._memmap.find
        self.rfind = self._memmap.rfind

    def __iter__(self):
        return self.findIter('\n')

    def __len__(self):
        return self._memmap.size()

    def __getitem__(self, index):
        return self._memmap[index]

    def regexIter(self, pattern):
        return re.finditer(pattern, self._memmap)

    def findIter(self, pattern):
        return self._findGenerator(pattern)

    def find(self, pattern, start, end):
        return self._

    def close(self):
        self._memmap.close()
        self._strm.close()

    def _findGenerator(self, pattern):
        pattern_len = len(pattern)
        loc = self._memmap.find(pattern, 0)
        while loc != -1:
            yield loc
            loc = self._memmap.find(pattern, loc + pattern_len)


