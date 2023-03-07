# Date： 2023/02/20
# Introduction：資料擷取最終版

import os
import requests
import csv
import json
import pandas as pd
import time

start_time = time.time()
print(start_time)
print("======================================")
# df = pd.read_csv('/Users/wood/Desktop/UXLab/BNX/')
file_dir = "/Users/wood/Desktop/UXLab/Era7-26/26"  # 數字改這裡！！！！      file directory改這裡
all_csv_list = os.listdir(file_dir)  # get csv list
for single_csv in all_csv_list:
    df = pd.read_csv(os.path.join(file_dir, single_csv))
    print(single_csv)


df = df.iloc[:,1]
df_list = df.values.tolist()
data_list = []

for items in df_list:
    url = "https://api.bscscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=751CDDEMJGZMZ13SHPAFCKPI4842V6SIG4".format(items)
    response = requests.get(url)
    data = json.loads(response.text)
    if not data['result']:
        print(f"No data returned for {items}, stopping the loop.")
        break

    data_list.extend(data['result'])

#！！！這裡記得要改文件名字！！！
    with open('Era7-UA.csv', 'a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["timeStamp", "from", "to", "value", "isError", "methodId", "functionName"])
      for item in data_list:
            writer.writerow([item['timeStamp'], item['from'], item['to'], item['value'], item['isError'], item['methodId'], item['functionName']])

    csv_output = '/Users/wood/Desktop/UXLab/Era7-26/Era7-UA.csv'
print(csv_output)
print("======================================")
print("ok!!")

end_time = time.time()
print(end_time)
duration = end_time - start_time
print(f"程式執行時間為 {duration:.2f} 秒")

import os
os.system('say "hey baby kiss my ass"')