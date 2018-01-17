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
        return 'sql/patientDiagnose.sql'

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

    select case when b.card_no is not null
    then b.card_no else a.inpatient_no end,
    --##a.happen_no, -- 发生序号 @seq_id@
    a.diag_kind, -- 诊断类型 1 主要诊断 2 其他诊断 3 并发症 4 院内感染 5 损伤 6 病理诊断 7 过敏药 8 新生儿疾病 9 新生儿院感 10 门诊诊断 11 入院诊断 @[new_diag_kind]kind.id,kind.name@
    --##a.level_code, -- 诊断级别 @level_code@
    --##a.perior_code, -- 诊断分期 @perior_code@
    a.icd_code, -- 诊断icd码 @icd_id@
    a.diag_name, -- 诊断名称 @diag.name@
    a.diag_date, -- 诊断日期 @diag.date@
    a.doct_code, -- 医师代号 @doct.id@
    --##a.doct_name, -- 医师姓名(诊断) @doct.name@
    --##a.in_date, -- 入院日期 @in_date@
    --##a.out_date, -- 出院日期 @out_date@
    --##a.diag_outstate, -- 治疗情况 0 治愈1 好转 2 未愈3 死亡 4 其他 @diag_outstate@
    --##a.second_icd, -- 第二icd @second_icd@
    --##a.syndrome_id, -- 并发症类别 @syndrome_id@
    --##a.cl_pa, -- 病理符合 @coincidence@ 0 不符合 1 符合
    a.dubdiag_flag, -- 是否疑诊 @suspected@
    --##a.main_flag, -- 是否主诊断 @main_flag@
    --##a.remark, -- 备注 @remark@
    --##a.oper_code, -- 操作员 @oper.id@
    a.oper_date -- 操作时间 @oper_date@
    --##a.oper_type, -- 类别 1 医生站录入诊断  2 病案室录入诊断 @oper_type@
    --##a.operation_flag -- 手术标志 @[operationtype]operation_type@ 没有数据
    --##a.is30disease -- 是否是30种疾病 @is30disease@
    from met_cas_diagnose a
    left join fin_ipr_inmaininfo b on a.inpatient_no=b.inpatient_no 
    """
    def _process_row(self, row):
        diag_kind = {
            '1' : '主要诊断',
            '2' : '其他诊断',
            '3' : '并发症',
            '4' : '院内感染',
            '5' : '损伤',
            '6' : '病理诊断',
            '7' : '过敏药',
            '8' : '新生儿疾病',
            '9' : '新生儿院感',
            '10' : '门诊诊断',
            '11' : '入院诊断'
        }
        results = [
            [row[0], row[5], row[4], None, diag_kind[row[1]], '', '疑诊' if row[6] == '1' else '', row[2], ''],
            [row[0], row[5], row[4], None, diag_kind[row[1]], '', '疑诊' if row[6] == '1' else '', row[3], ''],

        ]
        return results