# Création de la structure principale
mkdir -p email_scraper/{scrapy_project/{spiders,},api/{routes,utils},config,tests,data,scripts,docs}

# Création des fichiers dans scrapy_project
touch email_scraper/scrapy_project/{items.py,middlewares.py,pipelines.py,settings.py,link_extractors.py}
touch email_scraper/scrapy_project/spiders/{legal_email_spider.py,__init__.py}

# Création des fichiers dans api
touch email_scraper/api/{main.py,__init__.py}
touch email_scraper/api/routes/{domain_scrape.py,__init__.py}
touch email_scraper/api/utils/{email_validator.py,domain_checker.py,__init__.py}

# Création des fichiers de configuration
touch email_scraper/config/{config.yml,proxy_list.txt}

# Création des fichiers de test
touch email_scraper/tests/{test_legal_email_spider.py,__init__.py}

# Création du fichier de base de données (vide)
touch email_scraper/data/scraped_emails.db

# Création des scripts
touch email_scraper/scripts/{setup_vps.sh,deploy_api.sh}

# Création de la documentation
touch email_scraper/docs/README.md

# Création des fichiers à la racine du projet
touch email_scraper/{requirements.txt,docker-compose.yml}