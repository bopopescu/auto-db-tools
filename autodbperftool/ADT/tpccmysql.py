#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-06-20

@author: mizhon
'''

class Tpccmysql(object):
    
    def __init__(self,
                 warehouse,
                 connection,
                 rampuptime,
                 measuretime,
                 intervaltime):
        
        self.warehouse    = warehouse
        self.connection   = connection
        self.rampuptime   = rampuptime
        self.measuretime  = measuretime
        self.intervaltime = intervaltime
        
    