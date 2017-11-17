#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: ClinicalInfo.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 9:25 PM
"""

from export import Task


class ClinicalInfo(Task.Task):

    def __init__(self):
        super(ClinicalInfo, self).__init__()
    
    def _get_sql_file(self):
        return 'sql/inpatientInfo.sql'

    def _process_row(self, row):
        pass