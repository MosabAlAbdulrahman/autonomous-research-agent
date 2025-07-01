from bs4 import BeautifulSoup
import requests

def scrape_techcrunch_ai_articles():
    url = "https://techcrunch.com/tag/artificial-intelligence/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for article in soup.find_all("a", class_="post-block__title__link")[:5]:
        articles.append({
            "title": article.get_text(strip=True),
            "url": article["href"]
        })
    return articles
