import pytest
from api_utils import fetch_book_info

@pytest.mark.network
def test_valid_isbn():
    book = fetch_book_info("9780140328721")  # Matilda
    print("book:", book)  # Debug için ekledik
    if book is None:
        pytest.skip("API yanıt vermedi veya internet bağlantısı yok")
    assert "title" in book
    assert "author" in book
    assert "isbn" in book

def test_invalid_isbn():
    book = fetch_book_info("0000000000000")
    assert book is None
