#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: TimeConfig.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 8:11 PM
"""

from utils import Logger

import traceback
import ConfigParser

Logger = Logger.Logger()
logger = Logger.get_logger()


class TimeConfig(object):
    def _get_fname(self):
        return  'config/config.conf'
    
    def read_time(self, section, key):
        cf = ConfigParser.ConfigParser()
        result = None
        try:
            cf.read(self._get_fname())
            result = cf.get(section, key)
        except:
            traceback.print_exc()
            logger.error('Read Time Error!', key)
        return result
    
    def write_time(self, section, key, value):
        cf = ConfigParser.ConfigParser()
        try:            
            cf.read(self._get_fname())
            cf.set(section, key, value)
            cf.write(open(self._get_fname(), 'w'))
        except:
            traceback.print_exc()
            logger.error('Read Time Error!', key)
        return True
