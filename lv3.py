'''
跑不動
'''
import urllib.request as request
import bs4

def gettitle18(web):
    src = web
    requestUA = request.Request(src, headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'cookie' : "over18=1"
        })
    with request.urlopen(requestUA) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")    
    titles = root.find_all("div", class_ = 'title') # 尋找所有 class = "title" 的標籤
    for title in titles:
        print(title.a.string)
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["herf"]

web = input("ptt website:")
nextpage = "https://www.ptt.cc/"+gettitle18(web)
print(nextpage)