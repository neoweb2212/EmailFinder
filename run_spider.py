from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_project.spiders.legal_email_spider import LegalEmailSpider

def run_spider(domain):
    settings = get_project_settings()
    settings.update({
        'DEPTH_LIMIT': 3,
        'CLOSESPIDER_PAGECOUNT': 100,
        'LOG_LEVEL': 'WARNING',
        'DOWNLOAD_DELAY': 3,  # Délai de 3 secondes entre les requêtes
        'RANDOMIZE_DOWNLOAD_DELAY': True
    })
    process = CrawlerProcess(settings)
    process.crawl(LegalEmailSpider, domain=domain)
    process.start()

if __name__ == "__main__":
    domain = "randomlists.com"
    run_spider(domain)
