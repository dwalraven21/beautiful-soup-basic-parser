from bs4 import BeautifulSoup
import requests

page = requests.get('https://themanifest.com/web-development/magento/companies')

soup = BeautifulSoup(page.text, "html.parser")

all_headers = soup.find_all('h3')

company_names = []

for header in all_headers:
    if header.find('a'):
        # company_names.append(header.find('a').text)
        company_names.append(header.find('a')['href'])

for company_name in company_names:
    print(str(company_name).strip())