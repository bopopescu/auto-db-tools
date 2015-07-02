#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-06-18

@author: mizhon
'''
import os
import json

from Utility import util
from Utility.util import SysbenchUtility as su
from common import CommonActions
from Logs import logger
log = logger.Log()


class SysbenchActions(object):
    
    @classmethod
    def sa_get_cmds(cls, cmd_action):
        try:
            cmds = None
            if cmd_action == 'prepare':
                cmds = CommonActions.__coma_combine_cmds(util.NOHUP_PREFIX,
                                                         util.SYSBENCH,
                                                         (su.LUA_SCRIPT + CommonActions.lua),
                                                         (su.MYSQL_HOST + CommonActions.host),
                                                         (su.MYSQL_DB + CommonActions.db),
                                                         (su.MYSQL_USER + CommonActions.user),
                                                         (su.MYSQL_PASSWORD + CommonActions.password),
                                                         (su.MYSQL_PORT + CommonActions.port),
                                                         (su.OLTP_TABLES_COUNT + CommonActions.tables_count),
                                                         (su.OLTP_TABLE_SIZE + CommonActions.table_size),
                                                         cmd_action)
            
            elif cmd_action == 'run':
                cmds = CommonActions.__coma_combine_cmds(util.NOHUP_PREFIX,
                                                         util.SYSBENCH,
                                                         (su.LUA_SCRIPT + CommonActions.lua),
                                                         (su.MYSQL_HOST + CommonActions.host),
                                                         (su.MYSQL_DB + CommonActions.db),
                                                         (su.MYSQL_USER + CommonActions.user),
                                                         (su.MYSQL_PASSWORD + CommonActions.password),
                                                         (su.MYSQL_PORT + CommonActions.port),
                                                         (su.MAX_TIME + CommonActions.max_time),
                                                         (su.MAX_REQUESTS + CommonActions.max_requests),
                                                         (su.NUM_THREADS + CommonActions.threads),
                                                         (su.OLTP_TEST_MODE + CommonActions.test_mode),
                                                         (su.REPORT_INTERVAL + CommonActions.interval),
                                                         (su.MYSQL_TABLE_ENGINE + CommonActions.table_engine),
                                                         (su.MYSQL_ENGINE_TRX + CommonActions.engine_trx),
                                                         (su.PERCENTILE + CommonActions.percentile),
                                                         cmd_action)
            
            elif cmd_action == 'cleanup':
                cmds = CommonActions.__coma_combine_cmds(util.NOHUP_PREFIX,
                                                         util.SYSBENCH,
                                                         (su.LUA_SCRIPT + CommonActions.lua),
                                                         (su.MYSQL_HOST + CommonActions.host),
                                                         (su.MYSQL_DB + CommonActions.db),
                                                         (su.MYSQL_USER + CommonActions.user),
                                                         (su.MYSQL_PASSWORD + CommonActions.password),
                                                         (su.MYSQL_PORT + CommonActions.port),
                                                         cmd_action)
            
            return cmds
        except Exception as e:
            log.error(e)

    @classmethod
    def sa_save_results(cls, result):
        sb_json_result = SysbenchActions.__sa_get_json_results(result)
        
        "Abstract and save results in JSON format"
        json_file = CommonActions.ca_create_file_with_timestamp("json")
        json_file_path = os.path.join(CommonActions.RESULT_FOLDER, json_file)
        
        jf = open(json_file_path, 'w')
        jf.write(json.dumps(sb_json_result))
        jf.close()
        
    @classmethod
    def __sa_get_json_results(cls, sb_str):
        try:
            result = {
                        "status": 1,
                        "metrics": [],
                        "extra_data": {}
                     }
            tps_dict = {}
            qps_dict = {}
            rt_dict  = {}
            
            #extra_dict = CommonActions.ca
        
        except Exception as e:
            log.error(e)  
            
    @classmethod
    def sa_get_scenario_info(cls):
        pass
    

