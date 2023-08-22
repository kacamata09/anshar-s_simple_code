def match_case(condition):
    'penggunaan match case seperti switch case di bahasa pemrograman lain, tapi syntax ini hanya ada di python versi >= 3.10'
    match condition:
        case 1:
            return 'ini 1'
        case 2:
            return 'ini 2'
        case 3:
            return 'ini 3'
        case 4:
            return 'ini 4'
        case 5:
            return 'ini 5'
        

print(match_case(5))