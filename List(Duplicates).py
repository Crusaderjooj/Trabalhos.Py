lista = []

for i in range(8):
    nome = input("Digite um nome: ")
    lista.append(nome)     
lista2 = list(set(lista))

print(f"Lista Original: {lista}")
print(f"Lista sem repetições: {lista2}")
