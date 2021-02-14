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


web = input("ptt website:")
over18 = input("need over 18 cookie? (Y/N)").lower()

if over18 =="n":
    gettitle(web)
else:
    gettitle18(web)