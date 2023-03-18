import pytest

from main import BooksCollector

class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def fixture_books_collector(self):
        self.books_collector = BooksCollector()
        return self.books_collector

    @pytest.mark.parametrize(
        'names, expected_count',
        [
            [ [ 'Щегол' ], 1 ],
            [ [ 'Послемрак', '1Q84' ], 2 ]
        ]
    )
    def test_add_new_book_multiple_count_equals(self, names, expected_count):
        for name in names:
            self.books_collector.add_new_book(name)

        books_rating = self.books_collector.get_books_rating()

        assert len(books_rating) == expected_count

    def test_add_new_book_twice_count_equals_one(self):
        name = 'Щегол'

        self.books_collector.add_new_book(name)
        self.books_collector.add_new_book(name)

        books_rating = self.books_collector.get_books_rating()

        assert len(books_rating) == 1

    def test_set_book_rating_not_added_not_changed(self):
        added_name = 'Щегол'
        self.books_collector.add_new_book(added_name)

        not_added_name = '1Q84'
        self.books_collector.set_book_rating(not_added_name, 5)

        books_rating = self.books_collector.get_books_rating()

        assert not_added_name not in books_rating.keys()

    @pytest.mark.parametrize(
        'wrong_rating',
        [
            -1,
            0,
            11
        ]
    )
    def test_set_book_rating_out_of_bound_not_changed(self, wrong_rating):
        name = 'Щегол'

        self.books_collector.add_new_book(name)
        self.books_collector.set_book_rating(name, wrong_rating)

        book_rating = self.books_collector.get_book_rating(name)

        assert book_rating is not wrong_rating

    def test_get_book_rating_not_added_is_none(self):
        name = 'Щегол'

        book_rating = self.books_collector.get_book_rating(name)

        assert book_rating is None

    @pytest.mark.parametrize(
        'names, expected_count',
        [
            [ [ 'Щегол' ], 1 ],
            [ [ 'Послемрак', '1Q84' ], 2 ]
        ]
    )
    def test_add_book_in_favorites_multiple_count_equals(self, names, expected_count):
        for name in names:
            self.books_collector.add_new_book(name)
            self.books_collector.add_book_in_favorites(name)

        favorite_books = self.books_collector.get_list_of_favorites_books()

        assert len(favorite_books) == expected_count

    def test_add_book_in_favorites_not_added_not_found(self):
        name = 'Щегол'

        self.books_collector.add_book_in_favorites(name)

        books_rating = self.books_collector.get_books_rating()
        favorite_books = self.books_collector.get_list_of_favorites_books()

        assert name not in books_rating and \
               name not in favorite_books

    def test_delete_book_from_favorites_not_found(self):
        name = 'Щегол'

        self.books_collector.add_new_book(name)
        self.books_collector.add_book_in_favorites(name)
        self.books_collector.delete_book_from_favorites(name)

        favorite_books = self.books_collector.get_list_of_favorites_books()

        assert name not in favorite_books

