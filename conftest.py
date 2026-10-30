import pytest
from library.service import LibraryService


@pytest.fixture
def library():
    app = LibraryService()
    app.register_book("B1", "The Pragmatic Programmer", "Andrew Hunt", copies=2)
    app.register_book("B2", "Clean Code", "Robert C. Martin", copies=1)
    return app
