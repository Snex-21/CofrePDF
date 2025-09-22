import os
import json

def presentacion():
	os.system('clear')

	titulo = ' '*25 + 'CofrePDF'

	print('='*60)
	print(titulo)
	print('='*60)
	print(' '*60, '\n')
presentacion()
print('===configuracion inicial===\n')

print('--configuracion sobre la ruta de almacenamiento--\n')
print('por defecto la ruta de almacenamiento  de los PDFs esta en\n/storage/emulated/0/Download/\npara dispositivos adroid pero si estas en otro sistema\noperativo hay que cambiarlo')
print('\ncambiar ruta de almacenamiento?')

def cargar_configuracion():
	if os.path.exists('configuracion.json'):
		with open('configuracion.json', 'r') as f:
			return json.load(f)
	return {}

def guardar_configuracion(config):
	with open('configuracion.json', 'w') as f:
		json.dump(config, f, indent=4)

def guardar_texto(texto):
	print('para los PDFs se necesita un texto que sea menos sospechoso')
	with open('configuracion.json', 'w') as f:
		json.dump(config, f, indent=4)

def Texto():
	print('\n--configuracion del texto falso--')
	print('\ndentro de los PDFs tiene que haber un texto para despistar y que se note menos el mensaje secreto')
	configuracion = cargar_configuracion()
	while True:
		print('cambiar texto predeterminado?')
		confirmacion = input('[y]/[n]  ➜ ').lower()
		if confirmacion == 'y':
			nuevo_texto = input('nuevo texto  ➜ ')
			print(f'el nuevo texto es {nuevo_texto} ?')
			confirmacion2 = input('[y]/[n]  ➜ ').lower()
			if confirmacion2 == 'y':
				configuracion['texto'] = nuevo_texto
				guardar_configuracion(configuracion)
				return nuevo_texto
			elif confirmacion2 == 'n':
				continue
			else:
				print('la respuesta tiene que ser "y" o "n" ')
				continue
		elif confirmacion == 'n':
			print('\nver texto predeterminado? (muy largo)')
			confirmacion3 = input('[y]/[n]  ➜ ').lower()
			if confirmacion3 == 'y':
				texto_predeterminado = """La ciudad dormía, aunque nunca en silencio. Desde la ventana alta de un edificio antiguo, se podía ver el parpadeo constante de las luces lejanas: semáforos cambiando, faroles encendidos, ventanas iluminadas aquí y allá como islas en la oscuridad. El murmullo de motores se mezclaba con algún grito ocasional, un perro ladrando, la vida nocturna latiendo en rincones invisibles. Y sin embargo, en medio de todo eso, había una calma extraña, casi irreal.
El cielo, gris y cargado de nubes, parecía presionar sobre los techos, como si quisiera caer y cubrirlo todo. Pero justo en un claro entre esa inmensidad oscura, una estrella solitaria resistía. Brillaba con terquedad, pequeña y lejana, y cualquiera que la mirara podría pensar que no tenía importancia… salvo para aquel que necesitara una señal.
Allí, en ese cuarto pequeño con paredes despintadas y un escritorio lleno de papeles arrugados, alguien observaba esa estrella como si fuese el último faro del mundo. Tenía los ojos cansados, pero también un fuego dentro, ese tipo de fuego que no quema por fuera, sino que arde en silencio y empuja a seguir. Pensaba en todo lo que había hecho, en lo que había perdido, en lo que aún soñaba. Y, sin saber muy bien por qué, sentía que esa estrella le estaba respondiendo.
No con palabras, claro, pero sí con una certeza: que incluso en la inmensidad de la oscuridad, siempre hay un punto de luz que se niega a apagarse. Que la vida es ese vaivén constante entre la sombra y la claridad, y que uno mismo decide si caminar con la cabeza gacha o levantar la mirada y buscar ese brillo escondido.
Afuera, el viento comenzó a soplar más fuerte. Las hojas secas que quedaban del otoño se arremolinaron en las calles vacías, y un gato cruzó velozmente hacia algún refugio invisible. Las nubes avanzaban pesadas, pero la estrella seguía allí. Y, mientras tanto, la ciudad continuaba respirando: los que reían en bares escondidos, los que lloraban en habitaciones solitarias, los que soñaban dormidos sin saber que compartían el mismo cielo.
El observador, todavía frente a la ventana, respiró hondo. Tal vez mañana todo siguiera igual: los mismos problemas, las mismas dudas, la misma rutina. Pero, por un instante, entendió que había algo más, algo sencillo y profundo al mismo tiempo. Entendió que incluso en la ciudad más ruidosa, en la noche más pesada, podía existir un silencio íntimo, un espacio donde la esperanza brillaba tan obstinada como esa estrella solitaria.
Y con ese pensamiento, cerró los ojos. """
				configuracion['texto'] = texto_predeterminado
				guardar_configuracion(configuracion)
				print(texto_predeterminado)
				return texto_predeterminado
			elif confirmacion3 == 'n': 
				texto_predeterminado = '''La ciudad dormía, aunque nunca en silencio. Desde la ventana alta de un edificio antiguo, se podía ver el parpadeo constante de las luces lejanas: semáforos cambiando, faroles encendidos, ventanas iluminadas aquí y allá como islas en la oscuridad. El murmullo de motores se mezclaba con algún grito ocasional, un perro ladrando, la vida nocturna latiendo en rincones invisibles. Y sin embargo, en medio de todo eso, había una calma extraña, casi irreal.
El cielo, gris y cargado de nubes, parecía presionar sobre los techos, como si quisiera caer y cubrirlo todo. Pero justo en un claro entre esa inmensidad oscura, una estrella solitaria resistía. Brillaba con terquedad, pequeña y lejana, y cualquiera que la mirara podría pensar que no tenía importancia… salvo para aquel que necesitara una señal.
Allí, en ese cuarto pequeño con paredes despintadas y un escritorio lleno de papeles arrugados, alguien observaba esa estrella como si fuese el último faro del mundo. Tenía los ojos cansados, pero también un fuego dentro, ese tipo de fuego que no quema por fuera, sino que arde en silencio y empuja a seguir. Pensaba en todo lo que había hecho, en lo que había perdido, en lo que aún soñaba. Y, sin saber muy bien por qué, sentía que esa estrella le estaba respondiendo.
No con palabras, claro, pero sí con una certeza: que incluso en la inmensidad de la oscuridad, siempre hay un punto de luz que se niega a apagarse. Que la vida es ese vaivén constante entre la sombra y la claridad, y que uno mismo decide si caminar con la cabeza gacha o levantar la mirada y buscar ese brillo escondido.
Afuera, el viento comenzó a soplar más fuerte. Las hojas secas que quedaban del otoño se arremolinaron en las calles vacías, y un gato cruzó velozmente hacia algún refugio invisible. Las nubes avanzaban pesadas, pero la estrella seguía allí. Y, mientras tanto, la ciudad continuaba respirando: los que reían en bares escondidos, los que lloraban en habitaciones solitarias, los que soñaban dormidos sin saber que compartían el mismo cielo.
El observador, todavía frente a la ventana, respiró hondo. Tal vez mañana todo siguiera igual: los mismos problemas, las mismas dudas, la misma rutina. Pero, por un instante, entendió que había algo más, algo sencillo y profundo al mismo tiempo. Entendió que incluso en la ciudad más ruidosa, en la noche más pesada, podía existir un silencio íntimo, un espacio donde la esperanza brillaba tan obstinada como esa estrella solitaria.
Y con ese pensamiento, cerró los ojos.'''
				configuracion['texto'] = texto_predeterminado
				guardar_configuracion(configuracion)
				return texto_predeterminado 
			else:
				print('la respuesta tiene que ser "y" o "n" ')
				continue
		else:
			print('la respuesta tiene que ser "y" o "n" ')
			continue
#--------------------------------------------------------
def Ruta():
	configuracion = cargar_configuracion()
	if 'ruta' in configuracion:
		print(f'\nruta de almacenamiento: {configuracion["ruta"]}')
	while True:
		cambiar = input('[y]/[n] ➜ ').lower()
		if cambiar == 'y':
			while True:
				ruta = input('nueva ruta  ➜ ')
				print(f'la nueva ruta es {ruta} ?')
				confirmacion = input('[y]/[n]  ➜ ').lower()
				if confirmacion == 'y':
					configuracion['ruta'] = ruta
					guardar_configuracion(configuracion)
					return ruta
				elif confirmacion == 'n':
					continue
				else:
					print('la respuesta tiene que ser "y" o "n" ')
					continue

		elif cambiar == 'n':
			ruta = '/storage/emulated/0/Download/'
			configuracion['ruta'] = ruta
			guardar_configuracion(configuracion)
			return ruta
		else:
			print('la respuesta tiene que ser "y" o "n" ')
			continue
#--------------------------------------------------------
Ruta()

Texto()

presentacion()

while True:
	print('\nelegi una opcion:\n1. crear PDFs con el mensaje\n2. fusionar PDFs para revelar el mensaje')
	eleccion = str(input('numero  ➜  '))
	if eleccion == '1':
		os.system('python3 main.py')
		print('detener programa?')
		detener = input('[y]/[n]  ➜ ').lower()
		if detener == 'y':
			break
		elif detener == 'n':
			continue
		else:
			print('la respuesta tiene que ser "y" o "n" ')
	elif eleccion == '2':
		os.system('python3 fusion.py')
		print('detener programa?')
		detener2 = input('[y]/[n]  ➜ ').lower()
		if detener2 == 'y':
			break
		elif detener2 == 'n':
			continue
		else:
			print('la respuesta tiene que ser "y" o "n"')
			continue

	else:
		print('~'*7,'tiene que ser 1 o 2','~'*7)
		continue

