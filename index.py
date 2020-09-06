from os import system
from subnetting.indexIp import ClaseIps as ip
# esta es una prueba.
while True:
    print('\n\t\t*******>MENU PRINCIPAL<*******/\n')
    print('\t\t1.-Ir a IP')
    print('\t\t2.-pass por ahora.')
    print('\t\t3.-pass por ahora.')
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
            system("clear")
            ip()
        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            print('=' * 85)
            print('\n\t\t "Gracias por usar la app"\n')
            print('=' * 85)
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