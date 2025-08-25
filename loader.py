def load_urls(file_path="urls.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
##Bu fonks urls txt dosyasını okumak için var