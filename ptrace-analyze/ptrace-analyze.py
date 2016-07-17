#!/usr/bin/python

import sys
from eventfilter import *

def reportProcInfo(threads_list):
    totalns = max([thr.lastTime() for thr in threads_list]) - min([thr.startTime() for thr in threads_list])
    totalSec = float(totalns) / float(1000000000)
    print 'Process execution time: %.04f seconds' % (totalSec)
    print 'Number of threads: %d' % (len(threads_list))


def reportThreadInfo(threads_list):
    for thr in threads_list:
        tid = thr.id()
        total_uSec = thr.runTime()
        avg_wait_time = thr.averageWaitTime()
        max_wait_time = thr.maxWaitTime()
        prc_wait_time = thr.percentWaitTime()
        total_wait_time = thr.totalWaitTime()
        print '---- Thread Stats for Thread ID: %s ----' % (tid)
        print 'Total run time of thread: %dns' % (total_uSec)
        print 'Average wait time: %dns' % (avg_wait_time)
        print 'Max wait time: %dns' % (max_wait_time)
        print 'Thread waited %d percent of run time' % (prc_wait_time)
        print 'Total thread wait time: %dns' % (total_wait_time)
        print ''

def streamFile(strm):
    evt_fltr = EventFilter()
    for line in strm:
        record = line.strip("\n").split(" ")
        evt_fltr.addEvent(record[1], record[0], record[2])
    return evt_fltr.threadList()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        threads_file = open(sys.argv[1], mode="r")
        threads_list = streamFile(threads_file)
        threads_file.close()
        print '--- process information ---'
        reportProcInfo(threads_list)
        print ''
        reportThreadInfo(threads_list)
        print ''
    else:
        print 'ptrace-analyze (c)2012 Ardavon Falls'
        print 'usage...'
        print 'ptrace-analyze <log file>'

        
