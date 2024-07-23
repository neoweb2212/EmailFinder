BOT_NAME = 'legal_email_scraper'

SPIDER_MODULES = ['scrapy_project.spiders']
NEWSPIDER_MODULE = 'scrapy_project.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   'scrapy_project.pipelines.EmailValidationPipeline': 300,
}
