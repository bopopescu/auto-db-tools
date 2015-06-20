'''
Created on 2015-06-20

@author: mizhon
'''
import os
import argparse
import textwrap

from Logs import logger
log = logger.Log()


class CommonActions(object):
    
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

            
            
    
    
    
    
    