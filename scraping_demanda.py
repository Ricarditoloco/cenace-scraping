from playwright.sync_api import sync_playwright
from datetime import datetime
import csv
import os

CSV_FILE = "demanda_log.csv"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Ir a la página
    page.goto("https://www.cenace.gob.mx/graficademanda.aspx")

    # Esperar el elemento
    page.wait_for_selector("#ContentPlaceHolder1_demandaNAC")

    # Leer la demanda
    demanda = page.query_selector("#ContentPlaceHolder1_demandaNAC").inner_text()
    print("Demanda actual:", demanda)

    # Hora exacta de consulta, justo después de obtener la demanda
    hora_consulta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Revisar si existe el archivo CSV, si no, crear con encabezados
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fecha_hora", "demanda"])

    # Añadir nueva fila
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([hora_consulta, demanda])

    browser.close()
