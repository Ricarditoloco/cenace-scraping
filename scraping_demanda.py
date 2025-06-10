from playwright.sync_api import sync_playwright
from datetime import datetime

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

    # Guardar en archivo (para histórico)
    with open("demanda_log.csv", "a") as f:
        f.write(f"{datetime.now()},{demanda}\n")

    browser.close()
