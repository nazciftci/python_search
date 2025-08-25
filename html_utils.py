from bs4 import BeautifulSoup
from config import DROP_TAGS, KEEP_TAGS

def cleanup_html(soup: BeautifulSoup):
    for tag in list(soup.find_all(DROP_TAGS)):
        tag.decompose()
    return soup

def visible_text_nodes(soup: BeautifulSoup):
    for tag in soup.find_all(KEEP_TAGS):
        text = tag.get_text(" ", strip=True)
        if text:
            yield text
## metin işliyor.