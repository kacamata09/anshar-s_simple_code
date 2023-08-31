#### test syntax *

# list_asterisk = [['dont', 'do', 'it'], ['do', 'it', 'bro'], {'this': 'dictionary'}, 'string', 10]
list_asterisk = [
    [10, 20, 10, 20, 11, 12, 52, 10, 20, 53, 20, 40, 10],
    [19, 10, 10, 20, 11, 12, 51, 10, 20, 52, 20, 40, 10],
    [19, 10, 51, 20, 11, 12, 54, 10, 20, 55, 20, 40, 10],
    [19, 10, 51, 20, 56, 12, 54, 10, 20, 55, 20, 40, 10],
    [19, 10, 51, 20, 54, 12, 54, 10, 20, 55, 20, 40, 10],
    [19, 10, 51, 20, 54, 12, 54, 10, 20, 55, 20, 40, 10],
]

asterisk_list = [*list_asterisk]

# print(asterisk_list)

#### test syntax zip
'syntax zip untuk transpose data misal zip([10, 20], ["do", "it"]) maka return iterate nya (10, "do"), (20, "it")'

list_zip1 = ['dont', 'stay', 'awake']
list_zip2 = [[10, 20, 30], [20, 30, 50], ['list', 'zip']]
list_zip3 = [6, 8, 9]


# for i in zip(list_zip1, list_zip2, list_zip3):
#     print('value')
#     print(i)

list_zip_asterisk = [[10, 20, 30], [600, 300, 530], ['list', 'zip']]

for i in zip(*list_zip_asterisk):
    'fungsi * disini seperti mengatakan for i in zip(list_zip_asterisk[0], list_zip_asterisk[1], list_zip_asterisk[2])'
    print('value')
    print(i)
