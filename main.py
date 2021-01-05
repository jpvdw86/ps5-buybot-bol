from classes.autoOrderClass import autoOrder
import getopt, sys


if __name__ == '__main__':
    full_cmd_arguments = sys.argv
    argument_list = full_cmd_arguments[1:]

    options = ["email=", "password=", "productId=", "timeout=", "directorder"]

    try:
        arguments, values = getopt.getopt(argument_list, "", options)
        autoOrder(arguments).start()
    except getopt.error as err:
        print(str(err))
        sys.exit(2)



