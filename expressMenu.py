##########################################################################################################
#                                                                                                        #
# 1. create a basic menu capaple of imitating console inputs to do some work.                            #
#                                                                                                        #
#    a. Type python and expressMenu along with a few commands.                                           #
#                                                                                                        #
#    b. EX: python expressMenu.py -a -b -g                                                               #
#                                                                                                        #
#                                                                                                        #
# 2. If you type a wrong command it will terminate the program and give you a set of instructions        #
#                                                                                                        #
# 3. The script was built with the intention of being run like common networking tools                   #
#                                                                                                        #
# 4. The scrip outputs the names of fruit, this will be used as a template for future projects.          #
#                                                                                                        #
##########################################################################################################

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
        sys.exit(0)

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
