import sys
import getopt


def usrMSG():

    print("Fruit Menu")
    print("")
    print("-a --apple ")
    print("-b --bannana ")
    print("-o --orange ")
    print("-g --grapes ")
    print("-s --strawberry")
    print("-p --pear ")
    print("-t --tangerine ")
    print("")
    print("")
    print("Examples: ")
    print("expressMenu.py -a -b -o")
    print("expressMenu.py -apple -bannana -orange")

def main():


    if not len(sys.argv[1:]):
        usrMSG()
        sys.exit("no args")


    try:

        print(sys.argv[1:])

        opts, args = getopt.getopt(sys.argv[1:], "abogspt",
                                   ["apple", "bannana", "orange", "grapes", "strawberry", "pear", "tangerine"])

    except getopt.GetoptError as err:
        print(str(err))
        usrMSG()

    for o, a in opts:
        if o in ("-a", "--apple"):
            print("apples")
        elif o in ("-b", "--bannana"):
            print("bannas")
        elif o in ("-o", "--orange"):
            print("orange")
        elif o in ("-g", "--grapes"):
            print("grapes")
        elif o in ("-s", "--strawbery"):
            print("strawberry")
        elif o in ("-p", "--pear"):
            print("pear")
        elif o in ("-t", "--tangerine"):
            print("tangerine")
        else:
            assert False, "Unhandled Option"

main()
