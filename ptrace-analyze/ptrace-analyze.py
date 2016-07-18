#!/usr/bin/python

import sys
from threadsource import *
from eventfilter import *
from threadstatssink import *

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
    evt_sink = ThreadStatsSink(EventFilter(ThreadSource(strm)))
    thread_stats_list = evt_sink.next()
    evt_sink.close()
    return thread_stats_list

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
        print 'ptrace-analyze (c)2016 Ardavon Falls'
        print 'usage...'
        print 'ptrace-analyze <log file>'

        
