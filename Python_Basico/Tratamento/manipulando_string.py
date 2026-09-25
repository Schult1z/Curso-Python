#Manipulando String
fruta = "Melancia" # 0 1 2 3 4 5 6 7 (indice)
print(fruta[0])
print(fruta[0:3])

frase = "Eu amo Python"
frase_tamanho = len(frase)
print(f"A frase {frase} ten {frase_tamanho} caracteres !")

contagem = frase.count("a")
print(contagem)

if "Python" in frase:
    print("Python está na frase !")
else:
    print("Python não está na frase ")