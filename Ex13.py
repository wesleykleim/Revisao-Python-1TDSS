corredor = [False] * 1001

pes = 1


while pes <= 1000:
    porta = 1

    while porta <= 1000:
        if porta % pes == 0:
            if corredor[porta] == True:
                corredor[porta] = False
            else:
                corredor[porta] = True
        porta = porta + 1
    pes = pes + 1

for i in range(1, 1000):
    if corredor[i]:
        print("Porta ", i, " aberta")
