from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from time import sleep
from tqdm import tqdm

# Mock de CEPs (simulando uma leitura da planilha)
ceps = pd.DataFrame({
    'cep': ['88134360']  # Exemplo de CEPs
})

# Mock de links (simulando uma leitura da planilha)
links = pd.DataFrame({
    'links': [
        'https://www.cassol.com.br/ar-condicionado-split-inverter-12000btus-pac12000iqfm1-branco-quente-e-frio-philco/p',  # Exemplo de links
    ]
})

# Criação da planilha de saída
excel_book = openpyxl.Workbook()
sheet = excel_book.active
sheet.title = "Dados Extração Cassol"

# Definindo cabeçalhos na planilha
sheet["A1"] = "CEP"
sheet["B1"] = "LINK"
sheet["C1"] = "TRANSPORTADORA"
sheet["D1"] = "TEMPO"
sheet["E1"] = "CUSTO"

current_row = 2

# Iniciando o driver do Selenium (verifique se o caminho do driver está configurado corretamente)
driver = webdriver.Chrome()

# Laço para iterar sobre os CEPs e links
for i, row in tqdm(ceps.iterrows(), total=len(ceps), desc="Processando Cep"):
    num_cep = row['cep']
    print(f"Processando CEP: {num_cep}")
    
    # Laço para iterar sobre os links
    for j, row_link in tqdm(links.iterrows(), total=len(links), desc="Processando Links"):
        link = row_link['links']
        driver.get(link)  # Abrir a página do produto
        
        try:
            # Espera até que o campo de CEP esteja disponível na página do produto
            input_cep = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="modalInputCep"]'))
            )
            input_cep.clear()
            input_cep.send_keys(num_cep)  # Insere o CEP

            # Clica no botão para inserir o CEP
            botao_cep = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(normalize-space(.),"Inserir CEP")]'))
            )
            sleep(2)  # Espera para evitar problemas de tempo de carregamento
            botao_cep.click()

            # Agora que o CEP foi inserido, vamos procurar as informações de transporte
            try:
                linha_transp = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//tr[contains(.,"Transportadora")]'))
                )
                linha_transp_html = linha_transp.get_attribute("outerHTML")
                linha_tratada = BeautifulSoup(linha_transp_html, "html.parser")
                tds_linha = linha_tratada.find_all("td")
                tempo = tds_linha[1].text
                preco = tds_linha[2].text

                print(f"Preço: {preco} | Tempo: {tempo}")
                transportadora = "Transportadora"
                
                sheet.cell(row=current_row, column=1, value=num_cep)
                sheet.cell(row=current_row, column=2, value=link)
                sheet.cell(row=current_row, column=3, value=transportadora)
                sheet.cell(row=current_row, column=4, value=tempo)
                sheet.cell(row=current_row, column=5, value=preco)

                current_row += 1
            except:
                print("Informações de transportadora não encontradas.")
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

        except NoSuchElementException:
            print(f"Campo de CEP não encontrado na página do produto {link}")

# Salva o resultado final na planilha
excel_book.save("teste_2.xlsx")

# Fecha o driver no final
driver.quit()
