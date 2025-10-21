minha_tupla = ("banana", "maçã", "laranja", "uva", "morango")
print(f"1. Tupla original: {minha_tupla}")

minha_lista = list(minha_tupla)
print(f"2. Tupla convertida para lista: {minha_lista}")

minha_lista.append("abacaxi")
minha_lista.append("melancia")
print(f"3. Lista com 2 novos dados: {minha_lista}")

minha_lista.pop(0)
print(f"4. Lista após remover o primeiro dado: {minha_lista}")

minha_lista.pop()
print(f"5. Lista após remover o último dado: {minha_lista}")

primeiro_dado = minha_lista[0]
print(f"6. O primeiro dado da lista atual é: {primeiro_dado}")

quantidade_dados = len(minha_lista)
print(f"7. A quantidade de dados na lista é: {quantidade_dados}")

dados_pessoais = {
    "Nome": "Ana Silva",
    "Idade": 32,
    "Profissão": "Desenvolvedora"
}
print(f"8. Dicionário criado: {dados_pessoais}")

nome_no_dicionario = dados_pessoais["Nome"]
print(f"9. O valor da chave 'Nome' é: {nome_no_dicionario}")