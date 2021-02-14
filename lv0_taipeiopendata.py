import urllib.request as request
import json

'''
延伸：
1. 將 api 取得之資料做使用者查詢優化
公司地址  ADDR_X   ADDR_Y  ﻿統編  公司名稱

2. 是否將爬取資料存成純文字檔
'''

print("爬取資料來源：臺北市資料大平台 - 內湖科技園區廠商名錄")
src = 'https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'

# 讀取網頁資料試試看
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")
# print(data)

# 使用 JSON 讀取檔案
with request.urlopen(src) as response:
    data=json.load(response)#使用JASON格式讀取 
# print(data)
clist = data["result"]["results"] 


choose_data = input("欲爬取之資料：\n1. 公司名稱  2. 統一編號  3. 公司地址  4. 所在經度(ADDR_X)  5. 所在緯度(ADDR_Y) \n（請直接輸入代號並用「,」格開，如: 1,2,3 或 1,3）\n").split(",")
list = ["公司名稱", "\ufeff統編", "公司地址", "ADDR_X", "ADDR_Y"] 


for company in clist:
    for i in choose_data:
        # 印出觀察
        print(list[int(i)-1], ":", company[list[int(i)-1]])
        #print(company[wantknow])
    print("\n")





# write_or_not = input("是否將搜尋結果存成文字檔？（Y/N）\n").upper()

# if write_or_not == "Y":
#     with open("data.txt","w",encoding="utf-8") as file: # w, r
#         for company in clist:
#             for i in choose_data:
#                 # 印出觀察
#                 file.write(list[int(i)-1], ":", company[list[int(i)-1]])
#                 print(list[int(i)-1], ":", company[list[int(i)-1]])
#                 #print(company[wantknow])
#             print("\n")
# else:
#     for company in clist:
#         for i in choose_data:
#             # 印出觀察
#             print(list[int(i)-1], ":", company[list[int(i)-1]])
#             #print(company[wantknow])
#         print("\n")
