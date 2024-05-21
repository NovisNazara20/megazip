SELECT TOP 10 * FROM TRN_ORDER WHERE PRODUCT_ID='MM4' ORDER BY created_date DESC
SELECT TOP 10 * FROM CIF_PRIBADI  ORDER BY created_date DESC
SELECT TOP 10 * FROM TRN_OBJECT  ORDER BY created_date DESC
SELECT TOP 10 * FROM TRN_OBJECT_DOC WHERE order_id='BGRCC02228' ORDER BY created_date DESC
--PAJAK STNK (2) MATI
--1 = HIDUP
STATUS PAJAK STNK 4
SELECT * FROM MST_ATAS_NAMA_STNK
SELECT * FROM MST_STATUS_PAJAK_STNK
SELECT TOP 1 * FROM TRN_ORDER_EXT_MM WHERE order_id='BGRCC02228' ORDER BY created_date DESC
select * from faktur

SELECT TOD.atas_nama_stnk, TOD.isSatuKK, TOD.status_milik_stnk, TOD.bpkb_no, TOD.status_pajak_stnk FROM TRN_OBJECT_DOC WHERE order_id='BGRCC02228' ORDER BY created_date DESC
SELECT TOEM.isFakturExist, TOEM.tipe_mitra_id, TOEM.mitra_id FROM TRN_ORDER_EXT_MM WHERE order_id='BGRCC02228' ORDER BY created_date DESC

SELECT TOD.atas_nama_stnk, TOD.isSatuKK, TOD.status_milik_stnk, TOD.bpkb_no, TOD.status_pajak_stnk,TOEM.isFakturExist, TOEM.tipe_mitra_id, TOEM.mitra_id FROM TRN_OBJECT_DOC TOD INNER JOIN TRN_ORDER_EXT_MM TOEM ON TOD.order_id = TOEM.order_id WHERE TOD.order_id ='BGRCC02228'


SELECT * FROM [alias.dbo.pasnet].PMF.DBO.mm_agent WHERE NAME LIKE '%PERCOBAAN JUMAT%'
SELECT * FROM [alias.dbo.pasnet].PMF.DBO.MM_AGENT_MASTER_TIPE


SELECT TOP 10 * FROM TRN_ORDER_FILE_EXT WHERE order_id='BGRCC00242' ORDER BY created_date DESC
SELECT TOP 10 * FROM TRN_ORDER_FILE WHERE order_id='BGRCC00242' ORDER BY created_date DESC
SELECT TOP 10 * FROM cif_pasangan  ORDER BY created_date DESC
SELECT TOP 10 * FROM CIF_PENJAMIN  ORDER BY created_date DESC
SELECT TOP 10 * FROM TRN_ORDER_SLA  ORDER BY created_date DESC
--SELECT  * FROM TRN_CREDIT_SCORE WHERE order_id='BGRCC00491' -- ORDER BY created_date DESC

SELECT branch_id_login, fin_code, dealer_id FROM TRN_ORDER where order_id='BGRCC00493'

"select order_id, md_no from TRN_ORDER_APPROVAL where order_id = '"+inOrderIdMfast+"' and md_no is not null"

SELECT top 1 order_id,* FROM TRN_ORDER WHERE PRODUCT_ID='MM4' and created_by = '202100317' order by created_date desc

SELECT TOP 1 customer_no, CUST_NAME, cust_birth_place, cust_dob, cust_id_no, cust_marital_status,cust_house_status, cust_mother_name, cust_home_address, cust_home_kelurahan, cust_home_kecamatan,cust_home_city, cust_home_postal_code, cust_hp_no, cust_id_city, cust_home_rt, cust_home_rw, created_date AS TANGGALCREATED, created_by 
FROM CIF_PRIBADI WHERE customer_no = 'BGRCC02228'
ORDER BY created_date DESC
        

SELECT brand_id,series_id,type_id,year,chassis_no,engine_no,license_plate_no,created_by, created_date, qq_stnk FROM TRN_OBJECT where order_id='BGRCC00493'

SELECT * FROM [alias.dbo.pasnet].PMF.DBO.ITEMS where itemid='002'
select * from [alias.dbo.pasnet].PMF.DBO.ItemType where itemid='002' and ItemMerkID='998' and ItemSeriesID='198' and ItemTypeID='2327'
select * from [alias.dbo.pasnet].PMF.DBO.ItemSeries where itemid='002' and ItemMerkID='998' and ItemSeriesID='198'
select * from [alias.dbo.pasnet].PMF.DBO.ItemMerk where itemid='002'  and ItemMerkID='998' 






SELECT * FROM CIF_PRIBADI WHERE 1=1
--customer_no='BGRCC00493'
and  CUST_ID_NO='3525134507920002'
ORDER BY created_date DESC

SELECT TOP 1 customer_no, CUST_NAME, cust_birth_place, cust_dob, cust_id_no,cust_marital_status,cust_house_status, cust_mother_name, cust_home_address, cust_home_kelurahan, 
cust_home_kecamatan,cust_home_city, cust_home_postal_code, cust_hp_no, cust_id_city, cust_home_rt, cust_home_rw, created_date AS TANGGALCREATED, created_by
FROM CIF_PRIBADI WHERE CUST_ID_NO='3525134507920002' ORDER BY created_date DESC

SELECT TOP 1 cust_id_no FROM CIF_PRIBADI WHERE CUST_ID_NO='3525134507920002' and created_by='202100317' ORDER BY created_date DESC

SELECT TOP 1 customer_no, CUST_NAME, cust_birth_place, cust_dob, cust_id_no,cust_marital_status,cust_house_status, cust_mother_name, cust_home_address, 
cust_home_kelurahan, cust_home_kecamatan,cust_home_city, cust_home_postal_code, cust_hp_no, cust_id_city, cust_home_rt, cust_home_rw, created_date AS TANGGALCREATED, 
created_by FROM CIF_PRIBADI WHERE CUST_ID_NO='3525134507920002' and created_by='202100317' ORDER BY created_date DESC
 
select office_occupation_id, office_sub_occupation_id, office_years_of_service, office_months_of_service from cif_kantor where customer_no ='BGRCC00493' and created_by='202100317' 
order by created_date desc


SELECT TOP 1 * FROM TRN_OBJECT
SELECT TOP 1 * FROM TRN_OBJECT_HISTORY
SELECT TOP 1 * FROM TRN_ORDER_APPROVAL
SELECT TOP 1 * FROM TRN_ORDER_APPROVAL_HISTORY
SELECT TOP 1 * FROM TRN_ORDER_FILE
SELECT TOP 1 * FROM TRN_ORDER
SELECT TOP 1 * FROM TRN_ORDER
SELECT TOP 1 * FROM TRN_ORDER
SELECT TOP 1 * FROM TRN_ORDER


= "SELECT TOP 1 customer_no, CUST_NAME, cust_birth_place, cust_dob, cust_id_no, cust_marital_status,cust_house_status, cust_mother_name, cust_home_address, cust_home_kelurahan, cust_home_kecamatan,cust_home_city, cust_home_postal_code, cust_hp_no, cust_id_city, cust_home_rt, cust_home_rw, created_date AS TANGGALCREATED, created_by 
 FROM CIF_PRIBADI WHERE CUST_ID_NO='3525134507920002' and created_by='202100317' ORDER BY created_date DESC")
        
        query2 = dbCon.DbMflos(query = "SELECT TOP 1 office_occupation_id, office_sub_occupation_id, office_years_of_service, office_months_of_service 
		from cif_kantor where customer_no ='BGRCC00493' and created_by='202100317' order by created_date desc ")
        query3 = dbCon.DbMflos(query = "SELECT branch_id_login, fin_code, dealer_id FROM TRN_ORDER where order_id='BGRCC00493'")
        query4 = dbCon.DbMflos(query = "SELECT brand_id,series_id,type_id,year,chassis_no,engine_no,license_plate_no,created_by, created_date, qq_stnk 
		FROM TRN_OBJECT where order_id='BGRCC00493'")
        query5 = dbCon.DbMflos(query = "SELECT TOD.atas_nama_stnk, TOD.isSatuKK, TOD.status_milik_stnk, TOD.bpkb_no, TOD.status_pajak_stnk,TOBM.isFakturExist, TOBM.tipe_mitra_id, TOBM.mitra_id FROM TRN_OBJECT_DOC TOD INNER JOIN TRN_ORDER_EXT_MM TOBM ON TOD.order_id = TOBM.order_id WHERE TOD.order_id ='BGRCC02228'")
        

SELECT cp.customer_no,cp.CUST_NAME,cp.cust_birth_place,cp.cust_dob,cp.cust_id_no,cp.cust_marital_status,cp.cust_house_status,cp.cust_mother_name,cp.cust_home_address,cp.cust_home_kelurahan,cp.cust_home_kecamatan,cp.cust_home_city,cp.cust_home_postal_code,cp.cust_hp_no,cp.cust_id_city,cp.cust_home_rt,cp.cust_home_rw,cp.created_date AS TANGGALCREATED,cp.created_by,ck.office_occupation_id,ck.office_sub_occupation_id,ck.office_years_of_service,ck.office_months_of_service,TRN.branch_id_login, TRN.fin_code, TRN.dealer_id,TOB.brand_id,TOB.series_id,TOB.type_id,TOB.year,TOB.chassis_no,TOB.engine_no,TOB.license_plate_no,TOB.created_by,TOB.created_date,TOB.qq_stnk,TOD.atas_nama_stnk, TOD.isSatuKK, TOD.status_milik_stnk, TOD.bpkb_no, TOD.status_pajak_stnk,TOBM.isFakturExist, TOBM.tipe_mitra_id, TOBM.mitra_id FROM CIF_PRIBADI CP
INNER JOIN CIF_KANTOR CK ON cp.customer_no = CK.customer_no
inner join TRN_ORDER TRN on CP.customer_no = trn.order_id
inner join TRN_OBJECT TOB ON TRN.order_id = TOB.order_id
inner join TRN_ORDER_EXT_MM TOBM ON TRN.order_id = TOBM.order_id
inner join TRN_OBJECT_DOC TOD ON TRN.order_id = TOD.order_id

