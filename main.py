from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import codecs
import textwrap
import json
import os

#nombre de los PDFs y mensaje el secreto
nombre_pdf = input('nombre del pdf: ') + '.pdf'
nombre_pdf2 = input('nombre del segundo pdf: ') + '.pdf'
mensaje = input('mensaje secreto: ')

#cifrado con rot13 (proximamente algo mejor)
mensaje_codificado = codecs.encode(mensaje, 'rot_13')

#filtrando las letras
#-------------------------------
lista1=[]
lista2=[]
for i, letra in enumerate(mensaje_codificado):
	if i % 2 == 0:
		lista1.append(letra)
	else:
		lista2.append(letra)
#-------------------------------
with open('configuracion.json', 'r') as f:
	configuracion = json.load(f)
downloads = f"{configuracion['ruta']}{nombre_pdf}"
pdf_dir = f'PDFs/{nombre_pdf}'

downloads2 = f"{configuracion['ruta']}{nombre_pdf2}"
pdf_dir2 = f'PDFs/{nombre_pdf2}'

#posiciones
cantidad = len(lista1)
posicion_x = 100
posiciones = []

for i in range(cantidad):
        posiciones.append((posicion_x,200))
        posicion_x += 20

cantidad = len(lista2)
posicion_x2 = 110
posiciones2 = []

for i in range(cantidad):
        posiciones2.append((posicion_x2,200))
        posicion_x2 += 20

#texto
texto_random = configuracion['texto']

#crear PDF
for ruta in [downloads, pdf_dir]:
	pdf = canvas.Canvas(ruta)
	text_obj = pdf.beginText(100, 750)
	text_obj.setFont("Helvetica", 12)

#cortar automáticamente por ancho y que siga el texto abajo
	lineas = textwrap.wrap(texto_random,80)
	for linea in lineas:
		text_obj.textLine(linea)

	pdf.drawText(text_obj)
	pdf.showPage()

	for letra, (x,y) in zip(lista1, posiciones):
		pdf.drawString(x, y, letra)

	pdf.showPage()

	pdf.save()

#segundo pdf 
for ruta in [downloads2, pdf_dir2]:
	pdf = canvas.Canvas(ruta)
	text_obj = pdf.beginText(100, 750)   # posición ini>
	text_obj.setFont("Helvetica", 12)

#corte del texto por ancho (como el primer pdf)
	lineas = textwrap.wrap(texto_random,80)
	for linea in lineas:
		text_obj.textLine(linea)
	pdf.drawText(text_obj)
	pdf.showPage()

	for letra, (x,y) in zip(lista2, posiciones2):
		pdf.drawString(x, y, letra)
	pdf.showPage()
	pdf.save()
