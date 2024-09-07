import pandas as pd

# Criar dados de exemplo para os links
links_data = {
    'links': [
        'https://www.cassol.com.br/produto-exemplo-1',
        'https://www.cassol.com.br/produto-exemplo-2',
        'https://www.cassol.com.br/produto-exemplo-3'
    ]
}

# Criar dados de exemplo para os CEPs
ceps_data = {
    'cep': ['88034001', '88034002', '88034003']
}

# Criar DataFrames
links_df = pd.DataFrame(links_data)
ceps_df = pd.DataFrame(ceps_data)

# Salvar planilha com múltiplas abas
with pd.ExcelWriter('planilha_teste.xlsx') as writer:
    links_df.to_excel(writer, sheet_name='links', index=False)
    ceps_df.to_excel(writer, sheet_name='ceps', index=False)
