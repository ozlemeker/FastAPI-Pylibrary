import pytest
from library import Library
from api_utils import fetch_book_info


def test_add_and_find_book(tmp_path, monkeypatch):
    # API çağrısını sahte veriyle değiştiriyoruz
    def fake_fetch_book_info(isbn):
        return {"title": "Test Book", "author": "Test Author", "isbn": isbn}

    from library import fetch_book_info
    monkeypatch.setattr("library.fetch_book_info", fake_fetch_book_info)

    lib_file = tmp_path / "test.json"
    lib = Library(filename=str(lib_file))

    assert lib.add_book("123") == True
    found = lib.find_book("123")
    assert found is not None
    assert found.title == "Test Book"

def test_remove_book(tmp_path, monkeypatch):
    def fake_fetch_book_info(isbn):
        return {"title": "Test Book", "author": "Test Author", "isbn": isbn}

    monkeypatch.setattr("library.fetch_book_info", fake_fetch_book_info)

    lib_file = tmp_path / "test.json"
    lib = Library(filename=str(lib_file))

    lib.add_book("123")
    assert lib.remove_book("123") == True
    assert lib.find_book("123") is None

def test_list_books(tmp_path, monkeypatch):
    def fake_fetch_book_info(isbn):
        return {"title": f"Book {isbn}", "author": "Author", "isbn": isbn}

    monkeypatch.setattr("library.fetch_book_info", fake_fetch_book_info)

    lib_file = tmp_path / "test.json"
    lib = Library(filename=str(lib_file))

    lib.add_book("111")
    lib.add_book("222")
    books = lib.list_books()
    assert len(books) == 2
