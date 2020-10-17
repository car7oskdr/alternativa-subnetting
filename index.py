from os import system
from subnetting.indexIp import clasIp as ip

while True:

    print('\n\t \\*******>Menu<*******/ \n')
    print('\n\t1.-Go Ip')
    print('\n\t2.-pass for now')
    print('\n\t3.-pass for now')
    print('\n\t4.-Exit.\n')

    try:
        opt = int(input('Please select a option: '))
        print('\n\n')

        if opt <= 0:
            print('=' * 85)
            print('\n\tYou entered a zero or a negative number')
            print('\t\tPlease enter a whole number of the list. \n')
            print('=' * 85)
        elif opt == 1:
            system("clear")
            ip()
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            print('=' * 85)
            print('\n\t Thanks for use the app.')
            print('=' * 85)
            break
        else:
            print('=' * 85)
            print('\n\tThe number entered', opt)
            print('\tit\'s out of list range, select other option\n\n')
            print('=' * 85)

    except ValueError:

        print('=' * 85)
        print('\n\t You entered a character or')
        print('\t a number with a decimal point.')
        print('\t\t Please select a int number of the list.')
        print('=' * 85)
