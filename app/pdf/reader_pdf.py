from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

# Ruta del ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\guido.jacome\AppData\Local\Programs\Tesseract-OCR"  # Windows


def extraer_texto_de_pdf(pdf_path):
    """Extrae texto de un archivo PDF utilizando OCR."""
    paginas = convert_from_path(pdf_path, dpi=300)

    respuestas_detectadas = []

    for pagina_num, pagina_img in enumerate(paginas, start=1):
        texto = pytesseract.image_to_string(pagina_img, lang='spa')
        print(f"--- Página {pagina_num} ---")
        print(texto)
        respuestas_detectadas.append(texto)

    return respuestas_detectadas
