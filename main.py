from library import Library
from book import Book

def main():
    lib = Library()

    while True:
        print("\n📚 Kütüphane Uygulaması 📚")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            isbn = input("ISBN giriniz: ")
            if lib.add_book(isbn):
                print("✅ Kitap eklendi.")
            else:
                print("⚠️ Kitap eklenemedi.")

        elif choice == "2":
            isbn = input("Silmek istediğiniz kitabın ISBN'i: ")
            if lib.remove_book(isbn):
                print("✅ Kitap silindi.")
            else:
                print("⚠️ Kitap bulunamadı.")

        elif choice == "3":
            books = lib.list_books()
            if books:
                for b in books:
                    print(b)
            else:
                print("📭 Kütüphane boş.")

        elif choice == "4":
            isbn = input("Aranan kitabın ISBN'i: ")
            book = lib.find_book(isbn)
            print(book if book else "Kitap bulunamadı.")

        elif choice == "5":
            print("👋 Çıkış yapılıyor...")
            break
        else:
            print("⚠️ Geçersiz seçim!")

if __name__ == "__main__":
    main()
