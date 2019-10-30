# -*- coding: utf-8 -*-
#
# Scrapy settings for ke project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ke'

SPIDER_MODULES = ['ke.spiders']
NEWSPIDER_MODULE = 'ke.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ke.middlewares.KeSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'ke.middlewares.KeDownloaderMiddleware': 543,
#     # 'ke.cookiesmiddlewares.CookiesMiddleware': 544,
# }
# cookie池
COOKIES = [{
        'kr_stat_uuid': 'kwWWS26064183',
        'device-uid': '4442aef0-b723-11e9-84b5-639540c9b49f',
        'download_animation': '1',
        'krnewsfrontss': '3583db26833583b5e4e715e5248353fe',
        'M-X SRF-TOKEN': 'f36de0663a9f2fa96262335cd2208ecdd4ce2d2fa2f00d7ce91bfb76324a5a6f',
        'Hm_lvt_713123c60a0e86982326bae1a51083e1': '1569544443,1571383333,1571618227',
        'Hm_lvt_1684191ccae0314c6254306a8333d090': '1569544443,1571383333,1571618227',
        'ktm_source': 'kaike_pclandingpage',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22kwWWS26064183%22%2C%22%24device_id%22%3A%2216d2459296ba90-0eac3c4df477f2-c343162-2073600-16d2459296c617%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216d2459296ba90-0eac3c4df477f2-c343162-2073600-16d2459296c617%22%7D',
        'Hm_lpvt_713123c60a0e86982326bae1a51083e1': '1571618311',
        'Hm_lpvt_1684191ccae0314c6254306a8333d090': '1571618311',
        'Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3': '1571618356',
        'Hm_lpvt_e8ec47088ed7458ec32cde3617b23ee3': '1571618356',
        ' _kr_p_se': 'c663ef9c-5185-414e-841e-8f8f6005fc22',
        'krid_user_id': '941851778',
        ' krid_user_version': '2',
        'kr_plus_id': '941851778',
        'kr_plus_token': '3sYTEv7AwXzMT6Iii6znd8JijrYmEt76844_____',
    }, {
        'Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3': '1571618356, 1572250344',
        'Hm_lpvt_e8ec47088ed7458ec32cde3617b23ee3': '1572250344',
        'download_animation': '1',
        '_kr_p_se': '3e73b0eb-29f5-47da-a24d-124894f3e31e',
        'krid_user_id': '928483838',
        'krid_user_version': '2',
        'kr_plus_id': '928483838',
        'kr_plus_token': 'UBcNvsprbWs4DydTkHOlZ11NSkgu3925122_____',
    }]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'ke.pipelines.KePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_LEVEL = "WARNING"
