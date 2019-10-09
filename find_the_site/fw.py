"""Get a website from http://ddg.gg/ ."""
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from typing import List
from functools import lru_cache

@lru_cache(maxsize=1024)
def get_website(query: str, eco: False) -> List[str]:
    headers = {"User-Agent": generate_user_agent()}
    if eco:
        # Find website with ecosia to plant trees yay!!!
        url = "https://www.ecosia.org/search?"
        words = query.split(" ")
        query = "q=website"
        for w in words:
            query += "+" + str(w)
        url = url + query
        response = requests.get(url, headers=headers)
    else:
        website_query = f"website {query}"

        payload = {"q": website_query, "kl": "us-en"}
        response = requests.post(
            "https://duckduckgo.com/lite/", headers=headers, data=payload
        )
    soup = BeautifulSoup(response.text, "html.parser")

    if eco:
        site_list = [link["href"] for link in soup.findAll("a", {"class": "result-url js-result-url"})]

    else:
        site_list = [link["href"] for link in soup.findAll("a", {"class": "result-link"})]

    return site_list
