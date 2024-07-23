from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options

# ...

def __init__(self, domain=None, *args, **kwargs):
    super(LegalEmailSpider, self).__init__(*args, **kwargs)
    if domain:
        self.allowed_domains = [domain]
        self.start_urls = [f'https://www.{domain}']
    # Configuration de Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    
    # Utiliser Chromium
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
