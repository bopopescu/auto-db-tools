#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-06-19

@author: mizhon
'''
#from common import CommonActions
from Logs import logger
log = logger.Log()

class TpccmysqlActions(object):
    
    @classmethod
    def ta_get_cmds(cls, cmd_action):
        try:
            cmds = None
            if cmd_action == 'prepare':
                pass
            
            elif cmd_action == 'run':
                pass
            
            elif cmd_action == 'cleanup':
                pass
            
            return cmds
        except Exception as e:
            log.error(e)
    
    @classmethod
    def ta_save_results(cls, result):
        pass

    @classmethod
    def ta_get_scenario_info(cls):
        pass
    
    