# hero = {}
villain = {
    'power' : 1000,
    'defense': 2000,
    'speed' : 3000
}

villain_1 = {
    'power': 200,
    'defense' : 30000,
    'speed': 1000
}

villain_2 = {
    'power': 2000,
    'defense' : 3000,
    'speed': 1000
}

list_villain = [villain, villain_1, villain_2]

new_list_villain = [{'power' : i['power'] + 1000, 'defense': i['defense'] + 2000, 
                 'speed': i['speed'], 'buff': True} for i in list_villain]
print(new_list_villain)


# menggunakan map()
buff_villain = lambda i: {'power' : i['power'] + 1000, 
                           'defense': i['defense'] + 2000, 
                            'speed': i['speed'], 'buff': True, 'map': 'ya'}

# def buff_villain_func(i):
#     return {'power' : i['power'] + 1000, 
#             'defense': i['defense'] + 2000, 
#             'speed': i['speed'], 'buff': True, 'func': 'ya'}

villain_reborn = list(map(buff_villain, list_villain))
print(villain_reborn)


