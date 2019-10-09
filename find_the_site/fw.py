"""
Get a website from http://ddg.gg/            [default]
or
Get a website from https://www.ecosia.org/          [optional]
(to plant trees)
"""
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


def get_website(need_website=None, eco=False):
    """Return a website."""

    website = None
    ua = generate_user_agent()
    headers = {"User-Agent": ua}

    if eco:
        # Find website with ecosia to plant trees yay!!!
        url = "https://www.ecosia.org/search?"
        words = need_website.split(" ")
        query = "q=website"
        for w in words:
            query += "+" + str(w)
        url = url + query
        r = requests.get(url, headers=headers)
    else:
        # Find website with duckduckgo [default]
        find_website_ddg = "website " + need_website
        url = "https://duckduckgo.com/lite/"
        payload = {"q": find_website_ddg, "kl": "us-en"}
        r = requests.post(url, headers=headers, data=payload)

    soup = BeautifulSoup(r.text, "html.parser")

    if eco:
        website_list = [
            i.get("href") for i in soup.find_all("a", {"class", "result-url js-result-url"})
        ]
    else:
        website_list = [
            i.get("href") for i in soup.find_all("a", {"class", "result-link"})
        ]
    if website_list:
        website = website_list[0]
    return website_list