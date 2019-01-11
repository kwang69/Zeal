from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

## init parser
parser = EdinetXbrlParser()

## parse xbrl file and get data container
xbrl_file_path = "./data/jpcrp030000-asr-001_E05663-000_2018-06-30_01_2018-09-19.xbrl"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

## 貸借対照表
key = "jppfs_cor:Assets"
context_ref = "CurrentYearInstant"
current_year_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
print(current_year_assets)