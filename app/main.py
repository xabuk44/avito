import random

from flask import Flask, render_template, request

flat_1 = {
    'District': 'moskovskiy',
    'price': 3_000_000,
    'rooms': 2,
    'new flat?': True,
    'square(m2)': 50,
    'floor': 4
}
flat_2 = {
    'District': 'vahitovskiy',
    'price': 4_000_000,
    'rooms': 1,
    'new flat?': True,
    'square(m2)': 40,
    'floor': 7
}
flat_3 = {
    'District': 'sovetskiy',
    'price': 6_000_000,
    'rooms': 3,
    'new flat?': False,
    'square(m2)': 66,
    'floor': 8
}
flat_4 = {
    'District': 'vahitovskiy',
    'price': 8_000_000,
    'rooms': 3,
    'new flat?': False,
    'square(m2)': 90,
    'floor': 12
}
flat_list = [flat_1, flat_2, flat_3, flat_4]

from app.avito import search_dis, search_price_without_input


def main():
    app = Flask(__name__)

    # wp = create_book('war and piece', 'tolstoy')
    # ak = create_book('anna karenina', 'jopskoy')

    # сделать распаковку эдд буууук
    # container = add_book(container, wp)
    # container = add_book(container, ak)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search == str(search):
            results = search_dis(flat_list, search)
            return render_template('index.html', flats=results, search=search)
        return render_template('index.html', flats=flat_list)

    app.run(port=9008, debug=True)


if __name__ == '__main__':
    main()
