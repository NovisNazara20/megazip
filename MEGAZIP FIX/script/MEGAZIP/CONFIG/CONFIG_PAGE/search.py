import pyodbc
import pandas as pd
import difflib
import importlib.util
from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from importlib.machinery import SourceFileLoader

class BasePage(object):
    def __init__ (self,driver):
        self.driver = driver

class Search(BasePage):
    def Search_id_Province(self, Prov_Desc):
        dbCon = SourceFileLoader("configMzip","script/CONFIG/CONFIG_DB/configMzip.py").load_module()
        Data1 = dbCon.DbMzip(query="select province_id, description From loc_province where description='"+Prov_Desc+"'")
        for data in Data1 :
            arrayresult = {}
            arrayresult["id"] = data[0]
            arrayresult["desc"] = data[1]
        return arrayresult

    def Search_id_City(self, City_Desc, Prov_ID):
        dbCon = SourceFileLoader("configMzip","script/CONFIG/CONFIG_DB/configMzip.py").load_module()
        Data1 = dbCon.DbMzip(query="""select distinct lc.city_id, lc.description From loc_location ll with (nolock)
                                    Inner join loc_city lc with (nolock) on ll.city_id=lc.city_id
                                    where ll.province_id="""+Prov_ID+""" and lc.description='"""+City_Desc+"""'""")
        for data in Data1 :
            arrayresult = {}
            arrayresult["id"] = data[0]
            arrayresult["desc"] = data[1]
        return arrayresult

    def Search_id_District(self, District_Desc, Prov_ID, City_ID):
        dbCon = SourceFileLoader("configMzip","script/CONFIG/CONFIG_DB/configMzip.py").load_module()
        Data1 = dbCon.DbMzip(query="""select distinct ld.district_id, ld.description From loc_location ll with (nolock)
                                      Inner join loc_district ld with (nolock) on ll.district_id=ld.district_id
                                      where ll.province_id='"""+Prov_ID+"""' and ll.city_id="""+City_ID+""" 
                                      and ld.description='"""+District_Desc+"""'""")
        for data in Data1 :
            arrayresult = {}
            arrayresult["id"] = data[0]
            arrayresult["desc"] = data[1]
        return arrayresult

    def Search_id_Village(self,Village_Desc, Prov_ID, City_ID, District_ID):
        dbCon = SourceFileLoader("configMzip","script/CONFIG/CONFIG_DB/configMzip.py").load_module()
        Data1 = dbCon.DbMzip(query="""select lv.village_id, lv.description From loc_location ll with (nolock)
                                      Inner join loc_village lv with (nolock) on ll.village_id=lv.village_id
                                      where ll.province_id='"""+Prov_ID+"""' and ll.city_id="""+City_ID+""" 
                                      and ll.district_id='"""+District_ID+"""' and lv.description='"""+Village_Desc+"""'""")
        for data in Data1 :
            arrayresult = {}
            arrayresult["id"] = data[0]
            arrayresult["desc"] = data[1]
        return arrayresult

    def Search_Zipcode(self, Prov_ID, City_ID, District_ID, Village_ID):
        dbCon = SourceFileLoader("configMzip","script/CONFIG/CONFIG_DB/configMzip.py").load_module()
        Data1 = dbCon.DbMzip(query="""select zip_code, location_id From loc_location with (nolock)
                                      where province_id='"""+Prov_ID+"""' and city_id="""+City_ID+""" 
                                      and district_id='"""+District_ID+"""' and village_id='"""+Village_ID+"""'""")
        for data in Data1 :
            arrayresult = {}
            arrayresult["Zipcode"] = data[0]
            arrayresult["Loc_id"] = data[1]
        return arrayresult

    def Search_OTRMM(self, AreaId, TypeId):
        dbCon = SourceFileLoader("configMflos","script/CONFIG/CONFIG_DB/configMflos.py").load_module()
        Data1 = dbCon.DbMflos(query="select harga From MST_OTR_MM where area_id='"+AreaId+"' and item_type_id='"+TypeId+"'")
        for data in Data1:
            HargaOTRMM = data[0]
        return HargaOTRMM

    def Search_DepOTRMM(self, AreaId, ItemId, MerkId, SeriesId,Tahun):
        dbCon = SourceFileLoader("configMflos","script/CONFIG/CONFIG_DB/configMflos.py").load_module()
        pct='pct_'+str(Tahun)
        Data = dbCon.DbMflos(query="""select """+pct+""" from MST_DEPRECIATION_MATRIX_MM where area_id='"""+AreaId+"""' 
                                     and item_id='"""+ItemId+"""'  and merk_id='"""+MerkId+"""' 
                                     and series_id='"""+SeriesId+"""'""")
        for data in Data:
            DepHargaOTRMM = data[0]
        return DepHargaOTRMM

    def Search_Asr(self, BranchId, Tenor):
        dbCon = SourceFileLoader("configPmf","script/CONFIG/CONFIG_DB/configPmf.py").load_module()
        Data = dbCon.DbPMF(query="""SELECT b.Tenor, a.InsID AS inscoid, b.ID AS insrateid, b.RateMid
                                     FROM Insurance_Branch_Rate_Type as a with(nolock)        
                                     INNER JOIN ID_RATE_DISKON as b with(nolock) ON a.ID_RATE=b.ID             
                                     WHERE	a.MTS_id = '4'
                                            and a.branchid = '"""+BranchId+"""'        
                                            AND tenor='"""+Tenor+"""'""")
        for data in Data:
            arrayresult = {}
            arrayresult["inscoid"] = data[1]
            arrayresult["insrateid"] = data[2]
            arrayresult["RateMid"] = data[3]
        return arrayresult
        
    def Search_LastNPPNO(self, NPPNO):
        dbCon = SourceFileLoader("configPmf","script/CONFIG/CONFIG_DB/configPmf.py").load_module()
        Data = dbCon.DbPMF(query="""select top 1 NPPNo From cm
                                    inner join Lessee ls on cm.LesseeNo=ls.LesseeNo
                                    where cm.NPPNo is not null 
                                    and ls.LesseeID=(select ls.LesseeID from cm 
                                                     inner join Lessee ls on cm.LesseeNo=ls.LesseeNo
                                                     where NPPNo='"""+NPPNO+"""')
                                    order by cm.DateCreated desc""")
        for data in Data:
            LastNPPNO = data[0]
        return LastNPPNO

    def Search_LoanSeq(self, NPPNO):
        dbCon = SourceFileLoader("configPmf","script/CONFIG/CONFIG_DB/configPmf.py").load_module()
        Data = dbCon.DbPMF(query="""select count(NPPNo)jml From cm
                                    inner join Lessee ls on cm.LesseeNo=ls.LesseeNo
                                    where cm.NPPNo is not null and ls.LesseeID=(select ls.LesseeID from cm 
                                    inner join Lessee ls on cm.LesseeNo=ls.LesseeNo
                                    where NPPNo='"""+NPPNO+"""')""")
        for data in Data:
            LoanSeq = data[0]
        return LoanSeq

    def Search_ASV(self, BranchID, CMOId):
        dbCon = SourceFileLoader("configPmf","script/CONFIG/CONFIG_DB/configPmf.py").load_module()
        Data = dbCon.DbPMF(query="""select ASVCode From ASV_MAPPING_USER
                                    where BranchID='"""+BranchID+"""' and CMOCode='"""+CMOId+"""'""")
        for data in Data:
            ASVCode = data[0]
        return ASVCode
    
    def Search_TujuanPembiayaan(self, Prod, Desc):
        dbCon = SourceFileLoader("configPmf","script/CONFIG/CONFIG_DB/configPmf.py").load_module()
        Data = dbCon.DbPMF(query="""select mtp.tujuan_pembiayaan, mtp.IsPersonal, fvd.param_description From mst_field_values_dtl fvd
                                    inner join master_mapping_tujuan_pembiayaan mtp on fvd.param_value=mtp.tujuan_pembiayaan
                                    where mtp.product_id='"""+Prod+"""' and param_description='"""+Desc+"""'""")
        for data in Data:
            arrayresult = {}
            arrayresult["tujuan_pembiayaan"] = data[0]
            arrayresult["IsPersonal"] = data[1]
            arrayresult["Desc"] = data[2]
        return arrayresult
    