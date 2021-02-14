# 2
import urllib.request as req
# NOTE:url 網址!!!

url="https://www.kkday.com/zh-tw/product/ajax_productlist/?country=&city=&keyword=%E5%8F%B0%E5%8D%97%E5%B8%82&availstartdate=&availenddate=&cat=TAG_4_4&time=&glang=&sort=rdesc&page=1&row=10&fprice=*&eprice=*&precurrency=TWD&csrf_token_name=d840df7741e3cb9df1302c3b8231afeb"
request=req.Request(url, headers={ "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") 
print(data)


# 3
import json 
data=json.loads(data)
print(data)

# 4
posts=data["data"]
print("票券名稱:")
for key in posts:
    title = key["name"]
    print(title)

# 5
print("票券詳細內容連結:")
for key in posts:
    title = key["url"]
    print(title)

# 6
print("票券價格:")
for key in posts:
    title = key["price"]
    print(title)


# 7
print("最早可使用日期:")
for key in posts:
    title = key["earliest_sale_date"]
    print(title)

# 8
print("評價:")
for key in posts:
    title = key["rating_star"]
    print(title)