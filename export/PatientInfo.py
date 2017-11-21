#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 www.drcubic.com, Inc. All Rights Reserved
#
"""
File: PatientInfo.py
Author: shileicao(shileicao@stu.xjtu.edu.cn)
Date: 17/11/2017 9:19 PM
"""

from export import Task


class PatientInfo(Task.Task):

    def __init__(self):
        super(PatientInfo, self).__init__()
    
    def _get_sql_file(self):
        return 'sql/inpatientInfo.sql'


    """
    pat_num,
    provider_id,
    start_date,
    end_date,
    concept_cd,
    modifier_cd,
    tval_char,
    nval_num,
    units_cd
    
    select a.card_no,
       regexp_replace(a.name,'[0-9\* ,，．\.\?？；;０１２３８／]*'),
       Trunc(MONTHS_BETWEEN(SYSDATE,a.birthday)/12),
       trim(a.sex_code) as sex_id,
       case when decode(length(regexp_replace(b.idenno, '[^0-9xx]')), 18, 1, 0)=1
       then regexp_replace(b.idenno, '[^0-9xx]') else regexp_replace(a.idenno, '[^0-9xx]') end as id_no,
       trim(a.home) as home,
       case when regexp_replace(a.home_tel, '[^0-9]') is not null
       then regexp_replace(a.home_tel, '[^0-9]')
       when regexp_replace(a.work_tel, '[^0-9]') is not null
       then regexp_replace(a.work_tel, '[^0-9]')
       else regexp_replace(a.home_tel, '[^0-9]') end as tel,
       trim(a.mari) as mari_id,
       trim(a.nation_code) as nation_id,
       a.oper_date
    from com_patientinfo a
    """
    def _process_row(self, row):
        results = [
            row[0], '', row[9], None, 'Name', '', '',  row[1], '',
            row[0], '', row[9], None, 'Age', '', '',  row[2], '岁',
            row[0], '', row[9], None, 'Gender', '', '',  row[3], '',
            row[0], '', row[9], None, 'ID NO', '', '',  row[4], '',
            row[0], '', row[9], None, 'Home Address', '', '', row[5], '',
            row[0], '', row[9], None, 'Telephone', '', '',  row[6], '',
            row[0], '', row[9], None, 'Marital Status ', '', '',  row[7], '',
            row[0], '', row[9], None, 'NATION', '', '',  row[8], '',
        ]
        return results