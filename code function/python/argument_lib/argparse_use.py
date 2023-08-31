import argparse


def add_arg():
    parser = argparse.ArgumentParser(
        description="Contoh penggunaan argumen pada skrip Python"
    )
    parser.add_argument(
        "-s", "--save", action="store_true", help="Opsi untuk menyimpan data"
    )

    # untuk mengisi nilainya bisa seperti -n'nilainya' atau bisa juga -n 'nilainya'
    parser.add_argument(
        "-n", "--nilai", type=bool, help="Opsi untuk memunculkan data boolean"
    )

    # untuk mengisi nilainya bisa seperti -n'nilainya' atau bisa juga -n 'nilainya'
    parser.add_argument(
        "-t", "--text", type=str, help="Opsi untuk memunculkan data text"
    )

    # kalau makai -str atau argument yang nilai nya dari dua huruf, itu harus pakai spasi misal -tr 'nilainya'
    parser.add_argument(
        "-str", "--string", type=str, help="Opsi untuk memunculkan data"
    )

    args = parser.parse_args()

    if args.save:
        print("Opsi save diaktifkan")

    if args.nilai is not None:
        print("Opsi nilai diaktifkan dengan nilai:", args.nilai)

    if args.text is not None:
        print("Opsi text diaktifkan dengan text:", args.text)

    if args.string is not None:
        print("Opsi string diaktifkan dengan string:", args.string)


if __name__ == "__main__":
    add_arg()
