#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: Task.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 8:30 PM
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

from utils import OracleConn
from utils import TimeConfig
from utils import Logger
import traceback

import psycopg2
import ConfigParser
import time
Logger = Logger.Logger()
logger = Logger.get_logger()
timecfg = TimeConfig.TimeConfig()


def create_pg_table():
    cf = ConfigParser.ConfigParser()
    cf.read('config/config.conf')
    connect_info = cf.get('postgresql', 'connect')
    pg_conn = psycopg2.connect(connect_info)
    try:
        sql = """CREATE TABLE clinical_data (
                      id SERIAL PRIMARY KEY,
                      pat_num varchar(20) not null,
                      provider_id varchar(20) not null,
                      start_date date,
                      end_date date,
                      concept_cd varchar(200) not null,
                      modifier_cd varchar(50),
                      tval_char varchar(200),
                      nval_num varchar(200),
                      units_cd varchar(200)
                  )
        """
    
        cur = pg_conn.cursor()
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        pg_conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error('failed process create_pg_table: ' + error.message)
    finally:
        pg_conn.close()


class Task(object):
    def __init__(self):
        self._init_processing_time()

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def _init_processing_time(self):
        self._start_time = timecfg.read_time('time', 'start')
        if self._start_time is None:
            self._start_time = '1970-01-01 00:00:00'
        self._end_time = timecfg.read_time('time', 'end')

    def export_data(self):
        cf = ConfigParser.ConfigParser()
        cf.read('config/config.conf')
        connect_info = cf.get('postgresql', 'connect')

        pg_conn = psycopg2.connect(connect_info)
        or_cursor = None
        try:
            start_date_str = self.get_start_time()
            end_date_str = self.get_end_time()
            oracle_conn = OracleConn.OracleConn()
            conn = oracle_conn.get_db()
            or_cursor = conn.cursor()
            # print(self._get_sql(start_date_str, end_date_str))
            or_cursor.execute(self._get_sql(start_date_str, end_date_str))
            row = or_cursor.fetchone()
            num = 0
            start = time.time()
            while row:
                row = list(row)
                result_row = self._process_row(row)
                self._insert2pgdb(result_row, pg_conn)
                row = or_cursor.fetchone()
                num += 1
                if num % 1000 == 0:
                    logger.info(
                        self._get_sql_file() + \
                        ': Have processed %d; used time %3.2f seconds' %
                        (num, time.time()-start))
                    pg_conn.commit()

        except Exception, e:
            traceback.print_exc()
            logger.error('failed process ' + self._get_sql_file() + e.message)
            raise e
        finally:
            if or_cursor is not None:
                or_cursor.close()
            pg_conn.close()

    def _insert2pgdb(self, data, pg_conn):
        try:
            cur = pg_conn.cursor()
            # execute the INSERT statement
            args_str = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", x) for x in data)
            cur.execute('INSERT INTO clinical_data '
                        '(pat_num, provider_id, start_date, end_date, '
                        'concept_cd, modifier_cd, tval_char, nval_num, '
                        'units_cd) VALUES ' + args_str)
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as e:
            traceback.print_exc()
            logger.error('failed execute insert2db ' + e.message)
            raise e

    def _get_sql(self, start_date, end_date):
        file_obj = open(self._get_sql_file())
        try:
            sql_str = file_obj.read()
            sql_str = sql_str.replace('start_date', start_date)
            sql_str = sql_str.replace('end_date', end_date)
            file_obj.close()
            return sql_str
        except Exception, e:
            file_obj.close()
            traceback.print_exc()
            logger.error('failed open' + self._get_sql_file() + '!')
            raise e

    def _get_sql_file(self):
        raise Exception('not implementation _get_sql_file')

    def _process_row(self, row):
        raise Exception('not implementation _process_row')
