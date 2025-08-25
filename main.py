from loader import load_urls
from selector import select_url
from searcher import search_in_url

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
##sadece yönetimi burdan yapıyoruz