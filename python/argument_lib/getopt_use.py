import getopt
import sys

# cara lama


def show_help():
    print("ini help")


SAVE = False
PORT = None

try:
    opts, args = getopt.getopt(
        sys.argv[1:], shortopts="sp:h", longopts=["save", "port=", "help"]
    )

except getopt.GetoptError as err:
    print(err)
    print("Error: Invalid Argument")
    show_help()
    sys.exit(1)

for opt, arg in opts:
    if opt == "-h":
        show_help()
        sys.exit(0)

    if opt == "-s":
        SAVE = True

    if opt == "-p" or opt == "--port":
        PORT = arg

print("SAVE:", SAVE)
print("PORT:", PORT)
