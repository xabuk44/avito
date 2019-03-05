from lib import create_flat
from lib import add_flat
from lib import search_district
from lib import search_price

flat_list = []

flat_1 = create_flat(
    'Aviastroitelniy',
    2_000_000,
    1,               #room
    False,
    30,              #square
    3,
    'Panel',
)

flat_2 = create_flat(
    'Vahitovskiy',
    7_000_000,
    3,               #room
    True,
    100,              #square
    17,
    'Monolith',
)

flat_3 = create_flat(
    'Vahitovskiy',
    4_000_000,
    1,               #room
    False,
    40,              #square
    6,
    'Brick',
)


add_flat(flat_list, flat_1)
add_flat(flat_list, flat_2)
add_flat(flat_list, flat_3)

print(flat_list)
print(search_district(flat_list, 'vahit'))
print(search_price(flat_list, 1))
