from main.lib import create_flat, add_flat, search_dis, search_price_without_input


def test_create_flat():
    data = {
        'District': 'Vahitovskiy',
        'Price': 4_000_000,
        'Rooms': 1,
        'New flat?': True,
        'Square(m2)': 40,
        'Floor': 6,
        'House type': 'Brick',
    }
    result = create_flat(data['District'], data['Price'], data['Rooms'], data['New flat?'], data['Square(m2)'], data['Floor'], data['House type'])
    assert data == result


def test_add_flat():
    flat_list = []
    flat = create_flat(
        'Vahitovskiy',
        4_000_000,
        1,  # room
        True,
        40,  # square
        6,
        'Brick',
    )
    add_flat(flat_list, flat)
    assert flat_list == [flat]
    assert flat in flat_list
    assert len(flat_list)

def test_search_district():
    flat_list = []
    flat_1 = create_flat(
        'Aviastroitelniy',
        2_000_000,
        1,  # room
        False,
        30,  # square
        3,
        'Panel',
    )

    flat_2 = create_flat(
        'Vahitovskiy',
        4_000_000,
        1,  # room
        True,
        40,  # square
        6,
        'Brick',
    )

    flat_3 = create_flat(
        'Sovetskiy',
        8_000_000,
        5,  # room
        True,
        120,  # square
        10,
        'Monolith',
    )

    add_flat(flat_list, flat_1)
    add_flat(flat_list, flat_2)
    add_flat(flat_list, flat_3)
    search_result = [{
        'District': 'Vahitovskiy',
        'Price': 4_000_000,
        'Rooms': 1,
        'New flat?': True,
        'Square(m2)': 40,
        'Floor': 6,
        'House type': 'Brick',
    }]
    result = search_dis(flat_list, 'Vahitov')
    assert search_result == result

def test_search_price_without_input():
    flat_list = []
    flat_1 = create_flat(
        'Aviastroitelniy',
        2_000_000,
        1,  # room
        False,
        30,  # square
        3,
        'Panel',
    )

    flat_2 = create_flat(
        'Vahitovskiy',
        4_000_000,
        1,  # room
        True,
        40,  # square
        6,
        'Brick',
    )

    flat_3 = create_flat(
        'Sovetskiy',
        8_000_000,
        5,  # room
        True,
        120,  # square
        10,
        'Monolith',
    )

    add_flat(flat_list, flat_1)
    add_flat(flat_list, flat_2)
    add_flat(flat_list, flat_3)
    result = [{'District': 'Aviastroitelniy', 'Price': 2000000, 'Rooms': 1, 'New flat?': False, 'Square(m2)': 30, 'Floor': 3, 'House type': 'Panel'}, {'District': 'Vahitovskiy', 'Price': 4000000, 'Rooms': 1, 'New flat?': True, 'Square(m2)': 40, 'Floor': 6, 'House type': 'Brick'}]
    assert result == search_price_without_input(flat_list, 4_200_000)