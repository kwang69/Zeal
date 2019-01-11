import sys
sys.path.append(r'lib')
from xbrl_proc import read_xbrl
from xbrl_proc import read_xbrl_from_zip
import pandas as pd
from edinet_xbrl.edinet_xbrl_downloader import EdinetXbrlDownloader
import os

def download():
    # init downloader
    xbrl_downloader = EdinetXbrlDownloader()

    ## set a ticker you want to download xbrl file
    ticker = "E05663"
    target_dir = "./data"
    xbrl_downloader.download_by_ticker(ticker, target_dir)

def xbrl2csv():
    # convert xbrl to csv file
    path = './data'
    for filename in os.listdir(path):
        xbrl=r"./data/" + filename
        list = read_xbrl(xbrl)
        df = pd.DataFrame(list)
        df.to_csv('./csv/' + filename[:-5] + ".csv")



print("downloading xbrl files...")
download()
print("downloaded.")
print("converting xbrl files to csv files...")
xbrl2csv()
print("finished.")
