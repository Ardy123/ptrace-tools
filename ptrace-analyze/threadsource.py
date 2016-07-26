import mmap
import os
import re

class ThreadSource:
    
    def __init__(self, strm):
        self._strm = strm
        self._memmap = mmap.mmap(strm.fileno(), 0, prot=mmap.PROT_READ)

    def __iter__(self):
        return self._findIter('\n')

    def __len__(self):
        return self._memmap.size()

    def __getitem__(self, index):
        return self._memmap[index]

    def regexIter(self, pattern):
        return re.finditer(pattern, self._memmap)

    def findIter(self, pattern):
        return iter(self._createIterator(pattern), -1)

    def close(self):
        self._memmap.close()
        self._strm.close()

    def _createFindIterator(self, pattern):
        patern_len = len(pattern)
        def iterator():
            iterator.loc = self._memmap,find(
                patern,
                iterator.loc + patern_len
            )        
            return iterator.loc
        iterator.loc = -patern_len
        return iterator

        
