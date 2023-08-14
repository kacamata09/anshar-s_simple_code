# test syntax *

list_dummy = [['dont', 'do', 'it'], ['do', 'it', 'bro'], {'this': 'dictionary'}, 'string', 10]
# list_dummy = [
#     [10, 20, 10, 20, 11, 12, 52, 10, 20, 53, 20, 40, 10],
#     [19, 10, 10, 20, 11, 12, 51, 10, 20, 52, 20, 40, 10],
#     [19, 10, 51, 20, 11, 12, 54, 10, 20, 55, 20, 40, 10],
#     [19, 10, 51, 20, 56, 12, 54, 10, 20, 55, 20, 40, 10],
#     [19, 10, 51, 20, 54, 12, 54, 10, 20, 55, 20, 40, 10],
#     [19, 10, 51, 20, 54, 12, 54, 10, 20, 55, 20, 40, 10],
# ]

asterisk_list = [*list_dummy]

print(asterisk_list)

# for i in zip(list_dummy):
#     print('value')
#     # print(i)

# for i in zip(*list_dummy):
#     print('value')
#     # print(i)

