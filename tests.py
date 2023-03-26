import pytest

class TestBooksCollector:
    @pytest.mark.parametrize(
        'names, expected_count',
        [
            (['Щегол'], 1),
            (['Послемрак', '1Q84'], 2)
        ]
    )
    def test_add_new_book(self, books_collector, names, expected_count):
        for name in names:
            books_collector.add_new_book(name)

        books_rating = books_collector.get_books_rating()

        books_count = len(books_rating)

        assert books_count == expected_count, f'Expected count of books in rating: {expected_count}, got: {books_count}'

    def test_add_new_book_same(self, books_collector):
        name = 'Щегол'

        books_collector.add_new_book(name)
        books_collector.add_new_book(name)

        books_rating = books_collector.get_books_rating()

        books_count = len(books_rating)
        expected_count = 1

        assert books_count == expected_count, f'Expected count of books in rating: {expected_count}, got: {books_count}'

    def test_set_book_rating_not_added(self, books_collector):
        added_name = 'Щегол'
        books_collector.add_new_book(added_name)

        not_added_name = '1Q84'
        books_collector.set_book_rating(not_added_name, 5)

        books_rating = books_collector.get_books_rating()

        assert not_added_name not in books_rating.keys(), f'Book {not_added_name} must not be in books rating, because it was not added'

    @pytest.mark.parametrize(
        'wrong_rating',
        [
            -1,
            0,
            11
        ]
    )
    def test_set_book_rating_out_of_bound(self, books_collector, wrong_rating):
        name = 'Щегол'

        books_collector.add_new_book(name)
        books_collector.set_book_rating(name, wrong_rating)

        book_rating = books_collector.get_book_rating(name)

        assert book_rating is not wrong_rating, f'Book {name} added with the wrong rating {wrong_rating}'

    def test_get_book_rating_not_added(self, books_collector):
        name = 'Щегол'

        book_rating = books_collector.get_book_rating(name)

        assert book_rating is None, f'Book {name} must not be in books rating, because it was not added'

    @pytest.mark.parametrize(
        'names, expected_count',
        [
            (['Щегол'], 1),
            (['Послемрак', '1Q84'], 2)
        ]
    )
    def test_add_book_in_favorites(self, books_collector, names, expected_count):
        for name in names:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        favorite_books = books_collector.get_list_of_favorites_books()

        books_count = len(favorite_books)

        assert books_count == expected_count, f'Expected count of favorite books: {expected_count}, got: {books_count}'

    def test_add_book_in_favorites_not_added(self, books_collector):
        name = 'Щегол'

        books_collector.add_book_in_favorites(name)

        books_rating = books_collector.get_books_rating()
        favorite_books = books_collector.get_list_of_favorites_books()

        assert name not in books_rating, f'Book {name} must not be in books rating, because it was not added'
        assert name not in favorite_books, f'Book {name} must not be in favorites, because it was not added'

    def test_delete_book_from_favorites(self, books_collector):
        name = 'Щегол'

        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)

        favorite_books = books_collector.get_list_of_favorites_books()

        assert name not in favorite_books, f'Book {name} must not be in favorites, because it was deleted'
