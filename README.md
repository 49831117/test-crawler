# About Crawler Exercise

> 用 Python 練習爬蟲。

### LV0. HTML
- Web：[臺北市資料大平台](https://data.taipei/#/)
  > - 爬取搜尋「[臺北市內湖科技園區廠商名錄](https://data.taipei/#/dataset/detail?id=15c3e1ae-899b-466c-a536-208497e3a369)」的結果
  > - 取 API
- [LV0 Taipei Open Data](https://github.com/49831117/test-crawler/blob/master/lv0_taipeiopendata.py)
  > 自我延伸的巧思：
  > 1. 爬取的結果包含臺北市內湖科技園區各廠商的*公司名稱*、*統一編號*、*公司地址*、*所在經度(ADDR_X)*、*所在緯度(ADDR_Y)* 等標籤，可以選擇讀取其中某幾項。
  > 2. 可以選擇是否要將讀取結果存檔。

### LV1. HTML & lV2. cookie
- Web：[批踢踢實業坊](https://www.ptt.cc/bbs/index.html)
- [LV1 PTT](https://github.com/49831117/test-crawler/blob/master/lv1_ptt.py)
  > - 僅嘗試爬取某看板第一頁的文章標題。
  > - 無法爬取需要滿 18 歲的看板名稱。
- [LV1+2 PTT + cookie](https://github.com/49831117/test-crawler/blob/master/lv1_and_2.py)
  > 自我延伸的巧思：
  > 1. 一律夾帶 `over18=1` 的 cookie
  > 2. 可以選擇要讀取的看板名稱
  > 3. 可以自選要往前讀取的頁數


### LV3 AJAX
