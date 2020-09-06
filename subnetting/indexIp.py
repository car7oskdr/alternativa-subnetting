from os import system
from subnetting.tipoclase import clasesIp

class ClaseIps():
    
    def __init__(self):

        while True:
            #menu de subnetting
            print('\n\t\t=======>SUBNETTING<=======/\n')
            print('\t\t1.-Conocer la clase y mascara de red de una IP.')
            print('\t\t2.-Conocer la viabilidad del subneteo de un IP.')
            print('\t\t3.-Realizar subenetting.')
            print('\t\t4.-Salir\n')

            try:
                opc = int(input('Favor de eligir una opción: '))
                print('\n\n')

                if opc <= 0:
                    print('=' * 85)
                    print('\n\t\tHas ingresado un cero o un numero negativo')
                    print('\t\tFavor de elegir un numero entero de la lista.\n')
                    print('=' * 85)
                elif opc == 1:
                    clasesIp(1)
                elif opc == 2:
                    pass
                elif opc == 3:
                    pass
                elif opc == 4:
                    system("clear")
                    break
                else:
                    print('=' * 85)
                    print('\n\t El numero ingresado',opc,' esta fuera del rango de la lista, elige otra opción.\n\n')
                    print('=' * 85)

            except ValueError:
                print('=' * 85)
                print('\n\tHas escogido un carater o ingresaste un numero con punto decimal.')
                print('\t\tFavor de elegir un numero entero de la lista.\n')
                print('=' * 85)