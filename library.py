import json
from book import Book
from api_utils import fetch_book_info


class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, isbn: str):
        # ISBN benzersiz olmalı
        if self.find_book(isbn):
            print("Bu ISBN'e sahip kitap zaten mevcut.")
            return False

        # API'den kitap bilgisi çek
        print(f"📖 ISBN '{isbn}' için kitap bilgisi çekiliyor...")
        book_data = fetch_book_info(isbn)
        
        if book_data is None:
            # fetch_book_info fonksiyonu artık kendi hata mesajlarını bastığı için burada ek bir mesaj gerekmez.
            return False

        new_book = Book(**book_data)
        self.books.append(new_book)
        self.save_books()
        print("✅ Kitap başarıyla eklendi.")
        return True


    def remove_book(self, isbn: str):
        initial_count = len(self.books)
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()
        return len(self.books) < initial_count

    def list_books(self):
        return self.books

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            self.books = []
            print(f"Uyarı: '{self.filename}' dosyası bozuk veya boş. Yeni bir kütüphane oluşturuluyor.")


    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([b.__dict__ for b in self.books], f, ensure_ascii=False, indent=4)