# 🎮 Steam Games EDA (Exploratory Data Analysis) 📊

> Projeto de EDA em Python (Pandas e Matplotlib) focado no dataset Steam Games 2025. Aborda limpeza de dados, correlações estatísticas, identificação de multimodalidade e remoção de outliers via cálculo de IQR.

## 📌 Sobre o Projeto
Este projeto consiste em uma análise detalhada de mais de 263 mil aplicações disponíveis na plataforma Steam até janeiro de 2025. O objetivo foi aplicar técnicas de estatística descritiva e visualização para entender padrões de preços e descontos.

Projeto desenvolvido como parte do módulo de Data Science e Estatística do curso de Engenharia de Software da **FIAP**.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas
* **Visualização de Dados:** Matplotlib

## ⚠️ Observação sobre o Dataset (applications.csv)
Devido ao limite de tamanho de arquivos do GitHub (100MB), o arquivo de dados bruto não está incluso neste repositório.

* **Fonte dos Dados:** [Steam Games Dataset 2025 (Kaggle)](https://www.kaggle.com/datasets/abhishekgupta56447/steam-games-dataset-2025/data)
* **Arquivo necessário:** `applications.csv`

Para executar os scripts, baixe o arquivo no link acima e coloque-o na pasta raiz do projeto.

## 🚀 O que foi feito:
1. **Limpeza e Estruturação:** Tratamento de valores nulos e tipos de dados com Pandas.
2. **Estatística Descritiva:** Cálculo de Tendência Central (Média, Mediana) e Dispersão (Desvio Padrão).
3. **Histogramas:** Identificação de **assimetria à direita** e **multimodalidade** (picos em descontos de 50% e 75%).
4. **Scatterplots:** Investigação de correlação entre Preço x Recomendações e Preço x Desconto.
5. **Tratamento de Outliers (IQR):** Uso dos **Limites de Tukey** para remover anomalias e gerar Boxplots comparativos.

## 💡 Principais Insights
* **Robustez:** A mediana mostrou-se a medida mais confiável para representar o preço típico, dado que a média é inflada por outliers extremos.
* **Preços Psicológicos:** A distribuição de preços não é contínua, apresentando picos em valores tabelados da indústria e terminações psicológicas.
* **Popularidade:** Não foi encontrada correlação forte entre o preço de lançamento e o volume de recomendações.
