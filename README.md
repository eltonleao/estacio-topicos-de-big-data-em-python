# 🚀 UNIVERSIDADE ESTÁCIO DE SÁ - Projeto de Extensão para a Disciplina: Tópicos de Big Data em Python

## 🎯 Visão Geral

Este projeto permite extrair informações de frete para uma lista de SKUs, CEPs e Sellers através da API da **VTEX**, e exporta os resultados para uma planilha do Excel de maneira organizada. A aplicação é ideal para lojas online e integradores que precisam de uma forma automatizada de consultar diferentes transportadoras, prazos de entrega, preços e disponibilidades.

## 🛠️ Funcionalidades

- 📦 **Consulta Automática**: Faz consultas de informações de frete com base em uma lista de SKUs, CEPs e Sellers.
- 📊 **Exportação para Excel**: Os dados são exportados diretamente para uma planilha do Excel, com colunas de CEP, SKU, seller ID, transportadora, tempo de entrega, custo, preço original e preço atual.
- 🚚 **Suporte a Múltiplas Transportadoras**: Inclui tanto retiradas em loja quanto entregas em domicílio.
- ⚠️ **CEP Não Atendido**: Indica quando um SKU não pode ser entregue para um determinado CEP.
- 💲 **Preço Original e Atual**: Extração das informações de preço original (list price) e preço atual (selling price) do produto.

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
   git clone https://github.com/eltonleao/estacio-topicos-de-big-data-em-python.git
   cd estacio-topicos-de-big-data-em-python
   ```

2. **Adicione sua planilha de entrada**:
   
   Insira seu arquivo Excel chamado `input_ceps_skus.xlsx` com três abas:
   - **CEPs**: Coloque os CEPs sem cabeçalhos, linha a linha.
   - **SKUs**: Coloque os SKUs sem cabeçalhos, linha a linha.
   - **SELLERs**: Coloque os IDs de vendedores (Sellers) sem cabeçalhos, linha a linha.

3. **Execute o script**:

   ```bash
   python api.py
   ```

4. **Confira os resultados**:

   Os dados extraídos serão salvos em uma nova planilha chamada `dados_transportadoras_vtex_completos.xlsx`, e as respostas da API serão armazenadas na pasta `./responses/`.

## 💡 Dicas Importantes

- **CEP Não Atendido**: Quando um CEP não é atendido, a planilha indicará essa situação com a mensagem "Não pode ser entregue" na coluna **DISPONIBILIDADE**.
- **Preços**: As colunas **PREÇO ORIGINAL** e **PREÇO ATUAL** exibem os valores em reais. O preço original corresponde ao valor de tabela, enquanto o preço atual reflete possíveis promoções ou descontos.
- **Limite de requisições da API VTEX**: Fique atento ao número de requisições que sua conta da VTEX pode suportar.
- **Manutenção do arquivo Excel**: Garanta que o arquivo `input_ceps_skus.xlsx` contenha apenas CEPs, SKUs e IDs de vendedores válidos.

## 📁 Estrutura de Saída

- O arquivo Excel gerado (`dados_transportadoras_vtex_completos.xlsx`) terá as seguintes colunas:
   - CEP
   - SKU
   - Seller ID
   - Transportadora
   - Tempo de entrega
   - Custo do frete
   - Preço Original
   - Preço Atual
   - Disponibilidade
   - Imposto
   - Opções de Pagamento
   - CEP Atendido

- As respostas da API serão salvas na pasta `./responses/` como arquivos `.json`, identificados por CEP, SKU e Seller ID.