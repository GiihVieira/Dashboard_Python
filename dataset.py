'''
Código que efetua a conexão com o arquivo fonte dos dados a serem análisados
e os transforma em um dataFrame pra manipulação
'''
import json
import pandas as pd

file = open('dados/vendas.json') # Abrindo o arquivo 
data = json.load(file) # Carregando os dados do arquivo

df = pd.DataFrame.from_dict(data) # Criando um dataFrame para manipulação dos dados

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close() # Fechando a conexão com o arquivo
