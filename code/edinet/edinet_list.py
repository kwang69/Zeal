from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser
import pandas as pd
## init parser
parser = EdinetXbrlParser()

## parse xbrl file and get data container
xbrl_file_path = "./data/jpcrp030000-asr-001_E05663-000_2018-06-30_01_2018-09-19.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

## 貸借対照表
# names =['現預金等','売上債権','棚卸資産','その他流動資産','有形固定資産','無形固定資産','投資その他','買掛債務','有利子負債（流動と固定）','その他流動負債','その他固定負債','純資産']
list_ref=[]
list_ref.insert(0,['貸借','科目1','科目2','科目3','数値'])
list2 = ['流動資産','流動資産','流動資産','流動資産','固定資産','固定資産','固定資産','流動負債','流動負債','流動負債','固定負債','純資産']
list1 = ['資産','資産','資産','資産','資産','資産','資産','負債','負債','負債','負債','純資産']
list0 = ['借方','借方','借方','借方','借方','借方','借方','借方','貸方','貸方','貸方','貸方','貸方']
name_list = ['現預金等','売上債権','棚卸資産','その他流動資産','有形固定資産','無形固定資産','投資その他','買掛債務','有利子負債（流動と固定）','その他流動負債','その他固定負債','純資産']
tag_list = ['CashAndCashEquivalentsSummaryOfBusinessResults','NotesAndAccountsReceivableTrade','?','?','?','?','?','?','?','CurrentLiabilities','NoncurrentLiabilities','NetAssets']
context_list = ['CurrentYearInstant','CurrentYearInstant','?','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant','CurrentYearInstant']
cor_list = ["jpcrp_cor:","jppfs_cor:","?","jppfs_cor:","jpcrp_cor:","jpcrp_cor:","jpcrp_cor:","jpcrp_cor:","jpcrp_cor:","jppfs_cor:","jppfs_cor:","jppfs_cor:"]
for i in range(12):
    if tag_list[i] == '?':
        current_value = 0
    # elif i == 3:
    #     key = cor_list[i] + tag_list[i]
    #     context_ref = context_list[i]
    #     current_value = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    #     current_value = int(current_value) - (int(list_ref[1][4]) + int(list_ref[2][4]))
    else:
        key = cor_list[i] + tag_list[i]
        context_ref = context_list[i]
        current_value = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    list_ref += [[list0[i],list1[i],list2[i],name_list[i],current_value]]
df = pd.DataFrame(list_ref)
df.to_csv('./' + "貸借対照表" + ".csv")

## 損益計算書
list_balance=[]
name_list = ['売上原価','販管費','営業利益','売上']
tag_list = ['CostOfSales','SellingGeneralAndAdministrativeExpenses','OperatingIncome']
list_balance.insert(0,['売上原価','販管費','営業利益','売上'])
cor_list = ["jppfs_cor:",'jppfs_cor:','jppfs_cor:']
value_list = []
for i in range(3):
    key = cor_list[i] + tag_list[i]
    context_ref = "CurrentYearDuration"
    current_value = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    value_list += [current_value]
value_list += [int(value_list[0])+int(value_list[1])+int(value_list[2])]
list_balance.insert(1,value_list)
list_balance.insert(1,[1,1,1,2])
list_balance = list(map(list, zip(*list_balance)))
df = pd.DataFrame(list_balance)
df.to_csv('./' + "損益計算書" + ".csv")

## キャッシュフロー計算書
list_cf=[]
name_list = ['営業CF','投資CF','財務CF']
tag_list = ['NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults','NetCashProvidedByUsedInInvestmentActivities','NetCashProvidedByUsedInFinancingActivities']
list_cf.insert(0,['営業CF','投資CF','財務CF'])
cor_list = ["jpcrp_cor:",'jppfs_cor:','jppfs_cor:']
value_list = []
for i in range(3):
    key = cor_list[i] + tag_list[i]
    context_ref = "CurrentYearDuration"
    current_value = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
    value_list += [current_value]
list_cf.insert(1,value_list)
df = pd.DataFrame(list_cf)
df.to_csv('./' + "キャッシュフロー計算書" + ".csv")