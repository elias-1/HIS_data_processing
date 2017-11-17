#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: ClinicalMedicalOrder.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 9:19 PM
"""

from export import Task


class ClinicalMedicalOrder(Task.Task):

    def __init__(self):
        super(ClinicalMedicalOrder, self).__init__()
    
    def _get_sql_file(self):
        return 'sql/inpatientInfo.sql'

    def _process_row(self, row):
        pass