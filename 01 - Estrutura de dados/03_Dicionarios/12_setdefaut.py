# {}.setdefault é um método da classe dict que é utilizado em duas situações:

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# 1 - Se o atributo existir no dicionário, ele retorna o valor que existe no dicionário e não altera ele
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# 2 - Se o atributo não estiver no dicionário, ele adiciona o valor que for inserido no exemplo: Giovanna
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}