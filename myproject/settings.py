# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

LOG_LEVEL = 'DEBUG'
BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "myproject (+http://www.yourdomain.com)"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False # 繞過 robots.txt

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
FB_COOKIE = {
    "locale": "=zh_TW",
    "m_pixel_ratio": "=2",
    "wl_cbv": "=v2%3Bclient_version%3A2865%3Btimestamp%3A1752250692",
    "vpd": "=v1%3B845x400x2",
    "c_user": "=61578362034790",
    "dpr": "=1",
    "presence": "=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1752256423157%2C%22v%22%3A1%7D",
    "wd": "=400x845"
}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 進 api
    
    # "authority": "www.facebook.com",
    # "method": "POST",
    # "path": "/api/graphql/",
    # "scheme": "https",
    # "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    # "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6",
    # "content-type": "application/x-www-form-urlencoded",
    # "cookie": 'datr=lFB0aHEDGv0Il2IDD5p2dgqu; ps_l=1; ps_n=1; sb=pVB0aEKs7cakFJ3PhHGP8g6D; c_user=61578362034790; xs=22%3AXaeZJdrLv3UKXA%3A2%3A1752455745%3A-1%3A-1; fr=0RRe2gHEJSr5476ag.AWfwCPzBUiAhMm1_O0s88yX0DZOu2t4xArufiKmJgoxI74et6Cg.BodFDD..AAA.0.0.BodFpC.AWem_4bSD8OZF0G9X6ofLm_yGxE; wd=1046x932; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1752456040337%2C%22v%22%3A1%7D',
    # "origin": "https://www.facebook.com",
    # "priority": "u=1, i",
    # "referer": 'https://www.facebook.com/groups/443709852472133?locale=zh_TW',
    # "sec-ch-prefers-color-scheme": "light",
    # "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    # "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.204", "Chromium";v="131.0.6778.204", "Not_A Brand";v="24.0.0.0"',
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-model": "",
    # "sec-ch-ua-platform": "Linux",
    # "sec-ch-ua-platform-version": "6.8.0",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-origin",
    # "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    # "x-asbd-id": "359341",
    # "x-fb-friendly-name": "GroupsCometFeedRegularStoriesPaginationQuery",
    # "x-fb-lsd": "f9-gUxblGwPI2mz3sATNey", # csrf token
    # "x-requested-with": "XMLHttpRequest",
    # "fb_dtsg": "NAfuBFrimmGNsiZUIjEJuinlX-INsUAHaSEbGKaBt86VHk5rqwaYyDA:22:1752455745",
    

    # 進 fb 頁面
    # "authority": "www.facebook.com",
    # "method": "GET",
    # "path": "/groups/443709852472133",
    # "scheme": "https",
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "accept-encoding": "gzip, deflate, br, zstd",
    # "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6",
    # "cache-control": "max-age=0",
    # "Cookie": 'datr=JTlxaLOpSW9ZLwmgnSp6XppD; locale=zh_TW; ps_l=1; ps_n=1; sb=LzlxaE5Ey1YJYL8bXqE6C9Xw; m_pixel_ratio=2; vpd=v1%3B845x400x2; c_user=61578362034790; ar_debug=1; pas=100003467953862%3Ay4k5uXSetk%2C61578362034790%3Ar82kEUPEPi; wl_cbv=v2%3Bclient_version%3A2868%3Btimestamp%3A1752449880; fbl_st=100636676%3BT%3A29207502; dpr=1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1752450157810%2C%22v%22%3A1%7D; wd=400x845; fr=1yWdvwADLBUTx1f2I.AWcQxZNmjvGJoVot6ZIy78XhpNjY9kZvm0xgEDuvGNE6gdPa0zU.BodExL..AAA.0.0.BodExL.AWeYbFfgiXBh8ueaN9KurnxtGyE; xs=14%3A3__e_Ps4vqIClg%3A2%3A1752254517%3A-1%3A-1%3A%3AAcU3NLMpwhfmF_aw8Xho-YOj_aoYmgb6RvyKNft1pzg',
    # "dpr": "1",
    # "priority": "u=0, i",
    # "referer": "https://www.facebook.com/groups/443709852472133?locale=zh_TW",
    # "sec-ch-prefers-color-scheme": "light",
    # "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    # "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.204", "Chromium";v="131.0.6778.204", "Not_A Brand";v="24.0.0.0"',
    # "sec-ch-ua-mobile": "?1",
    # "sec-ch-ua-model": "Nexus 5",
    # "sec-ch-ua-platform": "Android",
    # "sec-ch-ua-platform-version": "6.0",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    # "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    # "viewport-width": "400",

    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6",
    # "cache-control": "max-age=0",
    # "dpr": "1",
    # "priority": "u=0, i",
    # "sec-ch-prefers-color-scheme": "light",
    # "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    # "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.204\", \"Chromium\";v=\"131.0.6778.204\", \"Not_A Brand\";v=\"24.0.0.0\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-model": "\"\"",
    # "sec-ch-ua-platform": "\"Linux\"",
    # "sec-ch-ua-platform-version": "\"6.8.0\"",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    # "viewport-width": "851",
    # 'Cookie': "datr=JTlxaLOpSW9ZLwmgnSp6XppD; locale=zh_TW; ps_l=1; ps_n=1; sb=LzlxaE5Ey1YJYL8bXqE6C9Xw; m_pixel_ratio=2; vpd=v1%3B845x400x2; c_user=61578362034790; ar_debug=1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1752256423157%2C%22v%22%3A1%7D; wd=400x845; fr=1EbFAalmFTrvl5wHe.AWd1fGl4GrBUdJbtDBpdnKlfEUIBVE8Rb6rEePcHP7V6ePpwYbg.Boc-CC..AAA.0.0.Boc-CC.AWc-GAyK0uSyFrz5nLDiIJ5I4Qw; xs=14%3A3__e_Ps4vqIClg%3A2%3A1752254517%3A-1%3A-1%3A%3AAcUpJU6_YlmRx0WgO_6PCcFAX0Pt-p_mGykzoj2BHUE; dpr=2; pas=100003467953862%3Ay4k5uXSetk%2C61578362034790%3Ar82kEUPEPi; fbl_st=100626814%3BT%3A29207076; wl_cbv=v2%3Bclient_version%3A2868%3Btimestamp%3A1752424580"
    # # "Cookie": "c_user=61578362034790; xs=14%3A3__e_Ps4vqIClg%3A2%3A1752254517%3A-1%3A-1%3A%3AAcUpJU6_YlmRx0WgO_6PCcFAX0Pt-p_mGykzoj2BHUE; "
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "myproject.middlewares.MyprojectSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "myproject.middlewares.MyprojectDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "myproject.pipelines.MyprojectPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
