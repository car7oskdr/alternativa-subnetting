from os import system
from subnetting.classIp import classIp


class validIp():

    def __init__(self, opt):

        self.opt = opt

        def valid_ip():
            """ Docstring for valid_ip.

            :rerutns: A list with the next values.
                    [0] = A list with the ip in binary without unnion =>
                            ['10100000', '00000000', '10100000', '00001010']
                    [1] = A list with the ip in integer without union =>
                            [192, 130, 23, 2]
                    [2] = The ip in str format =>
                            ['192.130.23.2']
            """

            while True:

                try:
                    # Ip entry and division. *******

                    str_ip = input('\n\t Enter the ip: ')
                    list_ip = list(str_ip.split(sep='.'))
                    system("clear")

                    # Converting list values to integers. *******
                    int_lis_ip = []
                    for x in range(len(list_ip)):
                        int_lis_ip.append(int(list_ip[x]))

                    # if -> checks if there are four elements
                    # in the list for the four octets.and verify
                    # that the four elements of the octets are
                    # less than their two hundred and fifty-six.
                    if len(int_lis_ip) == 4 and int_lis_ip[0] < 256:
                        if int_lis_ip[1] < 256:
                            if int_lis_ip[2] < 256:
                                if int_lis_ip[3] < 256:

                                    # Converting the list to binary *******
                                    bin_listip = []
                                    for x in range(len(list_ip)):
                                        bin_listip.append(bin(int(list_ip[x])))
                                    list_ip_bin = []
                                    for x in range(len(bin_listip)):
                                        var = bin_listip[x]
                                        list_ip_bin.append(var[2:])

                                    # Filling the list with octets. *******
                                    for x in range(len(list_ip_bin)):
                                        list_aux = []
                                        var = list_ip_bin[x]
                                        for y in range(len(var)):
                                            list_aux.append(var[y])
                                        while len(list_aux) < 8:
                                            list_aux.insert(0, '0')
                                        var = ''.join(map(str, list_aux))
                                        list_ip_bin[x] = var
                                        list_aux = []

                                    break

                                else:
                                    print('Fourth octect invalid',
                                          'please verify.')
                            else:
                                print('Third octect invalid please verify.')
                        else:
                            print('Second octect invalid please verify.')
                    else:
                        print('First octect invalid please verify.')

                except ValueError:

                    print('\n Ip invalid please verify. \n')

            list_ip_binint = []
            list_ip_binint.append(list_ip_bin)
            list_ip_binint.append(int_lis_ip)
            list_ip_binint.append(str_ip)

            return list_ip_binint

        def know_class(bin_ip):
            """Docstring for know_class.

            :bin_ip: First octet of the ip in str format.
            :returns: A integer =>
                        1 if the class is A.
                        2 if the class is B.
                        3 if the class is C.
                        4 if the class is D.
                        5 if the class is E.

            """
            if bin_ip[0] == '0':
                return 1
            elif bin_ip[0] == '1' and bin_ip[1] == '0':
                return 2
            elif bin_ip[0] == '1' and bin_ip[1] == '1' and bin_ip[2] == '0':
                return 3
            elif bin_ip[0] == '1' and bin_ip[1] == '1' and bin_ip[2] == '1' \
                    and bin_ip[3] == '0':
                return 4
            else:
                return 5

        def valid_sub(class_ip):
            """Docstring for valid_sub.

            :class_ip: A integer number of know_class()
            :returns: The number of subnets.

            """

            while True:

                try:
                    subnets = int(input('Enter the number of subnets: '))

                    if subnets < 0:
                        print('The number entered is less than zero',
                              'please ferify')
                    else:

                        if class_ip == 1:
                            if subnets <= 1048574:
                                break
                            else:
                                print('The subnets for the class A must be',
                                      'less than or equal to 1048574',
                                      'please verify.')
                        elif class_ip == 2:
                            if subnets <= 4094:
                                break
                            else:
                                print('The subnets for the class B must be',
                                      'less than or equal 4094',
                                      'please verify.')
                        elif class_ip == 3:
                            if subnets <= 30:
                                break
                            else:
                                print('The subnets for the class C must be',
                                      'less than or equal to 30',
                                      'please verify.')
                        else:
                            print('Subnetting invalid for classes D or E.')
                            break

                except ValueError:
                    print('Please enter an integer greater than zero.')

            return subnets

        var = valid_ip()

        if self.opt == 1:
            classIp(var[2], know_class(var[0]))
        else:
            pass
