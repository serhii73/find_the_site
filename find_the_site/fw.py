"""Get a website from http://ddg.gg/ ."""
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from typing import List


def get_website(query: str) -> List[str]:
    website_query = f"website {query}"
    headers = {"User-Agent": generate_user_agent()}
    payload = {"q": website_query, "kl": "us-en"}
    response = requests.post(
        "https://duckduckgo.com/lite/", headers=headers, data=payload
    )
    soup = BeautifulSoup(response.text, "html.parser")

    site_list = [link["href"] for link in soup.findAll("a", {"class": "result-link"})]
    return site_list
