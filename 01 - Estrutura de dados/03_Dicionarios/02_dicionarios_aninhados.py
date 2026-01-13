# Dicionários podem armazenar qualquer tipo de objeto em Python como valor, desde que a chave para esse valor seja um objeto imutável como String e Números.
# Estruturas aninhadas é quando tenho uma estrutura dentro da outra.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    
    # Foi adicionado um dicionário dentro do outro
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}


telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121" (Acessando o telefone através da chave e-mail)
print(telefone)

# Acessando valor da nova chave "extra" (chamando o valor) e atribuindo a chave na qual encontra-se o valor (nesse caso o e-mail): melaine@gmail.com
extra = contatos["melaine@gmail.com"]["extra"]["a"]  # acessando os valores "extra" e "a" por meio da chave e-mail
print(extra)
