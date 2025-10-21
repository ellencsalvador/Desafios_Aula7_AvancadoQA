# Crie uma tupla com 5 dados
# Uma tupla é criada com parênteses () e seus itens são imutáveis.
minha_tupla = ("banana", "maçã", "laranja", "uva", "morango")
print(f"1. Tupla original: {minha_tupla}")

# Altere a tupla para uma lista
# Usamos a função list() para converter a tupla em uma lista.
# Listas são mutáveis, ou seja, podemos alterar seus elementos.
minha_lista = list(minha_tupla)
print(f"2. Tupla convertida para lista: {minha_lista}")

# Insira 2 dados extras a essa lista
# O método .append() adiciona um item ao final da lista.
minha_lista.append("abacaxi")
minha_lista.append("melancia")
print(f"3. Lista com 2 novos dados: {minha_lista}")

# Remova o primeiro dado da lista
# O método .pop(0) remove o item que está no índice 0 (o primeiro).
minha_lista.pop(0)
print(f"4. Lista após remover o primeiro dado: {minha_lista}")

# Remova o último dado da lista
# O método .pop() sem argumento remove o último item da lista.
minha_lista.pop()
print(f"5. Lista após remover o último dado: {minha_lista}")

# Faça um print com o primeiro dado da lista
# Acessamos o primeiro item usando o índice 0.
primeiro_dado = minha_lista[0]
print(f"6. O primeiro dado da lista atual é: {primeiro_dado}")

# Faça um print com a quantidade de dados da lista
# A função len() retorna o número de itens em uma lista.
quantidade_dados = len(minha_lista)
print(f"7. A quantidade de dados na lista é: {quantidade_dados}")

# Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
# Um dicionário armazena dados em pares de chave:valor, dentro de chaves {}.
dados_pessoais = {
    "Nome": "Ana Silva",
    "Idade": 32,
    "Profissão": "Desenvolvedora"
}
print(f"8. Dicionário criado: {dados_pessoais}")

# Imprima somente o valor contido na chave "Nome" do dicionário
# Acessamos o valor de uma chave usando a sintaxe dicionario['chave'].
nome_no_dicionario = dados_pessoais["Nome"]
print(f"9. O valor da chave 'Nome' é: {nome_no_dicionario}")