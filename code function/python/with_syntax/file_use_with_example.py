'contoh penggunaan with untuk memastikan file tertutup setelah memanggil with'


##### cara kuno
file = open('file.txt', 'r')
content = file.read()
file.close()

##### cara modern

with open('file.txt', 'r') as file:
    content = file.read()
    print('fungsi atau logic yang akan di execute sebelum file di tutup')


