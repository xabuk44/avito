def create_flat(district, price, room_count, new_old, square_m, floor):
    return {
        'District': district,
        'Price': price,
        'Rooms': room_count,
        'New flat?': new_old,
        'Square(m2)': square_m,
        'Floor': floor,
    }



def add_flat(container, flat):
    container.append(flat)



def search_dis(container, search):  # search Это строка поиска
    result_d = []
    if search == str(search):
        search_lowercased = search.strip().lower()  # 1 -- strip  2. реузльтат search.strip переводится в нижгний регистр
        for flat in container:
            if search_lowercased in flat['District'].lower():
                result_d.append(flat)
            return result_d
        if search != str(search):
            for flat in container:
                if search >= flat['Price']:
                    result_d.append(flat)
            return



def search_price_without_input(container, search):

    result_p = []
    for flat in container:
        if search >= flat['Price']:
            result_p.append(flat)
    return result_p