list_numbers = [20, 30, 20, 40, 30]

# mapping menggunakan for
new_numbers = [i + 100 for i in list_numbers]
print(new_numbers)

new_numbers = [(i, i + 100) for i in list_numbers]
print(new_numbers)

# mapping menggunakan map()
new_numbers_map = list(map(lambda i: i + 100, list_numbers))
print(new_numbers_map)

new_numbers_map = list(map(lambda i: (i, i+ 100) , list_numbers))
print(new_numbers_map)




