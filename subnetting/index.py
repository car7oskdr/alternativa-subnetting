from os import system
from validIp import validIp

while True:

    print('\n\t\t \\=======>SUBNETTING<=======/ \n')
    print('\t\t1.-Know the class and netmask of a ip.')
    print('\t\t2.-Subnetting.')
    print('\t\t3.-Exit.\n')

    try:
        opt = int(input('Please select a option:  '))
        print('\n\n')

        if opt == 1:
            validIp(1)
        elif opt == 2:
            pass
            # subnetting
        elif opt == 3:
            system("clear")
            break
        else:
            print('\n\tThe number entered ', opt)
            print('\t it\'s out of list range, select other option.')
    except ValueError:
        print('=' * 80)
        print('\n\t You entered a characer or')
        print('\t a number with a decimal point')
        print('\tPlease enter a whole number of the list. \n')
        print('=' * 80)
