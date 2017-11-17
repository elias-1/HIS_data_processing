#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: OracleConn.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 8:11 PM
"""

from utils import Logger
import cx_Oracle 
import traceback
import ConfigParser
import os 

logger = Logger.Logger().get_logger()

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 


class OracleConn(object):
    def __init__(self, db_url='url_his'):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read('config/config.conf')
            url = cf.get('oracle', db_url)
            self.conn = cx_Oracle.connect(url)
        except Exception:
            logger.error('连接oracke数据库失败!')
            traceback.print_exc()
            
    def destroy(self):
        self.conn.close()
        
    def __del__(self):
        try:
            self.conn.close()
        except cx_Oracle.InterfaceError:
            traceback.print_exc()
        
    def get_db(self):
        return self.conn

if __name__ == '__main__':
    oc = OracleConn()
    conn = oc.get_db()
    print conn