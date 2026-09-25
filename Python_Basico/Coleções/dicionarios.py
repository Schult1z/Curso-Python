### Dicionarios
pessoa = {
    "nome": "Gabriel",
    "idade": 25,
    "cidade": "Curitiba",
    "profissao": ["programador", "estagiario"],
    #"telefone": None
}

print(pessoa["idade"])

pessoa["idade"] = 21

print(pessoa["profissao"][1])

print(pessoa)
print(pessoa.keys())

print(pessoa.get("telefone", "Não existe"))