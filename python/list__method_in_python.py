'percobaan list method'

def satu(param1, param2):
    print('ini satu ' + param1 )
    print(param2)

def dua(param1, param2):
    print('ini dua ' + param1 )
    print(param2)

def tiga(param1, param2):
    print('ini tiga ' + param1 )
    print(param2)

def empat(param1, param2):
    print('ini empat ' + param1 )
    print(param2)

def lima(param1, param2):
    print('ini lima ' + param1 )
    print(param2)



list_function = [satu, dua, tiga, empat, lima]
'untuk eksekusi banyak def sekaligus, bisa menggunakan cara ini, bahkan class juga bisa di execute spam menggunakan ini'

for i in list_function:
    i('param1 di execute', 'param2 di execute')