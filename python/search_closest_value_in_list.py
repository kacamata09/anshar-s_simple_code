list_value = [-40, -32, -29, -4, 20, 30, 40, 50, 54, 63, 69, 83, 94]
value = 26

closest_value = None
closest_index = None

for index, num in enumerate(list_value):
    difference = abs(num - value)
    # print(difference)

    if closest_value is None or difference < closest_value:
        closest_value = difference
        closest_index = index

# Hasilnya
print("Nilai terdekat:", list_value[closest_index])
print("Indeks nilai terdekat:", closest_index)
