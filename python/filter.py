def filtering(x):
    # bisa dengan filter yang lebih kompleks lagi kalau mau
    if x > 20:
        return True
    else:
        return 1


print(filtering(10))

list_number = [10, 12, 14, 30, 40, 50, 60]

for i in filter(filtering, list_number):
    print(i)

for i in filter(lambda x: x > 20, list_number):
    print(i)

new_number = list(filter(filtering, list_number))
print(new_number)
