import httpx

BASE_URL = "https://openlibrary.org"

def fetch_book_info(isbn: str):
    """
    Open Library API'den kitap bilgilerini alır.
    Başarılı olursa {title, author, isbn} dict döner.
    Hata olursa None döner.
    """
    try:
        url = f"{BASE_URL}/isbn/{isbn}.json"
        response = httpx.get(url, timeout=10.0)
        
        # 4xx veya 5xx durumunda hata fırlatır
        response.raise_for_status() 

        data = response.json()
        title = data.get("title", "Bilinmeyen Başlık")

        # Yazar bilgilerini çekme
        author_names = []
        if "authors" in data:
            for author in data["authors"]:
                author_key = author.get("key")
                if author_key:
                    try:
                        author_url = f"{BASE_URL}{author_key}.json"
                        author_response = httpx.get(author_url, timeout=5.0)
                        author_response.raise_for_status()
                        author_data = author_response.json()
                        author_names.append(author_data.get("name", "Bilinmeyen Yazar"))
                    except (httpx.RequestError, httpx.HTTPStatusError):
                        author_names.append("Bilinmeyen Yazar")
        
        author_str = ", ".join(author_names) if author_names else "Bilinmeyen Yazar"

        return {
            "title": title,
            "author": author_str,
            "isbn": isbn
        }

    except httpx.HTTPStatusError as e:
        # Kitap bulunamadı (404) gibi durumlar için hata mesajı
        print(f"⚠️ API hatası: Kitap bilgisi bulunamadı. Durum kodu: {e.response.status_code}")
        return None
    except httpx.RequestError:
        # İnternet bağlantısı yok veya DNS hatası gibi durumlar için hata mesajı
        print("⚠️ Ağ hatası: API'ye bağlanılamadı.")
        return None
    except Exception as e:
        # Diğer beklenmeyen hatalar için genel bir mesaj
        print(f"⚠️ Beklenmeyen bir hata oluştu: {e}")
        return None