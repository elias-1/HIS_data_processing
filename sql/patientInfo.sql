select a.card_no,
       regexp_replace(a.name,'[0-9\* ,，．\.\?？；;０１２３８／]*'),
       FTrunc(MONTHS_BETWEEN(SYSDATE,a.birthday)/12),
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
left join fin_ipr_inmaininfo b on a.card_no=b.card_no
where 1=1
and a.oper_date>=to_date('startDate','YYYY-MM-DD HH24:MI:SS')
and a.oper_date<to_date('endDate','YYYY-MM-DD HH24:MI:SS')
and regexp_replace(a.name,'[0-9\* ,，．\.\?？；;０１２３８／]*') is not null