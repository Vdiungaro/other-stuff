from playwright.sync_api import sync_playwright
import time
from datetime import datetime

with sync_playwright() as p:
    start = time.time()

    browser = p.chromium.launch()
    
    page = browser.new_page()

    page.goto("https://rodoviariaonline.com.br/passagem-onibus/rio-claro-sp/brotas-sp/?i=2021-08-01") #?i= mudar o dia ali para acessar outros dias

    time.sleep(1.5)

    page.click('//*[@id="from-info"]/section/label[2]/div[2]/div')

    time.sleep(1.5)

    Plivre = page.inner_text('id=livreIda')

    browser.close()


end = time.time()

now = datetime.now()
time_formated = now.strftime("%H:%M:%S")

Plivre = str(Plivre)
time_formated = str(time_formated)
temp = 'Numero de passagens disponiveis: ' + Plivre + ' no horário: ' + time_formated

with open('Passagens Disponiveis.txt', 'a') as f:
    f.write(temp + "\n")
f.close()