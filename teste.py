Valores = [10,10,10,5,5,5,3]

ListaSigma = list()
for c in Valores:
    print(c)
    print(c-7.5)
    print((3-6.85)*(3-6.85))
    ListaSigma.append((c - 6.85) * (c - 6.85))
print(ListaSigma)
