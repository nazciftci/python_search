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
##kullanıcıya hangi urli seçmek istediğini soruyor.