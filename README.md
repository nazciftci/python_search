# Terminal Web Search Tool

Bu proje, terminal üzerinden web sayfalarında belirli bir kelimeyi aramanıza olanak sağlayan basit bir Python aracıdır. HTML içeriğini temizler, cümlelere böler ve aranan kelimeyi vurgulayarak kullanıcıya gösterir.

---

** Özellikler**

- URL listesinden seçim yapabilme
- HTML içeriğini temizleyerek gereksiz etiketleri atlama (`script`, `style`, `nav`, vb.)
- Yalnızca önemli içerikleri (`title`, `h1`, `h2`, `h3`, `p`, `li`, `a`) tarama
- Cümlelere bölerek arama yapma
- Terminalde aranan kelimeyi kırmızı ve parlak olarak vurgulama
- Tekrarlayan cümleleri temizleyerek yalnızca benzersiz sonuçları gösterme
- Basit ve anlaşılır terminal arayüzü

---

**Gereksinimler**
- Python 3.8 veya üzeri
- Kütüphaneler:
  - `requests`
  - `beautifulsoup4`
  - `colorama`


