# {}.popitem é um método da classe dict que é utilizado para remover um valor do dicionário na sequência, não é necessário informar qual valor deseja remover.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

