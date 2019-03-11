from main.lib import create_flat, add_flat


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
