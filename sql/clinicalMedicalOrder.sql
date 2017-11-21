select a.card_no, -- 病历号 @old_pid@
--##a.see_no, -- 看诊序号 @see_no@
--##a.sequence_no, -- 项目流水号 @seq_no@
--##a.clinic_code, -- 门诊号 @clinic_id@
--##a.reg_date, -- 挂号日期 @reg_date@
--##a.dept_code, -- 挂号科室 @dept_code@
--##a.item_code, -- 项目代码 @映射并转换成收费项目国标编码gb_id/CDR药品统一编码写入CDR的item.id@
a.item_name, -- 项目名称 @item.name@
--##a.specs, -- 规格 @specs@
--##a.drug_flag, -- 1药品，2非药品 @drug_flag@
--##a.class_code, -- 系统类别 @[NEW_MO_CLASS]class.id,class.name@
--##a.fee_code, -- 最小费用代码 @fee_code@
--##a.unit_price, -- 单价 @unit_price@
a.qty, -- 开立数量 @qty@
--##a.days, -- 付数 @days@
--##a.pack_qty, -- 包装数量 @pack_qty@
--##a.item_unit, -- 计价单位 @item_unit@
--##a.own_cost, -- 自费金额 @own_cost@
--##a.pay_cost, -- 自负金额 @pay_cost@
--##a.pub_cost, -- 报销金额 @pub_cost@
--##a.base_dose, -- 基本剂量 @base_dose@
--##a.self_made, -- 自制药 @self_made@
--##a.drug_quanlity, -- 药品性质，普药、贵药 @[DRUGQUALITY]drug_property@
a.once_dose, -- 每次用量 @once_dose@
a.once_unit, -- 每次用量单位 @once_unit@
--##a.dose_model_code, -- 剂型代码 @[DOSAGEFORM]dose_form.id,dose_form.name@
--##a.frequency_code, -- 频次 @[NEW_FREQUENCY]freq.id@
--##a.frequency_name, -- 频次名称 @[NEW_FREQUENCY]freq.name@
--##a.usage_code, -- 使用方法 @[USAGE]usage.id@
--##a.usage_name, -- 用法名称 @[USAGE]usage.name@
--##a.english_ab, -- 用法英文缩写 @english_ab@
--##a.exec_dpcd, -- 执行科室代码 @exec_deptid@
--##a.exec_dpnm, -- 执行科室名称 @exec_deptname@
--##a.main_drug, -- 主药标志 @main_drug@
--##a.comb_no, -- 组合号 @comb_no@
--##a.hypotest, -- 1不需要皮试/2需要皮试，未做/3皮试阳/4皮试阴 @[NEW_HYPOTEST]hypotest.id,hypotest.name@
--##a.inject_number, -- 院内注射次数 @inject_number@
--##a.remark, -- 备注 @remark@
a.doct_code, -- 开立医生 @doct_id@
--##a.doct_name, -- 开立医生名称 @doct_name@
--##a.doct_dpcd, -- 医生科室 @doct_deptid@
a.oper_date -- 开立时间 @oper_date@
--##a.status -- 处方状态,0开立，1收费，2确认，3作废 @[MO_STATUS]status@
--##a.cancel_userid, -- 作废人 @cancel_userid@
--##a.cancel_date, -- 作废时间 @cancel_date@
--##a.emc_flag, -- 加急标记0普通/1加急 @emc_flag@
--##a.lab_type, -- 样本类型 @[SAMPLE]lab_type@
--##a.check_body, -- 检体 @[CHECKPART]check_body@
--##a.apply_no, -- 申请单号 @apply_no@
--##a.subtbl_flag, -- 0没有附材/1带附材/2是附材 @subtbl_flag@
--##a.need_confirm, -- 是否需要确认，1需要，0不需要 @need_confirm@
--##a.confirm_code, -- 确认人 @confirm_code@
--##a.confirm_dept, -- 确认科室 @confirm_dept@
--##a.confirm_date, -- 确认时间 @confirm_date@
--##a.charge_flag, -- 0未收费/1收费 @charge_flag@
--##a.charge_code, -- 收费员 @charge_code@
--##a.charge_date, -- 收费时间 @charge_date@
--##a.recipe_no, -- 处方号 @recipe_no@
--##a.recipe_seq, -- 处方内流水号 @recipe_seq@
--##a.phamarcy_code, -- 发药药房 @medstore_id@
--##a.minunit_flag, -- 开立单位是否是最小单位 1 是 0 不是 @minunit_flag@
--##a.ordertype, -- 医嘱类别 L 普通  Z 嘱托  B 补录医嘱 @ordertype@
--##a.subcombno, --  @subcombno@
--##a.resumeorder, --  @resumeorder@
--##a.recipe_feeseq, --  @recipe_feeseq@
--##a.pass_flag, --  @pass_flag@
--##a.sort_id, -- 排列序号，按排列序号由大到小顺序显示医嘱 @sort_id@
--##a.print_flag, -- 处方打印标志0未打1已打 @print_flag@
--##a.execreson as remark --  @remark@
--##a.ip_address --  @ip_address@
from met_ord_recipedetail a 
where a.oper_date >= TO_date('startDate','YYYY-MM-DD HH24:MI:SS')
and a.oper_date < TO_date('endDate', 'YYYY-MM-DD HH24:MI:SS')

