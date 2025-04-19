frase1 = input("Digite uma frase: ")
frase2 = input("Digite outra frase: ")
fraseNova = frase1.split(' ')
frasenova2 = frase2.split(' ')
final = []
for palavra in fraseNova:
    if palavra in frasenova2:
        final.append(palavra)
print(f"As palavras repetidas são: {final}")
print(f"AS frases escolhidas foram: {frase1} e {frase2}")
