def create_flat(district, price, room_count, new_old, square_m, floor, house_type):
    return {
        'District': district,
        'Price': price,
        'Rooms': room_count,
        'New flat?': new_old,
        'Square(m2)': square_m,
        'Floor': floor,
        'House type': house_type,
    }

def create_flat_self(district, price, room_count, new_old, square_m, floor, house_type):
    district = input('district: '),
    price = input('price: '),
    room_count = input('room: '),
    new_old = input('New?: '),
    square_m = input('Square(m2): ',),
    floor = input('Floor: '),
    house_type = input('House type: ',)
    return {
        'District': district,
        'Price': price,
        'Rooms': room_count,
        'New flat?': new_old,
        'Square(m2)': square_m,
        'Floor': floor,
        'House type': house_type,
    }


def add_flat(container, flat):
    container.append(flat)


def search_district(container, search):  # search Это строка поиска
    search_lowercased = search.strip().lower()  # 1 -- strip  2. реузльтат search.strip переводится в нижгний регистр
    result_d = []
    for flat in container:
        if search_lowercased in flat['District'].lower():
            result_d.append(flat)

    return result_d


def search_price(container, search):
    search = int(input('Enter max price: '))
    result_p = []
    for flat in container:
        if search > flat['Price']:
            result_p.append(flat)
    return result_p
