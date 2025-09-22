from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import codecs
import json
import textwrap

with open('configuracion.json', 'r') as f:
	configuracion = json.load(f)

print('para la fusion de los PDFs y la revelacion del mensaje es importante el orden.')
print('tambien es importante que los PDFs esten en la ruta selecionada')
while True:
	nombre_pdf1 = input('nombre del primer PDF  ➜ ') + '.pdf'
	print(f'el primer PDF se llama {nombre_pdf1}?')
	confirmacion = input('[y]/[n]  ➜ ').lower()
	if confirmacion == 'y':
		break
	elif confirmacion == 'n':
		continue
	else:
		print('tiene que ser "y" o "n" ')
		continue
while True:
	nombre_pdf2 = input('nombre del segundo PDF  ➜ ') + '.pdf'
	print(f'el segundo PDF es {nombre_pdf2}?')
	confirmacion2 = input('[y]/[n]  ➜ ')
	if confirmacion2 == 'y':
		break
	elif confirmacion == 'n':
		continue
	else:
		print('tiene quebser "y" o "n" ')
		continue


#ruta de los PDFs
pdf1 = f'PDFs/{nombre_pdf1}'
pdf2 = f'PDFs/{nombre_pdf2}'

#ruta del PDF final
pdf_final = 'PDFs/pdf_abierto.pdf'
ruta_pdf = configuracion['ruta']
pdf_final_interno = f"{ruta_pdf}pdf_abierto.pdf"

#leemos los PDFs
reader1 = PdfReader(pdf1)
reader2 = PdfReader(pdf2)

#extraemos la segunda pagina (donde esta el mensaje)
pagina1 = reader1.pages[1].extract_text()
pagina2 = reader2.pages[1].extract_text()

#reemplazamos el salto en linea por nada
pagina1 = pagina1.replace("\n", "")
pagina2 = pagina2.replace("\n", "")

#descodificamos el mensaje
texto_codificado = ''
for c1, c2 in zip(pagina1, pagina2):
	texto_codificado += c1 + c2
texto_descodificado = codecs.decode(texto_codificado, 'rot_13')

#creamos un PDF con el mensaje
pdf = canvas.Canvas(pdf_final,pagesize=A4)
texto_obj = pdf.beginText(100, 750)
texto_obj.setFont('Helvetica', 12)

lineas = textwrap.wrap(texto_descodificado, 80)
for linea in lineas:
	texto_obj.textLine(linea)
pdf.drawText(texto_obj)
pdf.showPage()
pdf.save()


pdf = canvas.Canvas(pdf_final_interno,pagesize=A4)
texto_obj = pdf.beginText(100, 750)
texto_obj.setFont('Helvetica', 12)

lineas = textwrap.wrap(texto_descodificado, 80)
for linea in lineas:
	texto_obj.textLine(linea)
pdf.drawText(texto_obj)
pdf.showPage()
pdf.save()
