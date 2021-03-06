#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: InpatientMedicalOrder.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 9:29 PM
"""

from export import Task


class InpatientMedicalOrder(Task.Task):

    def __init__(self):
        super(InpatientMedicalOrder, self).__init__()
    
    def _get_sql_file(self):
        return 'sql/inpatientMedicalOrder.sql'

    def _process_row(self, row):
        results = [
            [row[0], row[1], row[5], None, row[2], '', '', row[3], row[4]],

        ]
        return results