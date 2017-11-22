#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: main.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 8:11 PM
"""

import sys

from functools import partial
from multiprocessing import Pool

from export import Task
from export import PatientInfo
from export import ClinicalMedicalOrder
from export import InpatientMedicalOrder
from export import PatientDiagnose

reload(sys)
sys.setdefaultencoding('utf8')


__factory = [
    PatientInfo.PatientInfo(),
    # ClinicalMedicalOrder.ClinicalMedicalOrder(),
    # InpatientMedicalOrder.InpatientMedicalOrder(),
    # PatientDiagnose.PatientDiagnose(),
]


def do_task(i):
    __factory[i].export_data()


def main():
    Task.create_pg_table()

    pool = Pool(len(__factory))
    partial_do_task = partial(do_task)
    pool.map(partial_do_task, range(len(__factory)))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
