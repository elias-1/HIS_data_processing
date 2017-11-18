#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: PatientDiagnose.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 9:19 PM
"""

from export import Task


class PatientDiagnose(Task.Task):

    def __init__(self):
        super(PatientDiagnose, self).__init__()
    
    def _get_sql_file(self):
        return 'sql/patientInfo.sql'

    def _process_row(self, row):
        pass