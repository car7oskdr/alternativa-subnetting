class classIp():

    """Specific default nemask."""

    def __init__(self, str_ip, class_ip):
        """

        :str_ip: The ip in str formart [192.192.192.192]
        :class_ip: The default netmask of the ip.

        """

        self._str_ip = str_ip
        self._class_ip = class_ip

        if self._class_ip == 1:
            print('+' * 85)
            print('\n\t The ip ', self._str_ip, ' is class A it\'s',
                  'default netmask is 255.0.0.0 /8\n')
            print('+' * 85)
        elif self._class_ip == 2:
            print('+' * 85)
            print('\n\t The ip ', self._str_ip, ' is class B it\'s',
                  'default netmask is 255.255.0.0 /16\n')
            print('+' * 85)
        elif self._class_ip == 3:
            print('+' * 85)
            print('\n\t The ip ', self._str_ip, ' is class C it\'s',
                  'default netmask is 255.255.255.0 /24\n')
            print('+' * 85)
        elif self._class_ip == 4:
            print('+' * 85)
            print('\n\t The ip ', self._str_ip, ' is class D,',
                  'reserved for multicast.\n')
            print('+' * 85)
        else:
            print('+' * 85)
            print('\n\t The ip ', self._str_ip, ' is class E,',
                  'reserved for research.\n')
            print('+' * 85)
