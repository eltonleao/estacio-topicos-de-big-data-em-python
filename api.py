import requests
import pandas as pd
import openpyxl

# Carregar a planilha com os CEPs e SKUs sem cabeçalhos
input_file = "input_ceps_skus.xlsx"
ceps = pd.read_excel(input_file, sheet_name="CEPs", header=None)  # Sem cabeçalho, então header=None
skus = pd.read_excel(input_file, sheet_name="SKUs", header=None)  # Sem cabeçalho, então header=None

# Renomear as colunas manualmente
ceps.columns = ['CEP']
skus.columns = ['SKU']

# Criação da planilha de saída
excel_book = openpyxl.Workbook()
sheet = excel_book.active
sheet.title = "Dados Extração VTEX"

# Definindo cabeçalhos na planilha de saída
sheet["A1"] = "CEP"
sheet["B1"] = "SKU"
sheet["C1"] = "TRANSPORTADORA"
sheet["D1"] = "TEMPO"
sheet["E1"] = "CUSTO"

current_row = 2

# URL da API VTEX
vtex_api_url = "https://cassol.vtexcommercestable.com.br/api/checkout/pub/orderForms/simulation"

# Cabeçalhos para a requisição
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

def fetch_shipping_info(sku, cep):
    payload = {
        "items": [
            {
                "id": str(sku),  # Converter SKU para string
                "quantity": 1,
                "seller": "1"
            }
        ],
        "country": "BRA",
        "postalCode": str(cep)  # Converter CEP para string
    }

    # Faz a requisição POST à API da VTEX
    response = requests.post(vtex_api_url, json=payload, headers=headers)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        print(f"Resposta da API para CEP {cep} e SKU {sku}: {data}")  # Log da resposta

        resultados = []
        
        # Extrai as informações de logística (transportadora, tempo e preço)
        logistics_info = data.get('logisticsInfo', [])
        if logistics_info:
            for sla in logistics_info[0].get('slas', []):
                delivery_channel = sla.get('deliveryChannel', '')
                if delivery_channel == 'pickup-in-point':
                    transportadora = sla.get('name', 'Retirada em loja')
                    preco = 0  # Define o preço como 0 para retirada
                elif delivery_channel == 'delivery':
                    transportadora = sla.get('name', 'Entrega')  # Captura o nome correto para entregas
                    preco = sla.get('price', 0) / 100  # Convertendo centavos para reais
                else:
                    transportadora = 'Não informado'
                    preco = 0

                preco_formatado = 'Grátis' if preco == 0 else f"R$ {preco:.2f}"

                # Adiciona cada resultado como uma tupla na lista
                resultados.append((transportadora, sla.get('shippingEstimate', 'Não informado'), preco_formatado))
        
        return resultados
    
    return [('Não informado', 'Não informado', 'Não informado')]

# Laço para iterar sobre os CEPs e SKUs
for i, row_cep in ceps.iterrows():
    num_cep = row_cep['CEP']  # Certifique-se de que o nome da coluna é "CEP"
    for j, row_sku in skus.iterrows():
        sku = row_sku['SKU']  # Certifique-se de que o nome da coluna é "SKU"
        
        # Busca as informações de envio
        resultados = fetch_shipping_info(sku, num_cep)

        # Insere as informações na planilha
        for resultado in resultados:
            transportadora, tempo, preco = resultado
            sheet.cell(row=current_row, column=1, value=num_cep)
            sheet.cell(row=current_row, column=2, value=sku)
            sheet.cell(row=current_row, column=3, value=transportadora or 'Não encontrado')
            sheet.cell(row=current_row, column=4, value=tempo or 'Não encontrado')
            sheet.cell(row=current_row, column=5, value=preco or 'Não encontrado')
        
            current_row += 1

# Salva o resultado final na planilha
excel_book.save("dados_transportadoras_vtex.xlsx")

print("Processo concluído!")
