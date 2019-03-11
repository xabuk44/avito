from lib import create_flat
from lib import create_flat_self
from lib import add_flat
from lib import search_district
from lib import search_price
import random
from lib import search_dis
from lib import search_price_without_input

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
    4_000_000,
    1,               #room
    True,
    40,              #square
    6,
    'Brick',
)

flat_3 = create_flat(
    'Sovetskiy',
    8_000_000,
    5,               #room
    True,
    120,              #square
    10,
    'Monolith',
)

add_flat(flat_list, flat_1)
add_flat(flat_list, flat_2)
add_flat(flat_list, flat_3)


print('Welcome!\nFlats list:\n')
print('\n'.join(str(value) for value in flat_list))

a = input('Add flat? Y/N:').strip().lower()
if a == 'y':
    random.random = create_flat_self(1,2,3,4,5,6,7)
    flat_list.append(random.random)
    print(flat_list)
elif a != 'y':
    c = input('Search for flats? Y/N: ').strip().lower()
    if c == 'y':
        b = input('Enter - dist - to search by district, enter - price - to search by price:').strip().lower()
        if b == 'dist':
            print(search_district(flat_list, 'a'))
        if b == 'price':
            print(search_price(flat_list, 1))
        else:
            print(flat_list)
# print('\n'.join(str(value) for value in flat_list))
print(search_price_without_input(flat_list, 4_200_000))