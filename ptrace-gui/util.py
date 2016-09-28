def calcNanoSec(time_str):
    sec_usec = time_str.split(':')
    return (long(sec_usec[0]) * 1000000000L) + long(sec_usec[1])


def nano2MilSec(ns):
    return int(ns / 1000000L)

def mil2NanoSec(ms):
    return long(ms) * 1000000L

def safe_next(itr, default=None):
    try:
        return itr.next()
    except StopIteration:
        return default
