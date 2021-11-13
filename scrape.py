import requests
from bs4 import BeautifulSoup
import pprint


def get_scrape_urls():
    base_url = 'https://news.ycombinator.com/news?p='
    url_list = []
    for page in range(1, 3):
        url = base_url + str(page)
        url_list.append(url)
    return url_list


def get_html_data(urls_list):
    # print(urls_list)
    links_total = []
    subtext_total = []
    for url in urls_list:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titlelink')
        subtext = soup.select('.subtext')
        links_total += links
        subtext_total += subtext
    return (links_total, subtext_total)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def main():
    urls = get_scrape_urls()
    links, subtext = get_html_data(urls)
    my_hacker_news = create_custom_hn(links, subtext)
    print(my_hacker_news)


if __name__ == '__main__':
    main()
