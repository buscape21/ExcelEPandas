# ExcelEPandas

Este programa permite ao usuário gerenciar um banco de dados simples de produtos eletrônicos, adicionando novos produtos ou atualizando as condições dos produtos existentes. É uma aplicação útil para demonstrar como usar a biblioteca Pandas para manipular dados tabulares em Python. Certifique-se de ter a biblioteca Pandas instalada para executar este programa.

O programa permite ao usuário realizar as seguintes ações:

Carregar um banco de dados existente a partir do arquivo Excel produtos.xlsx em um DataFrame do Pandas.
Apresentar um menu de opções para o usuário, onde ele pode escolher entre:
Adicionar um novo produto (inserindo nome, quantidade, preço e condição).
Adicionar condição de um produto existente (atualizar a coluna "CONDIÇÃO").
Sair do programa.
O programa segue este fluxo:

Ao iniciar, ele carrega o banco de dados existente e o exibe na tela.
O usuário escolhe uma das opções do menu (1, 2 ou 3) digitando o número correspondente.
Se o usuário escolher adicionar um novo produto (opção 1), ele será solicitado a inserir informações sobre o novo produto, como nome, quantidade, preço e condição. O novo registro é criado como um dicionário Python e adicionado ao DataFrame.
Se o usuário escolher adicionar uma condição de produto existente (opção 2), ele iterará pelas linhas existentes e perguntará a condição para cada produto. A condição é atualizada na coluna "CONDIÇÃO" do DataFrame.
Se o usuário escolher sair (opção 3), o programa será encerrado.
Após qualquer uma dessas ações, o DataFrame atualizado é salvo de volta no arquivo Excel produtos.xlsx.
