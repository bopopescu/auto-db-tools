#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-06-19

@author: mizhon
'''
from Logs import logger
log = logger.Log()

NOHUP_PREFIX = "nohup"

"""database performance tools"""
SYSBENCH = "sysbench"
TPCCMYSQL = "tpcc-mysql"

"""supported database names"""
DB_MYSQL  = "mysql"
DB_ORACLE = "oracle"
DB_REDIS  = "redis"
DB_MSSQL  = "mssql" # plan to support this

SLEEP_TIME = 60 # sleep time between each command execution

"""sysbench settings"""
class SysbenchUtility(object):
    LUA_SCRIPT = "--test="
    
    """DB info related fields"""
    MYSQL_HOST     = "--mysql-host="
    MYSQL_DB       = "--mysql-db="
    MYSQL_USER     = "--mysql-user="
    MYSQL_PASSWORD = "--mysql-password="
    MYSQL_PORT     = "--mysql-port="
    MYSQL_TABLE_ENGINE = "--mysql-table-engine="
    MYSQL_ENGINE_TRX   = "--mysql-engine-trx="
    DB_DRIVER          = "--db-driver="
    NUM_THREADS        = "--num-threads="
    
    OLTP_TABLES_COUNT  = '--oltp-tables-count='
    OLTP_TABLE_SIZE    = '--oltp-table-size='
    OLTP_TEST_MODE     = '--oltp-test-mode='
    MAX_TIME           = '--max-time='
    MAX_REQUESTS       = '--max-requests='
    
    REPORT_INTERVAL    = '--report-interval='
    PERCENTILE         = '--percentile='
    
    """LUA script"""
    LUA_OLTP           = 'oltp.lua'
    LUA_COMMON         = 'common.lua'
    LUA_INSERT         = 'insert.lua'
    LUA_DELETE         = 'delete.lua'
    LUA_SELECT         = 'select.lua'
    
    LUA_PARALLEL_PREPARE     = 'parallel_prepare.lua'
    LUA_SELECT_RANDOM_POINTS = 'select_random_points.lua'
    LUA_SELECT_RANDOM_RANGES = 'select_random_ranges.lua'
    LUA_UPDATE_INDEX         = 'update_index.lua'
    LUA_UPDATE_NON_INDEX     = 'update_non_index.lua'


"""tpcc-mysql settings"""
class TpccmysqlUtility(object):
    
    TPCC_LOAD      = 'tpcc_load'
    TPCC_START     = 'tpcc_start'
    
    TPCC_HOST      = '-h'
    TPCC_DB        = '-d'
    TPCC_USER      = '-u'
    TPCC_PASSWORD  = '-p'
    TPCC_WAREHOUSE = '-w'
    TPCC_THREADS   = '-c'
    TPCC_RAMPUP    = '-r'
    TPCC_LASTTIME  = '-l'
