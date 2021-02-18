import urllib.request as request
import bs4


def gettitle(src):
    requestUA = request.Request(src, headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
        })
    with request.urlopen(requestUA) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")    
    titles = root.find_all("div", class_ = 'title') # 尋找所有 class = "title" 的標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink = root.find("a", string="‹ 上頁") #找到<a>的內文為「‹ 上頁」的部份
    return nextLink["href"] #抓取搜尋目標的屬性：使用["屬性名稱"]，抓取href屬性，return 丟回程式的外面

def gettitle18(src):
    requestUA = request.Request(src, headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'cookie' : "over18=1"
        })
    with request.urlopen(requestUA) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")    
    titles = root.find_all("div", class_ = 'title') # 尋找所有 class = "title" 的標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]    


web = input("\nptt 看板名稱 (eg. Gossiping、Stock):\n ").lower()
over18 = input("Need over \"18 cookie\"? (Y/N)\n ").lower()
page = int(input("How many pages of titles do you want? (eg. 2)\n "))

web = f"bbs/{web}/index.html"
src = f"https://www.ptt.cc/{web}"

print()
count = 0

if over18 =="n":
    while count < page:
        print(f"\n第 {count+1} 頁\n")
        src = f"https://www.ptt.cc{gettitle(src)}"
        count+=1 

else:
    while count < page:
        print(f"\n第 {count+1} 頁\n")
        src = f"https://www.ptt.cc{gettitle18(src)}"
        count+=1

