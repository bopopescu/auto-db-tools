#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2015-05-28

@author: mizhon
'''

import os
import sys
import logging

class Log(object):

    """SysbenchLog info class"""
    def __init__(self):
        """Init log format"""
        self.formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')

        self.file_handler = logging.FileHandler(self.get_adt_log_file())
        self.file_handler.setFormatter(self.formatter)

        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.stream_handler.setFormatter(self.formatter)

    def get_logger(self):
        """Set log record level"""
        log_instance = logging.getLogger()
        log_instance.setLevel(logging.INFO)
        log_instance.addHandler(self.file_handler)
        log_instance.addHandler(self.stream_handler)
        return log_instance

    def debug(self, msg):
        """Record DEGBU message"""
        f = sys._getframe(1)
        filename = os.path.split(f.f_code.co_filename)[-1]
        lineno = f.f_lineno
        self.get_logger().debug("[%s:%d] : %s" % (filename, lineno, msg))

    def info(self, msg):
        """Record INFO message"""
        f = sys._getframe(1)
        filename = os.path.split(f.f_code.co_filename)[-1]
        lineno = f.f_lineno
        self.get_logger().info("[%s:%d] : %s" % (filename, lineno, msg))

    def warn(self, msg):
        """Record WARN message"""
        f = sys._getframe(1)
        filename = os.path.split(f.f_code.co_filename)[-1]
        lineno = f.f_lineno
        self.get_logger().warn("[%s:%d] : %s" % (filename, lineno, msg))

    def error(self, msg):
        """Record ERROR message"""
        f = sys._getframe(1)
        filename = os.path.split(f.f_code.co_filename)[-1]
        lineno = f.f_lineno
        self.get_logger().error("[%s:%d] : %s" % (filename, lineno, msg))

    def get_adt_log_file(self):
        log_dir = self.__get_log_dir()
        log_file = os.path.join(log_dir, 'ADT.log')

        return log_file
    
    def get_log_path(self):
        return self.__get_log_dir()

    def __get_log_dir(self):
        """Get log folder path"""
        current_file = os.path.realpath(__file__)
        current_folder = os.path.dirname(current_file)
        log_folder = os.path.join(current_folder, "logs")
        if os.path.exists(log_folder):
            pass
        else:
            os.makedirs(log_folder)

        return log_folder

if __name__ == "__main__":
    log = Log()

    log.debug("DEBUG testing...")
    log.info("INFO testing...")
    log.warn("WARN testing...")
    log.error("ERROR testing...") 
    
    
    

