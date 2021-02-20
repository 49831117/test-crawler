# About Crawler Exercise

> 用 Python 練習爬蟲。

### LV0. HTML
- Web：[臺北市資料大平台](https://data.taipei/#/)
    > 爬取搜尋「[臺北市內湖科技園區廠商名錄](https://data.taipei/#/dataset/detail?id=15c3e1ae-899b-466c-a536-208497e3a369)」的結果
    > 取 API
  - 爬取的結果包含臺北市內湖科技園區各廠商的*公司名稱*、*統一編號*、*公司地址*、*所在經度(ADDR_X)*、*所在緯度(ADDR_Y)*等標籤，可以選擇讀取其中某幾項。
  - 可以選擇是否要將讀取結果存檔。
- [LV0 Taipei Open Data](https://github.com/49831117/test-crawler/blob/master/lv0_taipeiopendata.py)

### LV1. HTML & lV2. cookie
- Web：[批踢踢實業坊](https://www.ptt.cc/bbs/index.html)
- [LV1+2 PTT + cookie](https://github.com/49831117/test-crawler/blob/master/lv1_and_2.py)
  - 可以選擇要讀取的看板的文章標題，以及往前讀取標題的頁數（上一頁）。
  - 一律夾帶 `over18 = 1` 的 cookie。