#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: Logger.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 8:11 PM
"""

import logging.config
from utils import Singleton
import traceback


class Logger(Singleton.Singleton):
    logger = None

    def __init__(self):
        if self.logger is None:
            try:
                logging.config.fileConfig('config/logger.conf')
                self.logger = logging.getLogger('exportLog')
            except:
                traceback.print_exc()
        
    def get_logger(self):
        return self.logger
