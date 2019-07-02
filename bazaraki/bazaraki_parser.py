import requests
from bs4 import BeautifulSoup as bs


def bazaraki_parser(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        ad_dict = dict()
        ad_url_beg = 'https://www.bazaraki.com'
        divs = soup.find_all('div', 'list-announcement-block')
        for div in divs:
            date = div.find('div','announcement-block__date').text.strip()[:12]
            if 'Today' in date:
                href = div.find('a', 'announcement-block__title')['href']
                title = div.find('a', 'announcement-block__title').text
                title = title.split('\n')[1].strip()
                ad_dict[str(title)] = ad_url_beg + href
        return ad_dict
