from lib import create_flat
from lib import create_flat_self
from lib import add_flat
from lib import search_district
from lib import search_price
import random



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

add_flat(flat_list, flat_1)
add_flat(flat_list, flat_2)


print('Welcome!\nFlats list:\n')
print('\n'.join(str(value) for value in flat_list))

a = input('Add flat? Y/N:')
if a == 'y':
    random.random = create_flat_self(1,2,3,4,5,6,7)
    flat_list.append(random.random)
elif a != 'y':
    input('Enter - dist - to search by district, enter - price - to search by price:')
    print(search_price(flat_list, 1))
# print('\n'.join(str(value) for value in flat_list))