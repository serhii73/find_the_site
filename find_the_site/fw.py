"""Get a website from http://ddg.gg/ ."""
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from functools import lru_cache


@lru_cache(maxsize=1024)
def get_website(need_website=None):
    """Return a website."""
    website = None
    if need_website:
        # Find website
        find_website_ddg = "website " + need_website
        ua = generate_user_agent()
        headers = {"User-Agent": ua}
        payload = {"q": find_website_ddg, "kl": "us-en"}
        r = requests.post("https://duckduckgo.com/lite/", headers=headers, data=payload)
        soup = BeautifulSoup(r.text, "html.parser")
        website_list = [
            i.get("href") for i in soup.find_all("a", {"class", "result-link"})
        ]
        if website_list:
            website = website_list[0]
    return website_list
