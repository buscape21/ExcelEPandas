import pandas as pd

# Carregando o arquivo Excel em um DataFrame
arquivo = 'produtos.xlsx'
df = pd.read_excel(arquivo)

# Imprimindo o banco de dados atual
print('-LOJA DE ELETRONICOS-')
print(df)

# Apresentando opções para o usuário
print('\n')
print('1 - Adicionar produto')
print('2 - Adicionar condição de produto')
print('3 - Sair')
print('\n')

# Solicitando a decisão do usuário
decisao = int(input('O QUE DESEJA FAZER? '))

# Opção 1: Adicionar produto
if decisao == 1:
    # Solicitando informações sobre o novo produto
    novoProduto = input('Qual produto você quer adicionar? ') 
    novaQuantidade = int(input('Qual a quantidade? '))
    novoPreco = float(input('Qual o preço? '))
    novaCondicao = input('Qual a condição? ')
    
    # Criando um novo registro (linha) como um dicionário
    novo_registro = {'PRODUTO': novoProduto, 'QUANTIDADE': novaQuantidade, 'PREÇO': novoPreco, 'CONDIÇÃO': novaCondicao}
    
    # Adicionando o novo registro ao DataFrame
    df = df._append(novo_registro, ignore_index=True) 

# Opção 2: Adicionar condição de produto
elif decisao == 2:
    # Iterando através das linhas e adicionando estados dos produtos
    for i in range(len(df)):  
        novoValor = input(f'Qual o estado do produto {i}? ')
        df.at[i, 'CONDIÇÃO'] = novoValor

# Opção 3: Sair
else:
    print('Saindo....')

# Salvando o DataFrame atualizado de volta no arquivo Excel
df.to_excel(arquivo, index=False)
print(f'DataFrame com nova coluna salvo em "{arquivo}"')
