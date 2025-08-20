# Burada FastAPI ile API endpoint'lerini yazacağız (Aşama 3)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from library import Library # Library sınıfımızı import ediyoruz
from book import Book       # Book sınıfımızı import ediyoruz

# Library sınıfının bir örneğini oluştur
# Bu, tüm API endpoint'lerinin aynı kütüphane verisi üzerinde çalışmasını sağlar.
library = Library()

# Pydantic modelleri, API'nin veri alışverişini tanımlar.
# Bu, hem dokümantasyon hem de veri doğrulaması için önemlidir.
class BookResponse(BaseModel):
    # Book sınıfının nitelikleriyle eşleşmeli
    title: str
    author: str
    isbn: str

    class Config:
        # Pydantic'in Book objesinden doğrudan alanları eşlemesini sağlar
        from_attributes = True # Pydantic v2+ için
        # orm_mode = True # Pydantic v1 için (eğer eski versiyon kullanılıyorsa)

class ISBNRequest(BaseModel):
    isbn: str

app = FastAPI(
    title="Kütüphane API'si",
    description="Global AI Hub Python 202 Bootcamp projesi için Kütüphane Yönetim Sistemi API'si",
    version="1.0.0",
)

@app.get("/books", response_model=List[BookResponse], summary="Tüm kitapları listele")
async def get_all_books():
    """
    Kütüphanedeki tüm kitapları döndürür.
    """
    return library.list_books()

@app.post("/books", response_model=BookResponse, status_code=201, summary="Yeni bir kitap ekle")
async def add_book_api(request: ISBNRequest):
    """
    Belirtilen ISBN'e göre Open Library API'den kitap bilgilerini çeker ve kütüphaneye ekler.
    """
    isbn = request.isbn
    
    # Kütüphaneye ekleme işlemi Library sınıfında zaten halihazırda API çağrısını yapıyor
    if library.add_book(isbn):
        # Kitap başarıyla eklendiğinde find_book ile eklenen kitabı döndürüyoruz.
        # Bu, istemciye eklenen kitabın tam verilerini sağlar.
        added_book = library.find_book(isbn)
        if added_book:
            return added_book
        else:
            # Bu durum normalde oluşmamalıdır, add_book True döndüyse kitap bulunmalıdır.
            raise HTTPException(status_code=500, detail="Kitap eklendi ancak bulunamadı.")
    else:
        # add_book False dönerse, bir hata oluşmuştur (örn: kitap zaten var, API hatası)
        # Library sınıfı zaten hata mesajını bastığı için burada daha genel bir hata dönebiliriz.
        raise HTTPException(status_code=400, detail="Kitap eklenirken bir sorun oluştu. ISBN'i kontrol edin veya tekrar deneyin.")

@app.delete("/books/{isbn}", summary="Bir kitabı ISBN'ine göre sil")
async def delete_book_api(isbn: str):
    """
    Belirtilen ISBN'e sahip kitabı kütüphaneden siler.
    """
    if library.remove_book(isbn):
        return {"message": f"Kitap '{isbn}' başarıyla silindi."}
    else:
        raise HTTPException(status_code=404, detail=f"ISBN '{isbn}' ile kitap bulunamadı.")