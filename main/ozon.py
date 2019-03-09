def create_book(title, author, price, availability, tags):
    return {
        'title': title,
        'author': author,
        'price': price,
        'available': availability,
        'tags': tags,
    }


def add_book(container, book):  # container - it's where books stored
    container.append(book)  # append - is ADDING function


def list_books(container, page, page_size):
    # page_size = 10
    start = (page - 1) *page_size
    finish = start + page_size
    return container[start:finish]


def search_books(container, search):  # search Это строка поиска
    search_lowercased = search.strip().lower()  # 1 -- strip  2. реузльтат search.strip переводится в нижгний регистр
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue

        if search_lowercased in book['tags'].lower():
            result.append(book)
            continue

    return result


books = []

war_and_piece = create_book(
    'War and Peace',
    'Lev Tolstoy',
    1000,
    True,
    'война_и_мир, любовь, толстой, классика, русская, проза'
)

anna_karenina = create_book(
    'Anna Karenina',
    'Lev Tolstoy',
    500,
    False,
    'аннушка_уже_разлила_масло, любовь, толстой, классика, русская, проза'
)


print(add_book(books, war_and_piece))
add_book(books, anna_karenina)


print(search_books(books, "раз"))