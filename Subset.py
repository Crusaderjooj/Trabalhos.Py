A = set({})
B = set({})
for i in range(5):
    x = int (input("Digite um numero para o conjunto 1: "))
    A.add(x)
    y = int (input("Digite um numero para o conjunto 2: "))
    B.add(y) 
subconjunto = A.issubset(B)
if subconjunto == True:
    print("O conjunto A é subconjunto do conjunto B")
else:
    print("O conjunto A não é subconjunto do conjunto B")
