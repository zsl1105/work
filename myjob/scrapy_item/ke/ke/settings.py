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
import datetime

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
    'acw_tc': 'b65cfd3715725691802323962e3f6ee12b2de1f0bc9d0a702bf981b83dc1bc',
    '_kr_p_se': '51bb9d3a-ddeb-46d6-bd05-8f32fe12dff6',
    'krid_user_id': '941851778',
    'krid_user_version': '2',
    'kr_plus_id': '941851778',
    'kr_plus_token': 'SFj8s9QTkEW6F9A33WCxV_PKBJy33czv5ts2____',
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

# 配置loging日志
to_day = datetime.datetime.now()
LOG_FILE = "log/scrapy_{}_{}_{}".format(to_day.year, to_day.month, to_day.day)
LOG_LEVEL = "WARNING"
