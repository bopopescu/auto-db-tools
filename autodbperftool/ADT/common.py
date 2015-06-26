'''
Created on 2015-06-20

@author: mizhon
'''
import os
import re
import time
import shlex
import argparse
import textwrap
import subprocess
import ConfigParser
from subprocess import PIPE

from Utility import util

from Logs import logger
log = logger.Log()


class CommonActions(object):
    
    tool          = None
    provider      = None
    
    'database info fields'
    host          = None
    db            = None
    port          = None
    user          = None
    password      = None
    instance_type = None # indicate whether the instance is RDS or database on VM host
    db_version    = None # database version, e.g.: mysql5.5, mysql5.6 ...
    db_setup      = None # including three types: 1.default; 2.high-safety (slave-master); 3.high-performance;
    long_stand    = None # indicate whether the test is long-stand testing, default is False 
    
    'sysbench params fields'
    table_engine  = None
    engine_trx    = None
    test_mode     = None
    tables_count  = None
    table_size    = None
    max_time      = None
    max_requests  = None
    threads       = None
    interval      = None
    percentile    = None
    lua           = None
    
    'tpcc-mysql params fields'
    warehouse     = None
    connection    = None
    rampuptime    = None
    measuretime   = None
    intervaltime  = None
    
    RESULT_FOLDER = "/tmp/AutoDBPerfTool/" # indicate the result save path on LINUX.
    
    @classmethod
    def ca_receive_console_args(cls):
        parser = argparse.ArgumentParser(prog="AutoDBPerfTool",
                                         formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description=textwrap.dedent('''
                                         =============================================================
                                         AutoDBPerfTool used to automate database performance testing.
                                         =============================================================
                                         
                                         command example:
                                         python auto_run.py -a <specified action> -c <config folder or file path>
                                         ''')
                                         )
        
        parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0.0")
        parser.add_argument("-a", "--action", help="specify execution type.")
        parser.add_argument("-c", "--config", help="specify config path.")
        
        args = parser.parse_args()
        return args
    
    @classmethod
    def ca_get_console_args(cls, console_args):
        try:
            dict_args = vars(console_args)
            
            action = None
            config_file_list = []
            
            for item in dict_args.item():
                if item[0] =='action':
                    if item[1] is not None:
                        if item[1] == 'prepare' or item[1] == 'run' or item[1] =='cleanup':
                            action = item[1]
                        else:
                            log.error("Invalid value detected for action: '%s', please choose action in 'prepare/run/cleanup'." % item[1])
                    else:
                        content_error = item[0]
                        log.error("No value detected for param: '%s', please input -h/--help for usage." % content_error)
                elif item[0] == 'config':
                    if item[1] is not None:
                        config = item[1]
                        if os.path.exists(config):
                            config_file_list = CommonActions._ca_get_config_file_list(config)
                        else:
                            content_error = item[1]
                            log.error("Invalid config file: '%s', please check the config file is exist." % item[1])
                    else:
                        content_error = item[0]
                        log.error("No value detected for param: '%s', please input -h/--help for usage." % content_error)
            
            return (action, config_file_list)
        except Exception as e:
            log.error(e)

    @classmethod
    def ca_parse_config_params(cls, cfg_file):
        try:
            config = ConfigParser.RawConfigParser()
            config.read(cfg_file)
            
            CommonActions.tool          = config.get("ToolInfo", "tool")
            CommonActions.provider      = config.get("ProviderInfo", "provider")
            
            CommonActions.db_setup      = config.get("DBInfo", "db_setup")
            CommonActions.instance_type = config.get("DBInfo", "instance_type")
        
            CommonActions.host          = config.get("DBInfo", "host")
            CommonActions.db            = config.get("DBInfo", "db")
            CommonActions.port          = config.get("DBInfo", "port")
            CommonActions.user          = config.get("DBInfo", "user")
            CommonActions.password      = config.get("DBInfo", "password")
            
            if CommonActions.tool == util.SYSBENCH:               
                CommonActions.table_engine = config.get("RunInfo", "mysql-table-engine")
                CommonActions.engine_trx   = config.get("RunInfo", "mysql-engine-trx")
                CommonActions.test_mode    = config.get("RunInfo", "oltp-test-mode")
                CommonActions.tables_count = config.get("RunInfo", "oltp-tables-count")
                CommonActions.table_size   = config.get("RunInfo", "oltp-table-size")
                CommonActions.max_time     = config.get("RunInfo", "max-time")
                CommonActions.max_requests = config.get("RunInfo", "max-requests")
                CommonActions.threads      = config.get("RunInfo", "num-threads")
                CommonActions.interval     = config.get("RunInfo", "report-interval")
                CommonActions.percentile   = config.get("RunInfo", "percentile")
                CommonActions.lua          = config.get("RunInfo", "lua-script")
            
            elif CommonActions.tool == util.TPCCMYSQL:             
                CommonActions.warehouse    = config.get("RunInfo", "warehouse")
                CommonActions.connection   = config.get("RunInfo", "connection")
                CommonActions.rampuptime   = config.get("RunInfo", "ramuptime")
                CommonActions.measuretime  = config.get("RunInfo", "meaasuretime")
                CommonActions.intervaltime = config.get("RunInfo", "intervaltime")
            
        except Exception as e:
            log.error(e)
    
    @classmethod
    def ca_exec_cmds(cls, cmd_str):
        cmd = shlex.split(cmd_str)
        p = subprocess.Popen(cmd, bufsize=-1, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.wait()
        
        time.sleep(util.SLEEP_TIME) # sleep 300 seconds between each execution
        
        res = p.communicate()
        cmd_result = []
        for cmd_line in res:
            cmd_result.append(cmd_line)
            
        return ''.join(cmd_result)
        
    @classmethod
    def __coma_combine_cmds(cls, *params):
        try:
            flag = " "
            param_list = []
            
            for param in params:
                param_list.append(param)
                
            return flag.join(param_list)
        except Exception as e:
            log.error(e)
            
    @classmethod
    def __coma_get_mysql_version(cls):
        str_chk_mysql_ver = CommonActions.__coma_combine_cmds(util.DB_MYSQL,
                                                          "".join(["-h", CommonActions.tool]),
                                                          "".join(["-u", CommonActions.user]),
                                                          "".join(["-p", CommonActions.password]),
                                                          "-e",
                                                          "\"select version()\"")
        mysql_ver = shlex.split(str_chk_mysql_ver)
        
        p = subprocess.Popen(mysql_ver, bufsize=-1, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.wait()
        
        mysql_ver_info = p.communicate()
        mysql_version = ''.join(re.findall(r"\d\.\d\.\d+-\w+", mysql_ver_info[0], re.M))
        
        return mysql_version
    
    
    
    
    
    
    
    
    
    
    
    
    