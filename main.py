from app.pdf.reader_pdf import extraer_texto_de_pdf

ruta_pdf = "data/Hoja_de_Respuestas_diligenciado_OMIA.pdf"
texto = extraer_texto_de_pdf(ruta_pdf)

for pagina in texto:
    print(pagina)
