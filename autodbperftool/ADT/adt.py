#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on 2015-07-02

@author: mizhon
'''

import os
import time
import subprocess

from ADT.common import CommonActions
from Utility import util

from Logs import logger

log = logger.Log()

def main():
    try:
        console_args = CommonActions.ca_receive_console_args()  
        args_tpl = CommonActions.ca_get_console_args(console_args)
        
        action = args_tpl[0]
        cfg_file_list = args_tpl[1]
        
        if os.path.exists(util.RESULT_FOLDER):
            pass
        else:
            p = subprocess.Popen(["mkdir", "-p", util.RESULT_FOLDER])
            p.wait()
        
        for cfg_file in cfg_file_list:
            cmd_list = CommonActions.ca_get_cmds_list(action, cfg_file) 
            print "CMD_LIST:", cmd_list
            
            for cmd in cmd_list:
                log.info(cmd)
                result = CommonActions.ca_exec_cmds(cmd)
                print result
                
                if CommonActions.tool == util.SYSBENCH:
                    #SysbenchActions.sa_save_results(result)
                    pass
                elif CommonActions.tool == util.TPCCMYSQL:
                    #TpccmysqlActions.ta_save_results(result)
                    pass
                
                'If more than one commands, sleep between each execution'
                if len(cmd_list) > 1:
                    time.sleep(util.SLEEP_TIME)

        exit(0)
        
    except Exception as e:
        log.error(e)

