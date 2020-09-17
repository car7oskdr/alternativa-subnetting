class clases_ip():

	def __init__(self, str_ip, claseIp, opc):

		self.str_ip = str_ip
		self.claseIp = claseIp
		self.opc = opc

		# especifica la clase de la ip *****
		def especifica_ip(clase, str_ip):

			if clase == 1:
				print('\n\tLa ip',str_ip,' es clase A su mascara por defecto es: 255.0.0.0 /8\n')
			elif clase == 2:
				print('\n\tLa ip',str_ip,' es clase B su mascara por defecto es: 255.255.0.0 /16\n')
			elif clase == 3:
				print('\n\tLa ip',str_ip,' es clase C su mascara por defecto es: 255.255.255.0 /24\n')
			elif clase == 4:
				print('\n\tLa ip',str_ip,' es clase D generalmente estas IP\'s estan reservadas para multicast.\n')
			else:
				print('\n\tLa ip',str_ip,' es clase E generalmente estas IP\'s estan reservadas para investigación.\n')
		# **********************************

		if self.opc == 1:
			especifica_ip(self.claseIp, self.str_ip)