# # {}.keys é um método da classe dict que é utilizado para retornar somente as chaves do nosso dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

# retorna todas as chaves 
novo_dicionario = {"a": 100, 1: "teste", "b": "Python"}
print(novo_dicionario.keys())