# Python 202 Bootcamp Projesi

# 📚 FastAPI Pylibrary

Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirilmiş, üç aşamalı bir kütüphane yönetim sistemidir. Uygulama, komut satırı arayüzü (CLI) olarak başlar, harici bir API ile zenginleştirilir ve son olarak modern bir web servisi haline getirilir.

## 🌟 Özellikler

- **Terminal Uygulaması:** Kullanıcı dostu, interaktif bir komut satırı arayüzü ile kitap ekleme, silme, listeleme ve arama işlemleri.
- **API Entegrasyonu:** Open Library API üzerinden ISBN'e göre kitap bilgilerini otomatik olarak çeker.
- **Hata Yönetimi:** API bağlantı hataları, bulunamayan kitaplar ve diğer istisnalar için sağlam hata yakalama mekanizması.
- **Veri Kalıcılığı:** Kütüphanedeki kitaplar `library.json` dosyasına kaydedilir ve uygulama her başlatıldığında yüklenir.
- **RESTful API:** FastAPI kullanılarak HTTP üzerinden erişilebilen, tam özellikli bir web servisi.
- **Otomatik Dokümantasyon:** OpenAPI ve Swagger UI ile otomatik olarak oluşturulan interaktif API dokümantasyonu.

## 🚀 Proje Aşamaları

1.  **Aşama 1 (OOP):** `Book` ve `Library` sınıfları ile nesne yönelimli temel kütüphane mantığı oluşturuldu.
2.  **Aşama 2 (API Entegrasyonu):** `api_utils.py` ile Open Library API'ye bağlanarak kitap verileri zenginleştirildi.
3.  **Aşama 3 (FastAPI):** `api.py` dosyası ile projenin işlevselliği, bir web servisi olarak sunuldu.

## 🛠️ Kurulum

Projenin bağımlılıklarını kurmak ve yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler

- Python 3.8+
- Git

### Adımlar

1.  **Repoyu Klonlama**
    ```bash
    git clone [https://github.com/ozlemeker/FastAPI-Pylibrary.git](https://github.com/ozlemeker/FastAPI-Pylibrary.git)
    cd FastAPI-Pylibrary
    ```

2.  **Sanal Ortam Oluşturma ve Etkinleştirme**
    ```bash
    python -m venv .venv
    # Windows için:
    .venv\Scripts\activate
    # macOS/Linux için:
    source .venv/bin/activate
    ```

3.  **Bağımlılıkları Yükleme**
    ```bash
    pip install -r requirements.txt
    ```

## 🖥️ Kullanım

### Terminal Uygulaması (Aşama 1 & 2)

Terminal uygulamasını başlatmak için `main.py` dosyasını çalıştırın.
```
python main.py
```

API Sunucusu (Aşama 3)
API sunucusunu başlatmak için uvicorn komutunu kullanın. Sunucu, http://127.0.0.1:8000 adresinde çalışacaktır.

```uvicorn api:app --reload```

API çalışırken, otomatik olarak oluşturulan interaktif dokümantasyona http://127.0.0.1:8000/docs adresinden erişebilirsiniz.

#### 📖 API Endpoint'leri
1. Kitapları Listele
Endpoint: GET /books

Açıklama: Kütüphanedeki tüm kitapların listesini döndürür.

Örnek Yanıt:
[
  {
    "title": "Harry Potter and the Sorcerer's Stone",
    "author": "J.K. Rowling",
    "isbn": "9780590353427"
  }
]

2. Kitap Ekle
Endpoint: POST /books

Açıklama: Belirtilen ISBN'e göre Open Library API'den kitap bilgilerini çeker ve kütüphaneye ekler.

İstek Gövdesi (Request Body):
{
  "isbn": "9780321765723"
}

Başarılı Yanıt:
{
  "title": "The Lord of the Rings",
  "author": "J.R.R. Tolkien",
  "isbn": "9780321765723"
}

3. Kitap Sil
Endpoint: DELETE /books/{isbn}

Açıklama: Belirtilen ISBN'e sahip kitabı kütüphaneden siler.

Örnek Kullanım:
DELETE /books/9780321765723

Başarılı yanıt:
{
  "message": "Kitap başarıyla silindi."
}

📂 Proje Yapısı
.
├── api.py
├── api_utils.py
├── book.py
├── library.py
├── main.py
├── requirements.txt
├── pytest.ini
├── test_api_utils.py
└── test_library.py
💻 Kullanılan Teknolojiler
Python

FastAPI: Web servisi oluşturmak için.

Uvicorn: ASGI sunucusu olarak.

Httpx: Asenkron HTTP istekleri için.

Pydantic: Veri doğrulama ve API modelleri için.

pytest: Testler için.

Yazar: [ÖZLEM EKER]
mail : oozlemeker@gmail.com
