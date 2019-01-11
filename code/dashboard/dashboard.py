import requests
import csv
import json
import pandas as pd

modifiedFrom = "00010101"
print("統計メタ情報（系列）取得開始")
url ="https://dashboard.e-stat.go.jp/api/1.0/Csv/getIndicatorInfo?Lang=JP&modifiedFrom=" + modifiedFrom
with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    df = pd.DataFrame(my_list)
    df.to_csv('./統計メタ情報/' + "統計メタ情報（系列）取得" + ".csv")
print("統計メタ情報（系列）取得完了")

print("統計メタ情報（地域）取得開始")
url ="https://dashboard.e-stat.go.jp/api/1.0/Csv/getRegionInfo?Lang=JP&modifiedFrom=" + modifiedFrom
with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    df = pd.DataFrame(my_list)
    df.to_csv('./統計メタ情報/' + "統計メタ情報（地域）取得" + ".csv")
print("統計メタ情報（地域）取得完了")

print("統計データ取得開始")

# excel = pd.read_excel('提供データ一覧_島村編集.xlsx',sheet_name = "取得するデータ", usecols = [2,3,4,5,6,7,8,9,10], skiprows = [1,2])
excel = pd.read_csv('ID.csv', keep_default_na = False, na_values=None,encoding="UTF-8", dtype = 'object')
my_list = []

for number in excel.iloc[:,0]:
    # if len(str(number)) == 19:
    #     url ="https://dashboard.e-stat.go.jp/api/1.0/Csv/getData?Lang=JP&IndicatorCode=" + str(number) + "&modifiedFrom=" + modifiedFrom
    # else:
    #     my_list.insert(-1,[])
    #     continue
    # with requests.Session() as s:
    #     download = s.get(url)
    #     decoded_content = download.content.decode('utf-8')
    #     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    #     my_list.insert(-1,list(cr)[-1])
    # df = pd.DataFrame(my_list)
    # df.to_csv('./csv/' + "統計データ取得" + ".csv")
    # print("統計データ取得完了")
    if len(str(number)) == 19:
        url ="https://dashboard.e-stat.go.jp/api/1.0/Csv/getData?Lang=JP&IndicatorCode=" + str(number) + "&modifiedFrom=" + modifiedFrom + "&RegionLevel=3"
    else:
        continue
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        df = pd.DataFrame(my_list)
        df.to_csv('./csv/' + str(number) + ".csv")
print("統計データ取得完了")