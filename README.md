# 🚀 UNIVERSIDADE ESTÁCIO DE SÁ - Projeto de Extensão para a Disciplina: Tópicos de Big Data em Python

## 🎯 Visão Geral

Este projeto faz parte de uma atividade de extensão acadêmica para a **Universidade Estácio de Sá**, com o objetivo de automatizar a verificação de informações de frete utilizando a API da **VTEX**. O projeto visa resolver problemas de discrepância nas tabelas de frete cadastradas, garantindo que os valores exibidos aos clientes correspondam corretamente aos valores de frete reais.

Através desta solução, a empresa **Cassol Centerlar** pode identificar rapidamente erros em seus valores de frete, otimizando o processo de verificação e correção de SKUs com informações incorretas, aumentando assim a satisfação dos clientes e melhorando a taxa de conversão de vendas.

## 🛠️ Funcionalidades

- 📦 **Consulta Automática**: Consulta de informações de frete com base em uma lista de SKUs e CEPs.
- 📊 **Exportação para Excel**: Os dados são exportados diretamente para uma planilha do Excel, com colunas de CEP, SKU, transportadora, tempo, custo, preço original e preço atual.
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
   
   Insira seu arquivo Excel chamado `input_ceps_skus.xlsx` com duas abas:
   - **CEPs**: Coloque os CEPs sem cabeçalhos, linha a linha.
   - **SKUs**: Coloque os SKUs sem cabeçalhos, linha a linha.

3. **Execute o script**:

   ```bash
   python app.py
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

| CEP       | SKU     | TRANSPORTADORA                         | TEMPO  | CUSTO   | PREÇO ORIGINAL | PREÇO ATUAL | DISPONIBILIDADE           |
|-----------|---------|----------------------------------------|--------|---------|----------------|-------------|---------------------------|
| 88134360  | 2071060 | Retira - SC PALHOCA - Loja Palhoça (30) | 1bd    | Grátis  | R$ 3.039,00    | R$ 2.839,00 | Disponível                 |
| 22450200  | 2071060 | -                                      | -      | -       | R$ 3.039,00    | R$ 2.839,00 | Não pode ser entregue       |

## 💡 Dicas Importantes

- **CEP Não Atendido**: Quando um CEP não é atendido, a planilha indicará essa situação com a mensagem "Não pode ser entregue" na coluna **DISPONIBILIDADE**.
- **Preços**: As colunas **PREÇO ORIGINAL** e **PREÇO ATUAL** exibem os valores em reais. O preço original corresponde ao valor de tabela, enquanto o preço atual reflete possíveis promoções ou descontos.
- **Limite de requisições da API VTEX**: Fique atento ao número de requisições que sua conta da VTEX pode suportar.
- **Manutenção do arquivo Excel**: Garanta que o arquivo `input_ceps_skus.xlsx` contenha apenas CEPs e SKUs válidos.

---

**Este projeto é parte da atividade de extensão da Universidade Estácio de Sá, dentro da disciplina de Tópicos em Big Data e Python. O objetivo é aplicar conhecimentos adquiridos na disciplina para resolver problemas reais da empresa Cassol, aumentando a eficiência operacional e melhorando a experiência dos consumidores.**