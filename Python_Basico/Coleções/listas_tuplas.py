frutas = ['maca', 'banana', 'laranja']
print(frutas[1])

frutas.append("melancia")
frutas.remove("laranja")

print(frutas)

frutas[0] = "uva"
frutas.insert(1, 'laranja')

print(frutas)

frutas.sort()

print(frutas)

frutas2 = frutas.copy()
frutas2.append("Mamamo")

print(frutas)
print(frutas2)

### tupla
cores = ('vermelho', 'azul', 'verde') #const ()
cores[1] = 'amarelo' 