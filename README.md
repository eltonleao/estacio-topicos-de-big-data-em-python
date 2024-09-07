# 🚀 VTEX Shipping Info Extractor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🎯 Visão Geral

Este projeto permite extrair informações de frete para uma lista de SKUs e CEPs através da API da **VTEX**, e exporta os resultados para uma planilha do Excel de maneira organizada. Uma aplicação ideal para lojas online e integradores que precisam de uma forma automatizada de consultar diferentes transportadoras e prazos de entrega.

## 🛠️ Funcionalidades

- 📦 **Consulta Automática**: Consulta de informações de frete com base em uma lista de SKUs e CEPs.
- 📊 **Exportação para Excel**: Os dados são exportados diretamente para uma planilha do Excel, com colunas de CEP, SKU, transportadora, tempo e custo.
- 🚚 **Suporte a Múltiplas Transportadoras**: Inclui tanto retiradas em loja quanto entregas em domicílio.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Pandas (para leitura de planilhas)
- Openpyxl (para manipulação de arquivos Excel)
- Requests (para fazer requisições à API da VTEX)

Você pode instalar as dependências usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

1. **Clone o repositório**:
   
   ```bash
   git clone https://github.com/seu-usuario/vtex-shipping-extractor.git
   cd vtex-shipping-extractor
   ```

2. **Adicione sua planilha de entrada**:
   
   Insira seu arquivo Excel chamado `input_ceps_skus.xlsx` com duas abas:
   - **CEPs**: Coloque os CEPs sem cabeçalhos, linha a linha.
   - **SKUs**: Coloque os SKUs sem cabeçalhos, linha a linha.

3. **Execute o script**:

   ```bash
   python api.py
   ```

4. **Confira os resultados**:

   Os dados extraídos serão salvos em uma nova planilha chamada `dados_transportadoras_vtex.xlsx`.

**Exemplo do arquivo de entrada:**

- **CEPs Tab**:

   |    |     |
   |----|-----|
   | A1 | 88134360 |
   | A2 | 12345678 |

- **SKUs Tab**:

   |    |     |
   |----|-----|
   | A1 | 2071060 |
   | A2 | 1653182 |

**Resultado final na planilha**:

| CEP       | SKU     | TRANSPORTADORA                         | TEMPO  | CUSTO   |
|-----------|---------|----------------------------------------|--------|---------|
| 88134360  | 2071060 | Retira - SC PALHOCA - Loja Palhoça (30) | 1bd    | Grátis  |
| 88134360  | 1653182 | Entrega SC                             | 4bd    | R$ 29,65|


## 💡 Dicas Importantes

- **Manutenção do arquivo Excel**: Garanta que o arquivo `input_ceps_skus.xlsx` contenha apenas CEPs e SKUs válidos.
- **Limite de requisições da API VTEX**: Fique atento ao número de requisições que sua conta da VTEX pode suportar.
- **Possíveis erros**: Certifique-se de que o formato de CEP e SKU esteja correto e que os valores são convertidos para `string` ao serem enviados.