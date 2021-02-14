# import urllib.request as request
# # import json

# # HTML
# web = input("website:")
# src = web
# requestUA = request.Request(src, headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
# })

# with request.urlopen(requestUA) as response:
#     data = response.read().decode("utf-8") #使用JASON格式讀取 
# # print(data)

# import bs4
# # 讓 BeautifalSoup 解析 HTML 格式文件
# root = bs4.BeautifulSoup(data, "html.parser")
# # print(root) # 印出觀察
# # print(root.title) # 印出"title"標籤
# # print(root.title.string) # 印出"title"標籤中的字串

# titles = root.find("div", class_="title") #尋找class="title"的div標籤
# # print(titles) 
# # print(titles.div) 

# titles = root.find_all("div", class_ = 'title') # 尋找所有 class = "title" 的標籤
# for title in titles:
#     print(title.a.string)


# 或是用 def 做
import urllib.request as request
import bs4

def gettitle(web):
    src = web
    requestUA = request.Request(src, headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
        })
    with request.urlopen(requestUA) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")    
    titles = root.find_all("div", class_ = 'title') # 尋找所有 class = "title" 的標籤
    for title in titles:
        print(title.a.string)
web = input("ptt website:")
gettitle(web)