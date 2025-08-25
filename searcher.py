import re
import requests
from bs4 import BeautifulSoup
from html_utils import cleanup_html, visible_text_nodes
from text_utils import split_sentences
from highlighter import highlight

def find_sentences_with_keyword(html: str, keyword: str):
    soup = BeautifulSoup(html, "html.parser")
    cleanup_html(soup)

    matches = []
    for block in visible_text_nodes(soup):
        for sent in split_sentences(block):
            if re.search(re.escape(keyword), sent, re.IGNORECASE):
                matches.append(sent)

    # Tekrarları temizle
    seen, unique = set(), []
    for s in matches:
        key = s.lower()
        if key not in seen:
            seen.add(key)
            unique.append(s)
    return unique

def search_in_url(url: str, keyword: str):
    try:
        resp = requests.get(url, timeout=15)
    except Exception as e:
        print(f"İstek hatası: {e}")
        return

    if resp.status_code != 200:
        print(f"Sayfa çekilemedi! HTTP {resp.status_code}")
        return

    sentences = find_sentences_with_keyword(resp.text, keyword)
    if not sentences:
        print(f"\n '{keyword}' kelimesi bulunamadı.")
        return

    print(f"\n '{keyword}' kelimesi bulundu. Geçtiği cümleler:\n")
    for i, s in enumerate(sentences, 1):
        print(f"{i}. {highlight(s, keyword)}")
#seçilen url ye istek atıyor ve arama yapıyor 