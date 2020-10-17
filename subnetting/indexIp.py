from os import system
from subnetting.validIp import validIp


class clasIp():

    def __init__(self):

        while True:

            print('\n\t\t \\=======>SUBNETTING.<=======/\n')
            print('\t\t1.-Know the class and netmask of a Ip.')
            print('\t\t2.-Know viability of subnetting.')
            print('\t\t3.-Subnetting.')
            print('\t\t4.-Exit.\n')

            try:

                opt = int(input('Please select a option: '))
                print('\n\n')

                if opt <= 0:

                    print('=' * 85)
                    print('\n\t\t You entered a zero or a negative number.')
                    print('\t\t Please select a whole number of the list.')
                    print('=' * 85)

                elif opt == 1:

                    validIp(1)

                elif opt == 2:

                    pass

                elif opt == 3:

                    pass

                elif opt == 4:

                    system("clear")
                    break

                else:

                    print('\n\t The number entered ', opt)
                    print('\tit\'s out of list range, select other option.')

            except ValueError:

                print('=' * 85)
                print('\n\t You entered a character or')
                print('\t a number with a decimal point')
                print('\t\t Please enter a whole number of the list.\n')
