from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import pandas as pd
import openpyxl
from time import sleep
from tqdm import tqdm

# Forçar a leitura dos CEPs como strings
links = pd.read_excel(r"C:\Users\victor.hanioka\Desktop\Novo(a) Planilha do Microsoft Excel.xlsx")
ceps = pd.read_excel(r"C:\Users\victor.hanioka\Desktop\Novo(a) Planilha do Microsoft Excel.xlsx", sheet_name="ceps", dtype={'cep': str})

excel_book = openpyxl.Workbook()
sheet = excel_book.active
sheet.title = "Dados Extração Cassol"

sheet["A1"] = "CEP"
sheet["B1"] = "LINK"
sheet["C1"] = "TRANSPORTADORA"
sheet["D1"] = "TEMPO"
sheet["E1"] = "CUSTO"

current_row = 2

driver = webdriver.Chrome()
driver.get(r'https://www.cassol.com.br/')

for i, row in tqdm(ceps.iterrows(), total=len(ceps), desc="Processando Cep"):

    num_cep = row['cep']
    print(num_cep)
    if driver:
        driver.quit()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(r'https://www.cassol.com.br/')

    input_cep = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="modalInputCep"]'))
    )
    input_cep.send_keys(num_cep)

    botao_cep = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(normalize-space(.),"Inserir CEP")]'))
    )
    sleep(2)
    botao_cep.click()

    for j, row_link in tqdm(links.iterrows(), total=len(links), desc="Processando Links"):
        link = row_link['links']
        entrega_exp = 'expressa sc'
        driver.get(link)
        tempo_ent = ''
        preco = ''

        try:
            linha_transp = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//tr[contains(.,"Transportadora")]'))
            
            )

            linha_transp_html = linha_transp.get_attribute("outerHTML")
            linha_tratada = BeautifulSoup(linha_transp_html, "html.parser")
            tds_linha = linha_tratada.find_all("td")
            tempo = tds_linha[1].text
            preco = tds_linha[2].text

            print(preco)
            print(tempo)
            transportadora = "Transportadora"
            
            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)

            current_row += 1
        except:
            tempo = 'não encontrado'
            preco = 'não encontrado'
            transportadora = "Transportadora"

            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)
            current_row += 1
            pass

        try:
            linha_transp = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//tr[contains(.,"Entrega SC")]'))
            
            )
            transportadora = "Entrega SC"

            linha_transp_html = linha_transp.get_attribute("outerHTML")
            linha_tratada = BeautifulSoup(linha_transp_html, "html.parser")
            tds_linha = linha_tratada.find_all("td")
            tempo = tds_linha[1].text
            preco = tds_linha[2].text

            print(preco)
            print(tempo)
            
            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)

            current_row += 1
        except:
            tempo = 'não encontrado'
            preco = 'não encontrado'
            transportadora = "Entrega SC"

            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)
            current_row += 1
            pass
        try:
            linha_transp = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//tr[contains(.,"Entrega RS")]'))
            
            )
            transportadora = "Entrega Expressa RS"

            linha_transp_html = linha_transp.get_attribute("outerHTML")
            linha_tratada = BeautifulSoup(linha_transp_html, "html.parser")
            tds_linha = linha_tratada.find_all("td")
            tempo = tds_linha[1].text
            preco = tds_linha[2].text

            print(preco)
            print(tempo)
            
            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)

            current_row += 1
        except:
            tempo = 'não encontrado'
            preco = 'não encontrado'
            transportadora = "Entrega Expressa RS"

            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)
            current_row += 1
            pass
        try:
            linha_transp = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//tr[contains(.,"Entrega PR")]'))
            
            )
            transportadora = "Entrega Expressa PR"

            linha_transp_html = linha_transp.get_attribute("outerHTML")
            linha_tratada = BeautifulSoup(linha_transp_html, "html.parser")
            tds_linha = linha_tratada.find_all("td")
            tempo = tds_linha[1].text
            preco = tds_linha[2].text

            print(preco)
            print(tempo)
            
            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)

            current_row += 1
        except:
            tempo = 'não encontrado'
            preco = 'não encontrado'
            transportadora = "Entrega Expressa PR"

            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=link)
            sheet.cell(row=current_row, column=3, value=transportadora)
            sheet.cell(row=current_row, column=4, value=tempo)
            sheet.cell(row=current_row, column=5, value=preco)
            current_row += 1
            pass


excel_book.save("teste_2.xlsx")
