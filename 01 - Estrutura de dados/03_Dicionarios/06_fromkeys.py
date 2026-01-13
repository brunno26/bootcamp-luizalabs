# {}.fromkeys é um método da classe dict que é utilizado para criar chaves em duas situações:

# 1) Quando quer criar chaves e quer colocar no dicionário mas sem valor (none)
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# 2) Cria um conjunto de chaves com um valor padrão, no exemplo o valor é vazio.
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)