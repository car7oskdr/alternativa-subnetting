from os import system
class clasesIp():

	def __init__(self, opc):

		self.opc = opc

		def valida_ip():
			while True:

				try:

					# ingreso de  la IP y división.******************************
					str_ip = input('\n\tIngrese la IP: ')
					lista_ip = list(str_ip.split(sep = '.'))
					system('clear')
					# ***********************************************************

					# conversión de valores de la lista a enteros.***************
					lista_ip_int = []
					for x in range(len(lista_ip)):
						lista_ip_int.append(int(lista_ip[x]))
					# if para saber si hay 4 elementos en la lista que conformen los cuatro octetos
					if len(lista_ip_int) == 4 and lista_ip_int[0] < 256:
						if lista_ip_int[1] < 256:
							if lista_ip_int[2] < 256:
								if lista_ip_int[3] < 256:
									# conversión de la ip a binarios.****************************
									bin_lista_ip = []
									for x in range(len(lista_ip)):
										bin_lista_ip.append(bin(int(lista_ip[x])))
									lista_ip_bin = []
									for x in range(len(bin_lista_ip)):
										var = bin_lista_ip[x]
										lista_ip_bin.append(var[2:])
									# ***********************************************************

									# Llenado de la lista con los octetos ***********************
									for x in range(len(lista_ip_bin)):
										lista_aux = []
										var = lista_ip_bin[x]
										for y in range(len(var)):
											lista_aux.append(var[y])
										while len(lista_aux) < 8:
											lista_aux.insert(0, '0')
										var = ''.join(map(str, lista_aux))
										lista_ip_bin[x] = var
										lista_aux = []
									# ***********************************************************

									break
								else:
									print('Cuarto octeto invalido favor de verificar.')	
							else:
								print('Tercer octeto invalido favor de verificar.')
						else:
							print('Segundo octeto invalido favor de verificar.')
					else:
						print('\nIp no valida o primer octeto fuera de rango favor de verificar.\n')
					# ***********************************************************

				except ValueError:
					print('\nIP no valida favor de verificar.\n')

			# lista de retorno al validar la ip regresara dos listas una en binario,otra en decimal y un tercer elemnto la ip en str**
			lis_ip_binint = []
			lis_ip_binint.append(lista_ip_bin)
			lis_ip_binint.append(lista_ip_int)
			lis_ip_binint.append(str_ip)
			return lis_ip_binint
				# *****************************************************************************************

		def clase_ip(lista_bin, str_ip):
			# conocer la clase de la ip. ********************************
			octeto_uno_bin = lista_bin[0]
			if octeto_uno_bin[0] == '0':
				print('\n\tLa ip',str_ip,' es clase A su mascara por defecto es: 255.0.0.0 /8\n')
			elif octeto_uno_bin[0] == '1' and octeto_uno_bin[1] == '0':
				print('\n\tLa ip',str_ip,' es clase B su mascara por defecto es: 255.255.0.0 /16\n')
			elif octeto_uno_bin[0] == '1' and octeto_uno_bin[1] == '1' and octeto_uno_bin[2] == '0':
				print('\n\tLa ip',str_ip,' es clase C su mascara por defecto es: 255.255.255.0 /24\n')
			elif octeto_uno_bin[0] == '1' and octeto_uno_bin[1] == '1' and octeto_uno_bin[2] == '1' and octeto_uno_bin[3] == '0':
				print('\n\tLa ip',str_ip,' es clase D generalmente estas IP\'s estan reservadas para multicast.\n')
			elif octeto_uno_bin[0] == '1' and octeto_uno_bin[1] == '1' and octeto_uno_bin[2] == '1' and octeto_uno_bin[3] == '1':
				print('\n\tLa ip',str_ip,' es clase E generalmente estas IP\'s estan reservadas para investigación.\n')
			# ***********************************************************



		if self.opc == 1:
			variable = valida_ip()
			clase_ip(variable[0], variable[2])
