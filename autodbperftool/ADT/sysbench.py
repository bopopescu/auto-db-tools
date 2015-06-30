#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-06-18

@author: mizhon
'''

#from Utility.util import SysbenchUtility
from Logs import logger
log = logger.Log()


class SysbenchActions(object):
    
    @classmethod
    def sa_get_cmds(cls, cmd_action):
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
    def sa_get_scenario_info(cls):
        pass

