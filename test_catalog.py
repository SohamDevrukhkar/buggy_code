def test_search_is_case_insensitive(library):
    results = library.catalog.search("pragmatic")
    assert [book.book_id for book in results] == ["B1"]


def test_search_returns_empty_for_no_match(library):
    assert library.catalog.search("nonexistent") == []


def test_duplicate_book_id_is_rejected(library):
    import pytest
    from library.catalog import Book
    with pytest.raises(ValueError, match="already exists"):
        library.catalog.add_book(Book("B1", "Another title", "Someone", 1))
