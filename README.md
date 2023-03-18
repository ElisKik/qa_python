Тесты класса `BooksCollector`
===

# Как запустить

1. Открыть терминал.
2. Склонировать репозиторий.
3. Перейти в директорию репозитория с помощью команды `cd`
4. Развернуть virtual environment:
   ```bash
   python -m venv .venv
   ```
5. Запустить virtual environment:
   ```bash
   source .venv/bin/activate
   ```
6. Установить зависимость (`pytest`) внутри virtual environment:
   ```bash
   pip install -r requirements.txt
   ```
7. Запустить тесты:
   ```bash
   pytest -v tests.py
   ```
8. Убедиться в том, что все тесты прошлись.
    <details>
        <summary>Вывод должен быть следующим...</summary>

    ```bash
    ============================= test session starts ==============================
    ...
    tests.py::TestBooksCollector::test_add_new_book_multiple_count_equals[names0-1] PASSED [  8%]
    tests.py::TestBooksCollector::test_add_new_book_multiple_count_equals[names1-2] PASSED [ 16%]
    tests.py::TestBooksCollector::test_add_new_book_twice_count_equals_one PASSED [ 25%]
    tests.py::TestBooksCollector::test_set_book_rating_not_added_not_changed PASSED [ 33%]
    tests.py::TestBooksCollector::test_set_book_rating_out_of_bound_not_changed[-1] PASSED [ 41%]
    tests.py::TestBooksCollector::test_set_book_rating_out_of_bound_not_changed[0] PASSED [ 50%]
    tests.py::TestBooksCollector::test_set_book_rating_out_of_bound_not_changed[11] PASSED [ 58%]
    tests.py::TestBooksCollector::test_get_book_rating_not_added_is_none PASSED [ 66%]
    tests.py::TestBooksCollector::test_add_book_in_favorites_multiple_count_equals[names0-1] PASSED [ 75%]
    tests.py::TestBooksCollector::test_add_book_in_favorites_multiple_count_equals[names1-2] PASSED [ 83%]
    tests.py::TestBooksCollector::test_add_book_in_favorites_not_added_not_found PASSED [ 91%]
    tests.py::TestBooksCollector::test_delete_book_from_favorites_not_found PASSED [100%]

    ============================== 12 passed in 0.02s ==============================
    ```

    </details>

# Реализованные тесты

- [x] Проверка добавления книг
- [x] Нельзя добавить одну и ту же книгу дважды
- [x] Нельзя выставить рейтинг книге, которой нет в списке
- [x] Нельзя выставить рейтинг меньше 1
- [x] Нельзя выставить рейтинг больше 10
- [x] У не добавленной книги нет рейтинга
- [x] Добавление книги в избранное
- [x] Нельзя добавить книгу в избранное, если её нет в словаре `books_rating`
- [x] Проверка удаления книги из избранного
