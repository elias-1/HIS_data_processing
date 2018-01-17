select c.card_no, --  @old_pid@
-- a.inspection_id, --  @inspection_id@
-- a.group_id, --  @group_id@
--##a.inspection_date, --  @inspection_date@
--##a.inspection_time, --  @inspection_time@
-- a.sample_number, --  @sample_number@
-- a.requisition_id, --  @requisition_id@
-- a.patient_type, --  @patient_type@
--##a.outpatient_id, --  @outpatient_id@
--##a.inpatient_id, --  @inpatient_id@
--##a.invoice_id, --  @invoice_id@
--##a.charge_type, --  @charge_type@
-- a.patient_name, --  @name@
-- a.patient_sex, --  @sex@
--##a.age_type, --  @age_type@
--##a.age_input, --  @age@
--##a.age_save, --  @age2@ ×××1岁以内有用×××
--##a.patient_nation, --  @patient_nation@
--##a.patient_nation_name, --  @patient_nation_name@
--##a.bloodtype_abo, --  @bloodtype_abo@
--##a.bloodtype_rh, --  @bloodtype_rh@
--##a.patient_dept, --  @patient_dept@
--##a.patient_dept_name, --  @patient_dept_name@
--##a.patient_ward, --  @patient_ward@
--##a.patient_ward_name, --  @patient_ward_name@
--##a.patient_bed, --  @patient_bed@
--##a.especial_condition, --  @especial_condition@
--##a.clinical_diagnoses, --  @clinical_diagnoses@
--##a.clinical_diagnoses_name, --  @clinical_diagnoses_name@
-- a.sample_class, --  @sample_class.id@
-- a.sample_class_name, --  @sample_class.name@
--##a.infect_status, --  @infect_status@没有数据
--##a.sample_status, --  @sample_status@
--##a.sample_status_name, --  @sample_status_name@
--##a.sampling_position, --  @sampling_position@
--##a.sampling_position_name, --  @sampling_position_name@
-- a.test_order, --  @test_order@
-- a.test_order_name, --  @test_order_name@
--##a.sample_charge, --  @sample_charge@
--##a.item_count, --  @item_count@
--##a.workload, --  @workload@
-- a.sampling_time, --  @sampling_time@ 样本时间
-- a.sampling_person, --  @sampling_person@
-- a.requisition_time, --  @requisition_time@申请时间
-- a.requisition_person, --  @requisition_person@
-- --##a.deliver_hospital, --  @deliver_hospital@
-- a.incept_time, --  @incept_time@样本接收时间
-- a.incept_person, --  @incept_person@
-- a.input_person, --  @input_person@
-- a.input_time, --  @input_time@上机时间
-- a.inspection_person, --  @inspection_person@检验技师
a.check_person, --  @check_person@审核技师
a.check_time, --  @check_time@检验时间（发报告时间）
--##a.print_person, --  @print_person@
--##a.print_time, --  @print_time@
--##a.print_count, --  @print_count@
--##a.expert_rule, --  @expert_rule@
--##a.charge_state, --  @charge_state@
-- a.inspection_state, --  @[NEW_LIS_STATE]state.id,state.name@
--##a.rerun_state, --  @rerun_state@
--##a.read_state, --  @read_state@
-- a.remark, --  @remark@
--##a.remark_name, --  @remark_name@
--##a.id_card, --  @id_card@
--##a.confirm_person, --  @confirm_person@
--##a.confirm_time, --  @confirm_time@
-- a.instrument, --  @instrument@
--##a.patient_type_old, --  @patient_type_old@
--##a.mobileno, --  @mobileno@
--##a.send_date, --  @send_date@
--##a.send_state, --  @send_state@
--##a.patient_birthday, --  @patient_birthday@
--##a.exchange_state, --  @exchange_state@
--##a.exchange_time, --  @exchange_time@
--##a.exchange_hospital, --  @exchange_hospital@
--##a.sample_id, --  @sample_id@
--##a.return_cause, --  @return_cause@
--##a.lis5_prepared, --  @lis5_prepared@
--##a.print_page, --  @print_page@
--##a.print_no, --  @print_no@
--##a.serial_no, --  @serial_no@
--##a.pdf_flag, --  @pdf_flag@
--##a.machine_time, --  @machine_time@
--##a.positive_time, --  @positive_time@
--##a.rh_phenotype, --  @rh_phenotype@
--##a.d_flag, --  @d_flag@
--##a.positive_time2, --  @positive_time2@
--##a.c_person, --  @c_person@
--##a.c_time, --  @c_time@
--##a.read_person, --  @read_person@
--##a.read_time, --  @read_time@
--##a.collect_person, --  @collect_person@
--##a.collect_time, --  @collect_time@
--##a.collect_state, --  @collect_state@
--##a.yp, --  @yp@
--##a.rdstate, --  @rdstate@
--##a.forecast_time, --  @forecast_time@
--##a.resultfinish_time, --  @resultfinish_time@
--##a.lab_id, --  @lab_id@
--##a.area_id, --  @area_id@
--##a.special_item, --  @special_item@
--##a.alarm_item, --  @alarm_item@
--##a.assembly_line, --  @assembly_line@
--##a.auto_check, --  @auto_check@
--##a.return_person, --  @return_person@
--##a.rdflag1, --  @rdflag1@
--##a.patient_id, --  @patient_id@
--##a.charge_num, --  @charge_num@
--##a.left, --  @left@
--##a.data_from, --  @data_from@
--##a.alarm_reference, --  @alarm_reference@
--##a.address, --  @address@
--##a.internet_sendstate, --  @internet_sendstate@
--##a.visit_num, --  @visit_num@
--##a.infection_state, --  @infection_state@
--##a.run_state, --  @run_state@
--##a.addcheck_time, --  @addcheck_time@
--##a.addcheck_person, --  @addcheck_person@
--##a.rd_state, --  @rd_state@
--##a.rdflag, --  @rdflag@
--##b.inspection_id, --  @inspection_id@
-- b.test_item_id, --  @test_item_id@
--##b.group_id, --  @group_id@
-- b.inspection_date, --  @inspection_date@
-- b.inspection_time, --  @inspection_time@
--##b.sample_number, --  @sample_number@
-- b.test_item_sort, --  @test_item_sort@
-- b.english_name, --  @english_name@
b.chinese_name, --  @chinese_name@
-- b.original_result, --  @original_result@
b.quantitative_result, --  @quantitative_result@
b.qualitative_result, --  @qualitative_result@
b.test_item_reference, --  @test_item_reference@
b.test_item_unit --  @test_item_unit@
--##b.test_item_charge, --  @test_item_charge@
--##b.workload, --  @workload@
--##b.test_count, --  @test_count@
--##b.test_order, --  @test_order@  比如是肝功十项code
-- b.inspection_instrument, --  @inspection_instrument@
--##b.inspection_person, --  @inspection_person@
--##b.inspection_position, --  @inspection_position@
--##b.report_id, --  @report_id@
--##b.col_position, --  @col_position@
--##b.print_id, --  @print_id@
--##b.remark, --  @remark@
--##b.check_person, --  @check_person@
--##b.check_time, --  @check_time@
--##b.inspection_reagent, --  @inspection_reagent@
--##b.test_method, --  @test_method@
-- b.his_id  --  @his_id@
--##b.result_type, --  @result_type@
--##b.data_from, --  @data_from@
--##b.alarm_flag, --  @alarm_flag@
--##b.alarm_reference, --  @alarm_reference@
--##b.inspection_datetime, --  @inspection_datetime@
--##b.rerun_instrument, --  @rerun_instrument@
--##b.rerun_result, --  @rerun_result@
from LIS_INSPECTION_SAMPLE a
inner join LIS_INSPECTION_RESULT b on a.inspection_id=b.inspection_id
inner join com_patientinfo c on a.outpatient_id=c.card_no
where a.input_time >= TO_date('start_date','YYYY-MM-DD HH24:MI:SS')
and a.input_time < TO_date('end_date', 'YYYY-MM-DD HH24:MI:SS')--&&--
order by c.card_no