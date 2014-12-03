#coding: utf-8
import os
import random
import time 
from random import randint
import sys , traceback
class jugador(object): # mi clase que ejecuata la opcion de un solo jugador 
	def __init__(self):
		pass
	def inicio(self):
		valida = False
		while (valida == False): #verificara si el nombre de usario no puede estar bacio
			player = raw_input("Ingrese nombre: ")
			if len(player)==0:
				print "No puede dejar el nombre vacio"
				valida = False
			else:
				print "Nombre ingresado exitosamente"
				valida = True
		
		time.sleep(2)
		if sys.platform == "linux" or sys.platform == "linux2": 
			os.system("clear")
		elif sys.platform == "win32":   #segun esl sistema operatibo ejecuatara cls o clear
			os.system("cls")
		print "Comienza"
		print " "
		tablero = []
		for x in range(1,21):
		  tablero.append(["O"] * 20) #mi tablero

		def print_tablero(tablero):
			a = -1
			for fila in tablero:
				a += 1
				print a,"\t","/","I","||".join(fila),"I","/  ",a

		print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
		print_tablero(tablero)
		print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"

		def fila_aleatoria(tablero):
			return random.randint(0,len(tablero)-1)
		def columna_aleatoria(tablero): #numeros ramdom
			return random.randint(0,len(tablero[0])-1)
			

		barco_fila = fila_aleatoria(tablero) #aqui esta mis barcos pequeños
		barco_col = columna_aleatoria(tablero) 
		barco_fila2 = fila_aleatoria(tablero)
		barco_col2 = columna_aleatoria(tablero)

		barcog = columna_aleatoria(tablero) #las columnas de mis barco grande y mediano
		barcof =  columna_aleatoria(tablero)
		
		cod =  randint(0,15)
		cod2 = cod + 1    #aqui esta las partes de mis barcos medianos 
		codf = "%d%d" % (cod, cod2)
		
		code =  randint(0,15) #aqui estan las partes de mi barco mas grande
		code2 = code+1
		code3 = code2 + 1
		code4 = code3 + 1
		codef = "%d%d%d%d" % (code,code2,code3,code4)
		
		barco_fila3 = fila_aleatoria(tablero)
		barco_col3 = columna_aleatoria(tablero) #donde se guarda en variables la posivion de mis barcos peuqeños
		
		barco_fila4 = fila_aleatoria(tablero)
		barco_col4 = columna_aleatoria(tablero)
		
		if barco_fila != barco_fila2 or barco_fila != code:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code2:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code3:
			barco_fila = fila_aleatoria(tablero)



		barcog = columna_aleatoria(tablero) #las columnas de mis barco grande y mediano
		barcof =  columna_aleatoria(tablero)
		
		cod =  randint(0,15)
		cod2 = cod + 1    #aqui esta las partes de mis barcos medianos 
		codf = "%d%d" % (cod, cod2)
		
		code =  randint(0,15) #aqui estan las partes de mi barco mas grande
		code2 = code+1
		code3 = code2 + 1
		code4 = code3 + 1
		codef = "%d%d%d%d" % (code,code2,code3,code4)
		
		barco_fila3 = fila_aleatoria(tablero)
		barco_col3 = columna_aleatoria(tablero) #donde se guarda en variables la posivion de mis barcos peuqeños
		
		barco_fila4 = fila_aleatoria(tablero)
		barco_col4 = columna_aleatoria(tablero)
		
		if barco_fila != barco_fila2 or barco_fila != code:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code2:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code3:
			barco_fila = fila_aleatoria(tablero)

		elif cod != code4:
			cod =  randint(0,15)
		elif barco_fila3 !=  barco_fila:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  barco_fila2:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  barco_fila4:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code2:
			barco_fila3 = fila_aleatoria(tablero)    #se va comparar q los barcos no caigan en el mismo lugar
		elif barco_fila3 !=  code3:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code4:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila4 !=  barco_fila:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  barco_fila2:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  code:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  code2:
			barco_fila4 = fila_aleatoria(tablero)   #se va comparar q los barcos no caigan en el mismo lugar
		elif barco_fila4 !=  code3:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 != code4:
			barco_fila4= fila_aleatoria(tablero)

		turno = 0 #turno 
		barco = 0 # cuenta puntos
		barcop = 0 # cuenta puntos
		barp = 0# cuenta puntos
		barp2 = 0# cuenta puntos
		barm=0   #variables contadores y de los putos de los barcos undidos
		barmp=0 # cuenta puntos
		bar = barm + barmp
		def limpiador():
			if sys.platform == "linux" or sys.platform == "linux2": 
				os.system("clear")
			elif sys.platform == "win32":   #limpiador de ventana
				os.system("cls")

		for turno in range(10): #comenzara mis 10 turnos 
			valida = False
			while (valida == False):
				try:
					adivina_fila = raw_input("Adivina fila:")
					adivina_columna = raw_input("Adivina columna:") #donde se ingresa la donde vamos adivinar los tiros
					if len(adivina_fila)==0:
						print "No puede dejar el numero vacio" # verifica que no este basio 
						valida = False
					elif int(adivina_fila)<0:
						valida = False
						print "no puede ser negativo"
					elif int(adivina_columna)<0:
						valida = False
						print "no puede ser negativo"
					elif (str(adivina_fila).isalpha()==True): #verifivara que solo ingresen numeros
						valida = False
						print "No puedes ingresar letras"
					elif len(adivina_columna)==0:
						print "No puedes dejar el numero vacio"
					elif (str(adivina_fila).isalpha()==True):
						valida = False
						print "no puedes ingresar letras"
					else:
						#print "Numero ingresado exitosamente"
						valida = True

				except ValueError:
					valida = False
					print "asd"
			limpiador()

			adivina_fila = int(adivina_fila)
			adivina_columna = int(adivina_columna) #convierte mis nuemero en enteros
			if adivina_fila == code  and adivina_columna == barcog: #aqui ya empieza verificar si undo o no mis barcos
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero[adivina_fila][adivina_columna] = "x" # marcara con una donde fue impactado mi barco 
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /" #donde me imprime mi tablero 
				barco += 1
				barcop += 1 # va sumando los puntos donde cuenta los puntos y las partes de los barcos 

			elif adivina_fila == code2 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barcop += 1
			elif adivina_fila == code3 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()	#limpiador de ventana segun sea el sistema operativo 
				print "Le diste una parte de mi barco mas grande"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barcop += 1

			elif adivina_fila == code4 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()
				print "Le diste una ala parte principal de mi barco"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 4
				barcop += 1
				print """


                                                     db              
                                                                      
`7M'   `MF',pW"Wq.`7MM  `7MM      `7M'    ,A    `MF'`7MM  `7MMpMMMb.  
  VA   ,V 6W'   `Wb MM    MM        VA   ,VAA   ,V    MM    MM    MM  
   VA ,V  8M     M8 MM    MM         VA ,V  VA ,V     MM    MM    MM  
    VVV   YA.   ,A9 MM    MM          VVV    VVV      MM    MM    MM  
    ,V     `Ybmd9'  `Mbod"YML.         W      W     .JMML..JMML  JMML.
   ,V                                                                 
OOb"                                                                  



"""
				#aqui si le atina ala parte principal ganaara
				#self.inicio()
				break
			elif adivina_fila == barco_fila2  and  adivina_columna == barco_col2:
				time.sleep(2)
				limpiador()
				print "¡¡oohh no!! hundiste unos de mis barcos pequenios"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barp += 1					
			elif adivina_fila == barco_fila and  adivina_columna == barco_col:
				time.sleep(2)
				limpiador()	

				print "¡¡oohh no!! hundiste unos de mis barcos pequenios"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barp += 1
			elif adivina_fila == code4 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()	
				print "Le diste una a la parte principal de mi barco"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1

			elif adivina_fila == cod and adivina_columna == barcof:
				time.sleep(2)
				limpiador()	

				print "Le diste una parte a unos de mis barcos medianos"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barm += 1
			elif adivina_fila == cod2 and adivina_columna == barcof:
				limpiador()

				print "Le diste una parte  principal de mi barco mediano"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 3
				barmp += 1

			elif adivina_fila == barco_fila3  and  adivina_columna == barco_col3:
				time.sleep(2)
				limpiador()

				print "¡¡oohh no!! hundiste unos de mis barcos pequeños"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barp2 += 1

			elif adivina_fila == barco_fila4 and  adivina_columna == barco_col4:
				time.sleep(2)
				limpiador()

				print "¡¡oohh no!! hundiste unos de mis barcos pequeños"
				tablero[adivina_fila][adivina_columna] = "x"
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				barco += 1
				barp+= 1

			else:
				valida = False
				while valida == False:
					try:
						if adivina_fila >= 20  or  adivina_columna >= 20:
							print "Fuera de rango"
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print_tablero(tablero)
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							valida = True  #verificara que no este fuera de rango 
						else:
							print u"No impactaste mi barco!"
							tablero[adivina_fila][adivina_columna] = "#"
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print_tablero(tablero)
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							turno = turno + 1
							print "Su numero de turno es ",str(turno),"de 10"
							valida = True
					except ValueError:
						print "No símbolos"
						valida = False
				if turno == 10:
					print u"Terminó el juego"  #me dira mis resultados al finalizar con su 10 turnos
					print "jugador %s" % player
					print "De mis 6 barcos que tengo en mi tablero \nmi barco principal de 4 casillas \n4 barcos pequeños \n1 barco mediano"
					if  barco >= 0:
						print "Usted logró obtener %d puntos" % barco
					if barcop == 4:
						print "Hundiste todo mi barco principal "
					elif barcop == 3:
						print "Sólo le diste a 3 partes de mi barco principal"
					elif barcop == 2:
						print "Sólo le diste a 2 partes de mi barco principal"
					elif barcop == 1:
						print "Sólo le diste a 1 parte de mi barco principal"
					else: 
						print "No le diste a ninguna parte de mi barco principal"
					if barp == 1:
						print "Sólo le diste a uno de mis barcos pequeños"
					elif barp == 2:
						print "Le diste a mis dos barcos pequeño"
					elif barp == 3:
						print "Le diste a 3 de mis barcos pequeños"
					elif barp == 4:
						print "Le diste a 4 de mis barcos pequeños"
					else:
						print "No le diste a ninguno de mis barcos pequeños"
					if barm == 1:
						print "Le diste a una parte de mi barco mediano"
					elif barmp == 1:
						print "Le diste a la parte principal de mi barco mediano"
					elif bar == 2:
						print "Hundiste mi barco mediano completamente"
					else:
						print "No Hundiste mi barco mediano"
						time.sleep(15)
						limpiador()
					print """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
"""


class jugadores2(object): #aqui llamara al modo multi player
	def __init_(self):
		pass
	def inicio(self):
		valida = False
		while (valida == False): #verificara si el nombre de usario no puede estar bacio
			player = raw_input("Ingrese nombre player 1: ")
			if len(player)==0:
				print "No puede dejar el nombre vacio"
				valida = False
			else:
				print "Nombre ingresado exitosamente"
				while (valida == False):
					player2 = raw_input("Ingrese nombbre de player 2 ")
					if len(player2)==0:
						print "No puede dejar el nombre vaCio"
						valida = False
					else:
						print "Nombre ingresado exitosamente"
						valida = True
			time.sleep(2)
			if sys.platform == "linux" or sys.platform == "linux2": 
				os.system("clear")
			elif sys.platform == "win32":   #segun esl sistema operatibo ejecuatara cls o clear
				os.system("cls")

		tablero = [] #tablero del jugador 2
		tablero2 = [] #tablero del las posiciones del jugador 2
		tablero3 = [] # tablero del jugador 1
		tablero4 = [] # tablero del las posinones del jugador 1
		for x in range(1,21):
			tablero.append(["O"] * 20)
			tablero2.append(["O"] * 20)   #mi tablero
			tablero3.append(["O"] * 20) 
			tablero4.append(["O"] * 20) 
		def print_tablero(tablero):
			a = -1
			for fila in tablero:
				a += 1
				print a,"\t","/","I","||".join(fila),"I","/  ",a
		print_tablero(tablero)

		print "/"*40
		def print_tablero2(tablero2):
			a = -1
			for fila2 in tablero2:
				a += 1
				print a,"\t","/","I","||".join(fila2),"I","/  ",a
		print_tablero2(tablero2)
		print "/"*40

		def print_tablero3(tablero3):
			a = -1
			for fila3 in tablero3:
				a += 1
				print a,"\t","/","I","||".join(fila3),"I","/  ",a
		print_tablero3(tablero3)

		print "/"*40
		def print_tablero4(tablero4):
			a = -1
			for fila4 in tablero4:
				a += 1
				print a,"\t","/","I","||".join(fila4),"I","/  ",a
		print_tablero4(tablero4)
		print "/"*40

		def fila_aleatoria(tablero):
			return random.randint(0,len(tablero)-1)
		def columna_aleatoria(tablero): #numeros ramdom
			return random.randint(0,len(tablero[0])-1)
			


#////////////////////////////////////////////////////////barcos de 4 espacios//////////////////////////////////////////////////////
		code =  randint(0,15)
		code2 = code+1
		code3 = code2 + 1
		code4 = code3 + 1
		codef = "%d%d%d%d" % (code,code2,code3,code4)

		barcoc4 = randint(0,15)
		barcoc4_2= barcoc4 + 1
		barcoc4_3= barcoc4_2+1
		barcoc4_4=barcoc4_3+1
		barcolum4 = columna_aleatoria(tablero)

		barcoc42 = randint(0,15)
		barcoc42_2= barcoc42 + 1
		barcoc42_3= barcoc42_2+1
		barcoc42_4=barcoc42_3+1
		barcolum4_2 = columna_aleatoria(tablero)


		barcoc43 = randint(0,15)
		barcoc43_2= barcoc43 + 1
		barcoc43_3= barcoc43_2+1
		barcoc43_4=barcoc43_3+1
		barcolum4_3 = columna_aleatoria(tablero)



		barcoc44 = randint(0,15)
		barcoc44_2= barcoc44 + 1
		barcoc44_3= barcoc44_2+1
		barcoc44_4=barcoc44_3+1
		barcolum4_4 = columna_aleatoria(tablero)


		barcoc45 = randint(0,15)
		barcoc45_2= barcoc45 + 1
		barcoc45_3= barcoc45_2+1
		barcoc45_4=barcoc45_3+1
		barcolum4_5 = columna_aleatoria(tablero)


		barcoc46 = randint(0,15)
		barcoc46_2= barcoc46 + 1
		barcoc46_3= barcoc46_2+1
		barcoc46_4=barcoc46_3+1
		barcolum4_6 = columna_aleatoria(tablero)


		barcoc47 = randint(0,15)
		barcoc47_2= barcoc47 + 1
		barcoc47_3= barcoc47_2+1
		barcoc47_4=barcoc47_3+1
		barcolum4_7 = columna_aleatoria(tablero)


		barcoc48 = randint(0,15)
		barcoc48_2= barcoc48 + 1
		barcoc48_3= barcoc48_2+1
		barcoc48_4=barcoc48_3+1
		barcolum4_8 = columna_aleatoria(tablero)


		barcoc49 = randint(0,15)
		barcoc49_2= barcoc49 + 1
		barcoc49_3= barcoc49_2+1
		barcoc49_4=barcoc49_3+1
		barcolum4_9 = columna_aleatoria(tablero)


		barcoc410 = randint(0,15)
		barcoc410_2= barcoc410 + 1
		barcoc410_3= barcoc410_2+1
		barcoc410_4=barcoc410_3+1
		barcolum4_10 = columna_aleatoria(tablero)


		barcoc411 = randint(0,15)
		barcoc411_2= barcoc411 + 1
		barcoc411_3= barcoc411_2+1
		barcoc411_4=barcoc411_3+1
		barcolum4_11 = columna_aleatoria(tablero)


		barcoc412 = randint(0,15)
		barcoc412_2= barcoc412 + 1
		barcoc412_3= barcoc412_2+1
		barcoc412_4=barcoc412_3+1
		barcolum4_12 = columna_aleatoria(tablero)

		barcoc413 = randint(0,15)
		barcoc413_2= barcoc413 + 1
		barcoc413_3= barcoc413_2+1
		barcoc413_4=barcoc413_3+1
		barcolum4_13 = columna_aleatoria(tablero)

		barcoc414 = randint(0,15)
		barcoc414_2= barcoc414 + 1
		barcoc414_3= barcoc414_2+1
		barcoc414_4=barcoc414_3+1
		barcolum4_14 = columna_aleatoria(tablero)
#///////////////////////////////////////////////////barcos de 5 casillas////////////////////////////////////////////////////////////////////

		co =  randint(0,15)
		co2 = co+1
		co3 = co2 + 1
		co4 = co3 + 1
		co5 = co4 + 1
		#cof = "%d%d%d%d" % (co,co2,co3,co4,co5)
		coof= fila_aleatoria(tablero)

		barcoc51 = randint(0,15)
		barcoc51_2 = barcoc51 + 1
		barcoc51_3 = barcoc51_2 +1
		barcoc51_4 = barcoc51_3+1
		barcoc51_5 = barcoc51_4 +1
		barcolum5 = columna_aleatoria(tablero)

		barcoc52 = randint(0,15)
		barcoc52_2 = barcoc52 + 1
		barcoc52_3 = barcoc52_2 +1
		barcoc52_4 = barcoc52_3+1
		barcoc52_5 = barcoc52_4 +1
		barcolum5_2 = columna_aleatoria(tablero)

		barcoc53 = randint(0,15)
		barcoc53_2 = barcoc53 + 1
		barcoc53_3 = barcoc53_2 +1
		barcoc53_4 = barcoc53_3+1
		barcoc53_5 = barcoc53_4 +1
		barcolum5_3 = columna_aleatoria(tablero)

		barcoc53 = randint(0,15)
		barcoc53_2 = barcoc53 + 1
		barcoc53_3 = barcoc53_2 +1
		barcoc53_4 = barcoc53_3+1
		barcoc53_5 = barcoc53_4 +1
		barcolum5_3 = columna_aleatoria(tablero)

		barcoc54 = randint(0,15)
		barcoc54_2 = barcoc54 + 1
		barcoc54_3 = barcoc54_2 +1
		barcoc54_4 = barcoc54_3+1
		barcoc54_5 = barcoc54_4 +1
		barcolum5_4 = columna_aleatoria(tablero)

		barcoc55 = randint(0,15)
		barcoc55_2 = barcoc55 + 1
		barcoc55_3 = barcoc55_2 +1
		barcoc55_4 = barcoc55_3+1
		barcoc55_5 = barcoc55_4 +1
		barcolum5_5 = columna_aleatoria(tablero)

		barcoc56 = randint(0,15)
		barcoc56_2 = barcoc56 + 1
		barcoc56_3 = barcoc56_2 +1
		barcoc56_4 = barcoc56_3+1
		barcoc56_5 = barcoc56_4 +1
		barcolum5_6 = columna_aleatoria(tablero)

		barcoc57 = randint(0,15)
		barcoc57_2 = barcoc57 + 1
		barcoc57_3 = barcoc57_2 +1
		barcoc57_4 = barcoc57_3+1
		barcoc57_5 = barcoc57_4 +1
		barcolum5_7 = columna_aleatoria(tablero)

		barcoc58 = randint(0,15)
		barcoc58_2 = barcoc58 + 1
		barcoc58_3 = barcoc58_2 +1
		barcoc58_4 = barcoc58_3+1
		barcoc58_5 = barcoc58_4 +1
		barcolum5_8 = columna_aleatoria(tablero)

		barcoc59 = randint(0,15)
		barcoc59_2 = barcoc59 + 1
		barcoc59_3 = barcoc59_2 +1
		barcoc59_4 = barcoc59_3+1
		barcoc59_5 = barcoc59_4 +1
		barcolum5_9 = columna_aleatoria(tablero)

		barcoc510 = randint(0,15)
		barcoc510_2 = barcoc510 + 1
		barcoc510_3 = barcoc510_2 +1
		barcoc510_4 = barcoc510_3+1
		barcoc510_5 = barcoc510_4 +1
		barcolum5_10 = columna_aleatoria(tablero)

		barcoc511 = randint(0,15)
		barcoc511_2 = barcoc511 + 1
		barcoc511_3 = barcoc511_2 +1
		barcoc511_4 = barcoc511_3+1
		barcoc511_5 = barcoc511_4 +1
		barcolum5_11 = columna_aleatoria(tablero)

		barcoc512 = randint(0,15)
		barcoc512_2 = barcoc512 + 1
		barcoc512_3 = barcoc512_2 +1
		barcoc512_4 = barcoc512_3+1
		barcoc512_5 = barcoc512_4 +1
		barcolum5_12 = columna_aleatoria(tablero)

		barcoc513 = randint(0,15)
		barcoc513_2 = barcoc513 + 1
		barcoc513_3 = barcoc513_2 +1
		barcoc513_4 = barcoc513_3+1
		barcoc513_5 = barcoc513_4 +1
		barcolum5_13 = columna_aleatoria(tablero)

		barcoc514 = randint(0,15)
		barcoc514_2 = barcoc514 + 1
		barcoc514_3 = barcoc514_2 +1
		barcoc514_4 = barcoc514_3+1
		barcoc514_5 = barcoc514_4 +1
		barcolum5_14 = columna_aleatoria(tablero)

		barcoc515 = randint(0,15)
		barcoc515_2 = barcoc515 + 1
		barcoc515_3 = barcoc515_2 +1
		barcoc515_4 = barcoc515_3+1
		barcoc515_5 = barcoc515_4 +1
		barcolum5_15 = columna_aleatoria(tablero)

		barcoc516 = randint(0,15)
		barcoc516_2 = barcoc516 + 1
		barcoc516_3 = barcoc516_2 +1
		barcoc516_4 = barcoc516_3+1
		barcoc516_5 = barcoc516_4 +1
		barcolum5_16 = columna_aleatoria(tablero)

		barcoc517 = randint(0,15)
		barcoc517_2 = barcoc517 + 1
		barcoc517_3 = barcoc517_2 +1
		barcoc517_4 = barcoc517_3+1
		barcoc517_5 = barcoc517_4 +1
		barcolum5_17 = columna_aleatoria(tablero)

		barcoc518 = randint(0,15)
		barcoc518_2 = barcoc518 + 1
		barcoc518_3 = barcoc518_2 +1
		barcoc518_4 = barcoc518_3+1
		barcoc518_5 = barcoc518_4 +1
		barcolum5_18 = columna_aleatoria(tablero)

		barcoc519 = randint(0,15)
		barcoc519_2 = barcoc519 + 1
		barcoc519_3 = barcoc519_2 +1
		barcoc519_4 = barcoc519_3+1
		barcoc519_5 = barcoc519_4 +1
		barcolum5_19 = columna_aleatoria(tablero)
#//////////////////////////////////////////////barco de 2 casillas////////////////////////////////////////////////////////////////////////
		barcoc22 = randint(0,15)
		barcoc22_2 = barcoc22 + 1
		barcolum2 = columna_aleatoria(tablero)

		barcoc23 = randint(0,15)
		barcoc23_2 = barcoc23 + 1
		barcolum2_3 = columna_aleatoria(tablero)

		barcoc24 = randint(0,15)
		barcoc24_2 = barcoc4 + 1
		barcolum2_4 = columna_aleatoria(tablero)

		barcoc25 = randint(0,15)
		barcoc25_2 = barcoc25 + 1
		barcolum2_5 = columna_aleatoria(tablero)

		barcoc26 = randint(0,15)
		barcoc26_2 = barcoc26 + 1
		barcolum2_6 = columna_aleatoria(tablero)

		barcoc27 = randint(0,15)
		barcoc27_2 = barcoc27 + 1
		barcolum2_7 = columna_aleatoria(tablero)

		barcoc28 = randint(0,15)
		barcoc28_2 = barcoc28 + 1
		barcolum2_8 = columna_aleatoria(tablero)

		barcoc29 = randint(0,15)
		barcoc29_2 = barcoc29 + 1
		barcolum2_9 = columna_aleatoria(tablero)

		cod =  randint(0,15)
		cod2 = cod + 1
		codf = "%d%d" % (cod, cod2)
#///////////////////////////////////////////barcos de una casilla/////////////////////////////////////////////////////////////////////
		barco_fila = fila_aleatoria(tablero)
		barco_col = columna_aleatoria(tablero) #donde se guardaran en varibles los numeros ramdom

		barco_fila2 = fila_aleatoria(tablero)
		barco_col2 = columna_aleatoria(tablero)

		barcog = columna_aleatoria(tablero)
		barcof =  columna_aleatoria(tablero)

		barco_fila3 = fila_aleatoria(tablero)
		barco_col3 = columna_aleatoria(tablero) #donde se guarda en variables la posivion de mis barcos

		barco_fila4 = fila_aleatoria(tablero)
		barco_col4 = columna_aleatoria(tablero)

		barco_fila5 = fila_aleatoria(tablero)
		barco_col5 = columna_aleatoria(tablero)

		barco_fila6 = fila_aleatoria(tablero)
		barco_col6 = columna_aleatoria(tablero)

		barco_fila7 = fila_aleatoria(tablero)
		barco_col7 = columna_aleatoria(tablero)

		barco_fila8 = fila_aleatoria(tablero)
		barco_col8 = columna_aleatoria(tablero)

		barco_fila9 = fila_aleatoria(tablero)
		barco_col9 = columna_aleatoria(tablero)

		barco_fila10 = fila_aleatoria(tablero)
		barco_col10 = columna_aleatoria(tablero)
#///////////////////////////////////////////////////////barco principal///////////////////////////////////////////////////////////////


		if barco_fila != barco_fila2 or barco_fila != code:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code2:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code3:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != code4:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != cod:
			barco_fila = fila_aleatoria(tablero)
		elif barco_fila != cod2:
			barco_fila = fila_aleatoria(tablero)   #se va comparar q los barcos no caigan en el mismo lugar
		elif barco_fila2 != cod:
			barco_fila2 = fila_aleatoria(tablero)
		elif barco_fila2 != cod2:
			barco_fila2 = fila_aleatoria(tablero)
		elif barco_fila2 != code:
			barco_fila2 = fila_aleatoria(tablero)
		elif barco_fila2 != code2:
			barco_fila2 = fila_aleatoria(tablero)
		elif barco_fila2 != code3:
			barco_fila2 = fila_aleatoria(tablero)	
		elif barco_fila2 != code4:
			barco_fila2 = fila_aleatoria(tablero)
		elif barco_fila != barco_fila2:
			barco_fila = fila_aleatoria(tablero)
		elif barco_col != barco_col2:
			barco_col = columna_aleatoria(tablero)
			
		elif cod != code:
			cod =  randint(0,15)
		elif cod != code2:
			cod =  randint(0,15)
		elif cod != code3:
			cod =  randint(0,15)
		elif cod != code4:
			cod =  randint(0,15)
		elif barco_fila3 !=  barco_fila:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  barco_fila2:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  barco_fila4:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code2:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code3:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila3 !=  code4:
			barco_fila3 = fila_aleatoria(tablero)
		elif barco_fila4 !=  barco_fila:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  barco_fila2:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  code:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  code2:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 !=  code3:
			barco_fila4 = fila_aleatoria(tablero)
		elif barco_fila4 != code4:
			barco_fila4= fila_aleatoria(tablero)
			

		tablero2[barco_fila][barco_col] = "B"
		tablero2[barco_fila2][barco_col2] = "B"
		tablero2[barco_fila3][barco_col3] = "B"
		tablero2[barco_fila4][barco_col4] = "B"
		tablero2[cod][barcof] = "B"
		tablero2[cod2][barcof] = "B"
		tablero2[code][barcog] = "B"
		tablero2[code2][barcog] = "B"
		tablero2[code3][barcog] = "B"
		tablero2[code4][barcog] = "B"

		tablero2[coof][co] = "B"
		tablero2[coof][co2] = "B"
		tablero2[coof][co3] = "B"
		tablero2[coof][co4] = "B"
		tablero2[coof][co5] = "B"



		barco_filap2 = fila_aleatoria(tablero)
		barco_colp2 = columna_aleatoria(tablero) #donde se guardaran en varibles los numeros ramdom

		barco_fila2p2 = fila_aleatoria(tablero)
		barco_col2p2 = columna_aleatoria(tablero)

		barcogp2 = columna_aleatoria(tablero)
		barcofp2 =  columna_aleatoria(tablero)

		codp2 =  randint(0,15)
		cod2p2 = codp2 + 1
		codfp2 = "%d%d" % (cod, cod2)

		codep2 =  randint(0,15)
		code2p2 = codep2+1
		code3p2 = code2p2 + 1
		code4p2 = code3p2 + 1
		codefp2 = "%d%d%d%d" % (code,code2,code3,code4)

		cop2 =  randint(0,15)
		co2p2 = cop2+1
		co3p2 = co2p2+ 1
		co4p2 = co3p2 + 1
		co5p2 = co4p2 + 1
		#cof = "%d%d%d%d" % (co,co2,co3,co4,co5)
		coofp2 = fila_aleatoria(tablero) 

		barco_fila3p2 = fila_aleatoria(tablero)
		barco_col3p2 = columna_aleatoria(tablero) #donde se guarda en variables la posivion de mis barcos

		barco_fila4p2 = fila_aleatoria(tablero)
		barco_col4p2 = columna_aleatoria(tablero)




		if barco_filap2 != barco_fila2p2 or barco_filap2 != codep2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_filap2 != codep2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_filap2 != code2p2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_filap2 != code3p2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_filap2 != code4p2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_filap2 != codp2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_filap2 != cod2p2:
			barco_filap2 = fila_aleatoria(tablero)   #se va comparar q los barcos no caigan en el mismo lugar
		elif barco_fila2p2 != codp2:
			barco_fila2p2 = fila_aleatoria(tablero)
		elif barco_fila2p2 != cod2p2:
			barco_fila2p2 = fila_aleatoria(tablero)
		elif barco_fila2p2 != codep2:
			barco_fila2p2 = fila_aleatoria(tablero)
		elif barco_fila2p2 != code2p2:
			barco_fila2p2 = fila_aleatoria(tablero)
		elif barco_fila2p2 != code3p2:
			barco_fila2p2 = fila_aleatoria(tablero)	
		elif barco_fila2p2 != code4p2:
			barco_fila2p2 = fila_aleatoria(tablero)
		elif barco_filap2 != barco_fila2p2:
			barco_filap2 = fila_aleatoria(tablero)
		elif barco_colp2 != barco_col2p2:
			barco_colp2 = columna_aleatoria(tablero)
			
		elif codp2 != codep2:
			codp2 =  randint(0,15)
		elif codp2 != code2p2:
			codp2 =  randint(0,15)
		elif codp2 != code3p2:
			codp2 =  randint(0,15)
		elif codp2 != code4p2:
			codp2 =  randint(0,15)
		elif barco_fila3p2 !=  barco_filap2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila3p2 !=  barco_fila2p2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila3p2 !=  barco_fila4p2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila3p2 !=  codep2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila3p2 !=  code2p2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila3p2 !=  code3p2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila3p2 !=  code4p2:
			barco_fila3p2 = fila_aleatoria(tablero)
		elif barco_fila4p2 !=  barco_filap2:
			barco_fila4p2 = fila_aleatoria(tablero)
		elif barco_fila4p2 !=  barco_fila2p2:
			barco_fila4p2 = fila_aleatoria(tablero)
		elif barco_fila4p2 !=  codep2:
			barco_fila4p2 = fila_aleatoria(tablero)
		elif barco_fila4p2 !=  code2p2:
			barco_fila4p2 = fila_aleatoria(tablero)
		elif barco_fila4p2 !=  code3p2:
			barco_fila4p2 = fila_aleatoria(tablero)
		elif barco_fila4p2 != code4p2:
			barco_fila4p2= fila_aleatoria(tablero)
			

		tablero4[barco_filap2][barco_colp2] = "B"
		tablero4[barco_fila2p2][barco_col2p2] = "B"
		tablero4[barco_fila3p2][barco_col3p2] = "B"
		tablero4[barco_fila4p2][barco_col4p2] = "B"
		tablero4[codp2][barcofp2] = "B"
		tablero4[cod2p2][barcofp2] = "B"
		tablero4[codep2][barcogp2] = "B"
		tablero4[code2p2][barcogp2] = "B"
		tablero4[code3p2][barcogp2] = "B"
		tablero4[code4p2][barcogp2] = "B"

		tablero4[coofp2][cop2] = "B"
		tablero4[coofp2][co2p2] = "B"
		tablero4[coofp2][co3p2] = "B"
		tablero4[coofp2][co4p2] = "B"
		tablero4[coofp2][co5p2] = "B"




		turnop2 = 0
		barcop2 = 0
		barcopp2 = 0
		barpp2 = 0
		barp2p2 = 0
		barmp2=0   #variables contadores y de los putos de los barcos undidos
		barmpp2=0
		barp2 = barmp2 + barmpp2


		turno = 0
		barco = 0
		barcop = 0
		barp = 0
		barp2 = 0
		barm=0   #variables contadores y de los putos de los barcos undidos
		barmp=0
		bar = barm + barmp
		puntos = 0
		puntos2 = 0
		bp2 = 0
		bp2p2 = 0

		time.sleep(6)
		def limpiador():
			if sys.platform == "linux" or sys.platform == "linux2": 
				os.system("clear")
			elif sys.platform == "win32":   #limpiador de ventana
				os.system("cls")

		limpiador()

		for turno in range(4): #comenzara mis 10 turnos 
			print "/"* 30,"Tablero Enemigo","/"* 30
			print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
			print_tablero(tablero)
			print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
			print "/"* 35,"jugador1","/"* 35
			print_tablero4(tablero4)
			print "Comienza jugador 1"
			valida = False
			while (valida == False):
				try:
					adivina_fila = raw_input("Adivina fila:")
					adivina_columna = raw_input("Adivina columna:") 
					if len(adivina_fila)==0:
						print "no puede dejar el numero Vacio"
						valida = False
					elif int(adivina_fila)<0:
						valida = False
						print "no puede ser negativo"
					elif int(adivina_columna)<0:
						valida = False
						print "no puede ser negativo"
					elif (str(adivina_fila).isalpha()==True): #verifivara que solo ingresen numeros
						valida = False
						print "No puedes ingresar letras"
					elif len(adivina_columna)==0:
						print "No puedes dejar el numero vacio"
					elif (str(adivina_fila).isalpha()==True):
						valida = False
						print "No puedes ingresar letras"
					else:
						#print "Numero ingresado exitosamente"
						valida = True
				except ValueError:
					valida = False
					print "asd"
			limpiador()

			adivina_fila = int(adivina_fila)
			adivina_columna = int(adivina_columna) #convierte mis nuemero en enteros
			if adivina_fila == code  and adivina_columna == barcog: #aqui ya empieza verificar si undo o no mis barcos
				time.sleep(2)
				limpiador()

				print "Le diste una parte de mi barco mas grande"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barcop += 1

			elif adivina_fila == code2 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barcop += 1
			elif adivina_fila == code3 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barcop += 1

			elif adivina_fila == code4 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()	
				print "Le diste una a la parte principal de mi barco"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 4
				barcop += 1
				print """


															 db              
																			  
		`7M'   `MF',pW"Wq.`7MM  `7MM      `7M'    ,A    `MF'`7MM  `7MMpMMMb.  
		  VA   ,V 6W'   `Wb MM    MM        VA   ,VAA   ,V    MM    MM    MM  
		   VA ,V  8M     M8 MM    MM         VA ,V  VA ,V     MM    MM    MM  
			VVV   YA.   ,A9 MM    MM          VVV    VVV      MM    MM    MM  
			,V     `Ybmd9'  `Mbod"YML.         W      W     .JMML..JMML  JMML.
		   ,V                                                                 
		OOb"                                                                  



		"""
				#aqui si le atina ala parte principal ganaara
				#self.inicio()
				break
			elif adivina_fila == co and adivina_columna == coof:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				bp2 += 1
			elif adivina_fila == co2 and adivina_columna == coof:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				bp2 += 1
			elif adivina_fila == co3 and adivina_columna == coof:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				bp2 += 1
			elif adivina_fila == co4 and adivina_columna == coof:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				bp2 += 1
			elif adivina_fila == co5 and adivina_columna == coof:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				bp2 += 1
#---------------------------------------------------
			elif adivina_fila == barco_fila2  and  adivina_columna == barco_col2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barp += 1					
			elif adivina_fila == barco_fila and  adivina_columna == barco_col:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barp += 1
			elif adivina_fila == code4 and adivina_columna == barcog:
				time.sleep(2)
				limpiador()	
				print "Le diste una a la parte principal de mi barco"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1

			elif adivina_fila == cod and adivina_columna == barcof:
				time.sleep(2)
				limpiador()
				print "Le diste una parte a unos de mis barcos medianos"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barm += 1
			elif adivina_fila == cod2 and adivina_columna == barcof:
				time.sleep(2)
				limpiador()
				print "Le diste una parte  principal de mi barco mediano"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 3
				barmp += 1

			elif adivina_fila == barco_fila3  and  adivina_columna == barco_col3:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barp2 += 1

			elif adivina_fila == barco_fila4 and  adivina_columna == barco_col4:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero[adivina_fila][adivina_columna] = "x"
				tablero2[adivina_fila][adivina_columna] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero(tablero)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador1","/"* 35
				print_tablero4(tablero4)
				barco += 1
				barp+= 1

			else:
				valida = False
				while valida == False:
					try:
						if adivina_fila >= 20  or  adivina_columna >= 20:
							print "Fuera de rango"
							print "/"* 30,"Tablero Enemigo","/"* 30
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print_tablero(tablero)
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print "/"* 35,"jugador1","/"* 35
							print_tablero4(tablero4)
							valida = True  #verificara que no este fuera de rango 
						else:
							print u"No impactaste mi barco!"
							tablero[adivina_fila][adivina_columna] = "#"
							tablero2[adivina_fila][adivina_columna] = "#"
							print "/"* 30,"Tablero Enemigo","/"* 30
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print_tablero(tablero)
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print "/"* 35,"jugador1","/"* 35
							print_tablero4(tablero4)
							turno = turno + 1
							print "Su numero de turno es ",str(turno),"de 10"
							valida = True
					except ValueError:
						print "No simbolos"
						valida = False
				time.sleep(9)
				limpiador()
				print "tu turno jugador 2"
				time.sleep(2)
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				
			#/////////////////////////////////////////jugador 2////////////////////////////////////////////////
			valida = False
			while (valida == False):
				try:
					adivina_filap2 = raw_input("Adivina fila:")
					adivina_columnap2 = raw_input("Adivina columna:") 
					if len(adivina_filap2)==0:
						print "No puede dejar el numero vacio"
						valida = False
					elif int(adivina_fila)<0:
						valida = False
						print "no puede ser negativo"
					elif int(adivina_columna)<0:
						valida = False
						print "no puede ser negativo"
					elif (str(adivina_filap2).isalpha()==True): #verifivara que solo ingresen numeros
						valida = False
						print "No puedes ingresar letras"
					elif len(adivina_columnap2)==0:
						print "No puedes dejar el numero vacio"
					elif (str(adivina_filap2).isalpha()==True):
						valida = False
						print "No puedes ingresar letras"
					else:
						#print "Numero ingresado exitosamente"
						valida = True
				except ValueError:
					valida = False
					print "asd"
			limpiador()
			adivina_filap2 = int(adivina_filap2)
			adivina_columnap2 = int(adivina_columnap2) #convierte mis nuemero en enteros
			if adivina_filap2 == codep2  and adivina_columnap2 == barcogp2: #aqui ya empieza verificar si undo o no mis barcos
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barcopp2 += 1

			elif adivina_filap2 == cop2 and adivina_columnap2 == coofp2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				bp2p2 += 1
			elif adivina_filap2 == co2p2 and adivina_columnap2 == coofp2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				bp2p2 += 1
			elif adivina_filap2 == co3p2 and adivina_columnap2 == coofp2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				bp2p2 += 1
			elif adivina_filap2 == co4p2 and adivina_columnap2 == coofp2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				bp2p2 += 1
			elif adivina_filap2 == co5p2 and adivina_columnap2 == coofp2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste una parte de mis barcos grandes"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				bp2p2 += 1

			elif adivina_filap2 == code2p2 and adivina_columnap2 == barcogp2:
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barcopp2 += 1
			elif adivina_filap2 == code3p2 and adivina_columnap2 == barcogp2:
				time.sleep(2)
				limpiador()
				print "Le diste una parte de mi barco mas grande"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)	
				barco += 1
				barcop += 1

			elif adivina_filap2 == code4p2 and adivina_columnap2 == barcogp2:
				time.sleep(2)
				limpiador()
				print "Le diste una a la parte principal de mi barco"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 4
				barcopp2 += 1
				print """


															 db              
																			  
		`7M'   `MF',pW"Wq.`7MM  `7MM      `7M'    ,A    `MF'`7MM  `7MMpMMMb.  
		  VA   ,V 6W'   `Wb MM    MM        VA   ,VAA   ,V    MM    MM    MM  
		   VA ,V  8M     M8 MM    MM         VA ,V  VA ,V     MM    MM    MM  
			VVV   YA.   ,A9 MM    MM          VVV    VVV      MM    MM    MM  
			,V     `Ybmd9'  `Mbod"YML.         W      W     .JMML..JMML  JMML.
		   ,V                                                                 
		OOb"                                                                  



		"""
				#aqui si le atina ala parte principal ganaara
				#self.inicio()
				break

			elif adivina_filap2 == barco_fila2p2  and  adivina_columnap2 == barco_col2p2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barpp2 += 1					
			elif adivina_filap2 == barco_filap2 and  adivina_columnap2 == barco_colp2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barpp2 += 1
			elif adivina_filap2 == code4p2 and adivina_columnap2 == barcogp2:
				time.sleep(2)
				limpiador()
				print "Le diste una a la parte principal de mi barco"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1

			elif adivina_filap2 == codp2 and adivina_columnap2 == barcofp2:
				time.sleep(2)
				limpiador()
				print "Le diste una parte a unos de mis barcos medianos"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barmp2 += 1
			elif adivina_filap2 == cod2p2 and adivina_columnap2 == barcofp2:
				time.sleep(2)
				limpiador()
				print "Le diste una parte  principal de mi barco mediano"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)	
				barcop2 += 3
				barmpp2 += 1

			elif adivina_filap2 == barco_fila3p2  and  adivina_columnap2 == barco_col3p2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barp2p2 += 1

			elif adivina_filap2 == barco_fila4p2 and  adivina_columnap2 == barco_col4p2:
				time.sleep(2)
				limpiador()
				print "¡¡oohhh nooo!! Hundiste unos de mis barcos pequeños"
				tablero3[adivina_filap2][adivina_columnap2] = "x"
				tablero4[adivina_filap2][adivina_columnap2] = "x"
				print "/"* 30,"Tablero Enemigo","/"* 30
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print_tablero3(tablero3)
				print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
				print "/"* 35,"jugador2","/"* 35
				print_tablero2(tablero2)
				barcop2 += 1
				barpp2 += 1

			else:
				valida = False
				while valida == False:
					try:
						if adivina_filap2 >= 20  or  adivina_columnap2 >= 20:
							print "Fuera de rango"
							print "/"* 30,"Tablero Enemigo","/"* 30
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print_tablero3(tablero3)
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print "/"* 35,"jugador2","/"* 35
							print_tablero2(tablero2)
							valida = True  #verificara que no este fuera de rango 
						else:
							print u"No impactaste mi barco!"
							tablero3[adivina_filap2][adivina_columnap2] = "#"
							tablero4[adivina_filap2][adivina_columnap2] = "#"
							print "/"* 30,"Tablero Enemigo","/"* 30
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print_tablero3(tablero3)
							print "\t/   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19   /"
							print "/"* 35,"jugador2","/"* 35
							print_tablero2(tablero2)
							turnop2 = turnop2 + 1
							time.sleep(2)
							limpiador()
							print "Su numero de turno es ",str(turnop2),"de 10"
							valida = True
					except ValueError:
						print "No simbolos"
						valida = False

				if turno == 4:
					print u"Termino el juego"  #me dira mis resultados al finalizar con su 10 turnos
					print "jugador %s" % player
					print "De mis 7 barcos que tengo en mi talblero \nmi barco principal de 4 casillas \nmi otro barco grande de 5 casillas \n4 barcos pequenios \n1 barco mediano"
					puntos += barco
					if  barco > 0:
						print "Usted logro obtener %d puntos" % barco
					if bp2 == 5:
						print "Hundiste todo mi barco mas grande"
					elif bp2 == 4:
						print "Solo le diste a 4 partes de mi barco principal"
					elif bp2 == 3:
						print "Solo le diste a 3 partes de mi barco principal"
					elif bp2== 2:
						print "Solo le diste a 2 partes de mi barco principal"
					elif bp2 == 1:
						print "Solo le diste a 1 parte de mi barco principal"
					else:
						print "no le diste a ninguno de las parte de mi barco"
					if barcop == 4:
						print "Hundiste todo mi barco principal "
					elif barcop == 3:
						print "Solo le diste a 3 partes de mi barco principal"
					elif barcop == 2:
						print "Solo le diste a 2 partes de mi barco principal"
					elif barcop == 1:
						print "Solo le diste a 1 parte de mi barco principal"
					else: 
						print "No le diste a ninguna parte de mi barco principal"
					if barp == 1:
						print "Solo le diste a uno de mis barcos pequeños"
					elif barp == 2:
						print "Le doiste a mis dos barcos pequeño"
					elif barp == 3:
						print "Le diste a 3 de mis barcos pequeños"
					elif barp == 4:
						print "Le diste a 4 de mis barcos pequeños"
					else:
						print "No le diste a ninguno de mis barcos pequeños"
					if barm == 1:
						print "Le diste a una parte de mi barco mediano"
					elif barmp == 1:
						print "le diste ala parte principal de mi barco mediano"
					elif bar == 2:
						print "Hundiste mi barco mediano completamente"
					else:
						print "No Hundiste mi barco mediano"
						time.sleep(5)
						limpiador()
					
		#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
					print u"Termino el juego" 
					puntos2 += barcop2 #me dira mis resultados al finalizar con su 10 turnos
					print "jugador %s" % player2
					print "De mis 7 barcos que tengo en mi talblero \nmi barco principal de 4 casillas \nmi otro barco grande de 5 casillas \n4 barcos pequenios \n1 barco mediano"
					if  barcop2 > 0:
						print "Usted logro obtener %d puntos" % barcop2
					if bp2p2 == 5:
						print "Hundiste todo mi barco mas grande"
					elif bp2p2 == 4:
						print "Solo le diste a 4 partes de mi barco principal"
					elif bp2p2 == 3:
						print "Solo le diste a 3 partes de mi barco principal"
					elif bp2p2== 2:
						print "Solo le diste a 2 partes de mi barco principal"
					elif bp2p2 == 1:
						print "Solo le diste a 1 parte de mi barco principal"
					else:
						print "no le diste a ninguno de las parte de mi barco"
					if barcop == 4:
						print "Hundiste todo mi barco principal "
					elif barcop == 3:
						print "Solo le diste a 3 partes de mi barco principal"
					elif barcop == 2:
						print "Solo le diste a 2 partes de mi barco principal"
					elif barcop == 1:
						print "Solo le diste a 1 parte de mi barco principal"
					else: 
						print "No le diste a ninguna parte de mi barco principal"
					if barcopp2 == 4:
						print "Hundiste todo mi barco principal "
					elif barcopp2 == 3:
						print "Solo le diste a 3 partes de mi barco principal"
					elif barcopp2 == 2:
						print "Solo le diste a 2 partes de mi barco principal"
					elif barcopp2 == 1:
						print "Solo le diste a 1 parte de mi barco principal"
					else: 
						print "No le diste a ninguna parte de mi barco principal"
					if barpp2 == 1:
						print "Solo le diste a uno de mis barcos pequenios"
					elif barpp2 == 2:
						print "Le doiste a mis dos barcos pequeño"
					elif barpp2 == 3:
						print "Le diste a 3 de mis barcos pequeños"
					elif barpp2 == 4:
						print "Le diste a 4 de mis barcos pequeños"
					else:
						print "No le diste a ninguno de mis barcos pequeños"
					if barmp2 == 1:
						print "Le diste a una parte de mi barco mediano"
					elif barmpp2 == 1:
						print "Le diste ala parte principal de mi barco mediano"
					elif barp2 == 2:
						print "Hundiste mi barco mediano completamente"
					else:
						print "No Hundiste mi barco mediano"
						time.sleep(5)
						limpiador()
					if puntos > puntos2:
						print "jugador 1 %s gano por puntos" % player
 					elif puntos < puntos2:
						print "jugador 2 %s gano por puntos" % player2
					else:
						print "jugado1 %s jugador2 %s fue un empate" % (player,player2)

					print """
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
	  ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
													 ░                   
		"""
class instrucciones(object): #saldra del programa
	def __init__(self):
		pass
	def inicio(self):
		limpiador()
		print "Intrucciones:"
		print "1.Usted tendra 10 turnos tanto como un player o multiplayer \n2.Usted ganará cuando hunda todos los barcos o hunda el barco principal de su enemigo \n3.En el modo multiplayer será las misma regla para ganar si ninguno adivina a la parte \nprincipal o hunde todos los barcos el ganador se basará en base de puntos \n4.El rango de disparo será de 0 - 19\n"


class salir(object): #saldra del programa
	def __init__(self):
		pass
	def inicio(self):
		print "Gracias por jugar nuestra batalla naval vuelva pronto"
		sys.exit(0)


menu = {'jugador':jugador, 'jugadores':jugadores2,'salir':salir ,"instrucciones": instrucciones} # el diccionario que guardara y llmara mi menu
"""
while True:
	print "Bienvenido a batalla naval listo para comenzar la batalla?"
	print "Si quiers jugar un player ingresa 'jugador' si quieres jugar multi player ingresa 'jugadores' "
	opcion = raw_input("Ingrese opcion: ")
	varialbe = menu[opcion]()
	print varialbe.inicio()

"""
while True:
	valida = False
	while (valida == False): # while donde va validar si no sepude dejar basio y no me permita agregar otra cosa q no este en las opciones
		print "Bienvenido a batalla naval ¿listo para comenzar la batalla?"
		print "Si quieres jugar un player ingresa 'jugador' si quieres jugar multi player ingresa 'jugadores' Ingresa  Instruciones para mostrar las 'instrucciones'"
		try:
			opcion = raw_input("Ingresa una opcion: \n")
			if len(opcion)==0:
				print "no puede dejar basio"
				valida = False
			elif (str(opcion).isdigit()==True):
				valida = False
				print "no puedes ingresar otra cosa que nosea algunas de las opciones"
			else:
				varialbe = menu[opcion]()
				print varialbe.inicio()
				valida = True
		except KeyError:
			print "no esta ingrensando la opcion bien intenta de nuevo"
			valida = False
