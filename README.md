# 爬蟲作業 爬FB貼文

## 題目
請收錄以下臉書社團近三個月的貼文及留言，並以restful api的方式提供給我們進行呼叫。
回傳的欄位包含 : 類型(主文/留言)、內容、時間、發文者/留言者。
https://www.facebook.com/groups/443709852472133?locale=zh_TW

## 預期格式
```json
{
    "type": "主文/留言 (先只保留主文)",
    "content": "內容",
    "post_time": "發文時間",
    "author": "留言者"
    "url": "連結 (方便我檢查)"
    "comments": [
        {
            "content": "留言內容",
            "post_time": 1752419048000,
            "author": "留言的人"
        }
    ]
}
```

## 使用步驟
```
git clone <本篇>

# 安裝環境
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 執行
scrapy crawl example
```

## 使用前備註
- 主要執行的檔案 `/myproject/myproject/spiders/example.py`
    - 執行前，請先將 ookies, headers, payload 更換成自己的
    - 可以設定翻頁上限, 時間區間
- 沒有實做自動化，因為有太多參數需要進瀏覽器取得，所以仍須手動運作



