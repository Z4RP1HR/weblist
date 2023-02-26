import requests
from bs4 import BeautifulSoup

def get_websites(country):
    url = f"https://www.alexa.com/topsites/countries/{country}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    sites = soup.find_all('div', class_='tr site-listing')
    websites = []
    for i, site in enumerate(sites):
        if i == 50:
            break
        website = site.find('div', class_='td DescriptionCell').find('a').get_text()
        websites.append(website)
    return websites

country = input("Enter a country: ")
websites = get_websites(country)
print(f"Top 50 websites in {country}:")
for i, website in enumerate(websites):
    print(f"{i+1}. {website}")
