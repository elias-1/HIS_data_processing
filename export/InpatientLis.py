#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: InpatientLis.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 9:19 PM
"""

from export import Task


class InpatientLis(Task.Task):

    def __init__(self):
        super(InpatientLis, self).__init__()
    
    def _get_sql_file(self):
        return 'sql/inpatientLis.sql'

    def _process_row(self, row):
        results = [
            [row[0], row[1] if row[1] is not None else '', row[2], None, row[3] if row[3] is not None else '', '', row[5], row[4], (str(row[6])+'||'+str(row[7])).replace('None', '')],
        ]
        return results