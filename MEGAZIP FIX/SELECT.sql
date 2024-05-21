SELECT 
	[0] E.cust_birth_place,
	[1] E.cust_marital_status,
	[2] E.cust_id_no,
	[3] E.cust_hp_no,
	[4] E.cust_mother_name,
	[5] E.cust_home_address,
	[6] E.cust_home_rt,
	[7] E.cust_home_rw,
	[8] E.cust_home_kelurahan,
	[9] E.cust_home_kecamatan,
	[10] E.cust_home_city,
	[11] E.cust_home_postal_code,
	[12] B.office_years_of_service,
	[13] B.office_months_of_service,
	[14] E.cust_id_address, 	
	[15] E.cust_id_rt, 	
	[16] E.cust_id_rw, 	
	[17] E.cust_id_kelurahan, 	
	[18] E.cust_id_kecamatan, 	
	[19] E.cust_id_city, 	
	[20] E.cust_id_postal_code,
	[21] E.cust_home_address,
	[22] E.cust_home_rt,
	[23] E.cust_home_rw,
	[24] E.cust_home_kelurahan,
	[26] E.cust_home_kecamatan,
	[27] E.cust_home_city,
	[28] E.cust_home_postal_code,
	[29] A.cmo_id,
	[30] A.asv_id,
	[31] A.fppm_id,
	[32] a.product_id,
	[33] a.otr,
	[34] a.insurance,
	[35] a.tenor,
	[36] a.admin,
	[37] a.net_dp,
	[38] a.dp,
	[39] a.customer_dp,
	[40] a.gross_dp,
	[41] a.installment,
	[42] a.nfa,
	[43] a.eff_rate_pa,
	[44] a.flat_rate,
	[45] a.amt_to_dealer,
    [46] A.order_id,
	[47] E.cust_full_name,
    [48] F.dealer_code
FROM TRN_ORDER A -- WHERE ORDER_ID ='BGRCC02266' 
LEFT JOIN CIF_KANTOR B ON A.order_id = B.customer_no
LEFT JOIN CIF_PRIBADI E ON B.customer_no = E.customer_NO
WHERE 1=1
and A.order_status LIKE '%PRE_ORDER_ENTRY%'
and A.product_id ='NMC'
AND A.branch_id ='BGR'
and A.order_id='BGRCC02266'
ORDER BY A.created_date DESC