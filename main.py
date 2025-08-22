import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Style, init

# Windows terminalde renk desteği için
init(autoreset=True)

DROP_TAGS = {"script", "style", "nav", "footer", "header", "noscript", "aside", "form", "svg"}
KEEP_TAGS = {"title", "h1", "h2", "h3", "p", "li", "a"}

def load_urls(file_path="urls.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def select_url(urls):
    print("\nMevcut URL Listesi:\n")
    for i, url in enumerate(urls, 1):
        print(f"{i}. {url}")
    while True:
        try:
            n = int(input("\nHangi URL'de arama yapmak istiyorsun? (numara): "))
            if 1 <= n <= len(urls):
                return urls[n-1]
        except ValueError:
            pass
        print("Geçerli bir numara gir!")

def cleanup_html(soup: BeautifulSoup):
    for tag in list(soup.find_all(DROP_TAGS)):
        tag.decompose()
    return soup

def visible_text_nodes(soup: BeautifulSoup):
    for tag in soup.find_all(KEEP_TAGS):
        text = tag.get_text(" ", strip=True)
        if text:
            yield text

def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

def split_sentences(text: str):
    """ Noktalama işaretlerine göre cümleleri böl ve işaretleri koru """
    sentences = re.findall(r'[^.!?]*[.!?]', text, re.MULTILINE | re.DOTALL)
    return [normalize_spaces(s) for s in sentences if s.strip()]

def highlight(sentence: str, keyword: str) -> str:
    pat = re.compile(re.escape(keyword), re.IGNORECASE)
    return pat.sub(lambda m: Fore.RED + Style.BRIGHT + m.group(0) + Style.RESET_ALL, sentence)

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
        print(f"\n❌ '{keyword}' kelimesi bulunamadı.")
        return

    print(f"\n✅ '{keyword}' kelimesi bulundu. Geçtiği cümleler:\n")
    for i, s in enumerate(sentences, 1):
        print(f"{i}. {highlight(s, keyword)}")

def main():
    urls = load_urls("urls.txt")
    if not urls:
        print("URL listesi boş!")
        return
    selected = select_url(urls)
    keyword = input("Aramak istediğin kelimeyi gir: ").strip()
    if not keyword:
        print("Anahtar kelime boş olamaz!")
        return
    search_in_url(selected, keyword)

if __name__ == "__main__":
    main()
