from lib.book import Book

'''Class Constructs with correct properties'''
def test_book_constructs_correctly():
    book = Book(1, 'All Quiet on the Western Front', 'Erich Maria Remarque')
    assert book.id == 1
    assert book.title == 'All Quiet on the Western Front'
    assert book.author_name == 'Erich Maria Remarque'

'''Class prints nicely formatted strings'''
def test_books_format_nicely():
    book = Book(1, 'All Quiet on the Western Front', 'Erich Maria Remarque')
    assert str(book) == "Book(1, All Quiet on the Western Front, Erich Maria Remarque)"

'''Two idetical books are equal'''
def test_books_are_equal():
    book1 = Book(1, 'All Quiet on the Western Front', 'Erich Maria Remarque')
    book2 = Book(1, 'All Quiet on the Western Front', 'Erich Maria Remarque')
    assert book1 == book2
