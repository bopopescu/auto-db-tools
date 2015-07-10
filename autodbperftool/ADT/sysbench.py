#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-06-20

@author: mizhon
'''

class Sysbench(object):
    
    def __init__(self,
                 table_engine,
                 engine_trx,
                 test_mode,
                 table_count,
                 table_size,
                 max_time,
                 max_requests,
                 threads,
                 interval,
                 percentile,
                 lua):
        
        self.table_engine = table_engine
        self.engine_trx   = engine_trx
        self.test_mode    = test_mode
        self.table_count  = table_count
        self.tale_size    = table_size
        self.max_time     = max_time
        self.max_requests = max_requests
        self.threads      = threads
        self.interval     = interval
        self.percentile   = percentile
        self.lua          = lua
        
    