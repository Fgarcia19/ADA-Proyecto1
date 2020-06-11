def bloques(A):
    A_bloques = []
    inicio = -1
    def_inicio=False
    for i in range(0, len(A)):
        if A[i] == 1 and def_inicio==False:
            inicio = i
            def_inicio=True
        if A[i] == 0 and inicio != -1:
            fin = i - 1
            A_bloques.append((inicio, fin))
            inicio = -1
            def_inicio=False
    return A_bloques

def peso(A,B):
    if len(A)==1:
        return A/sum(B)
    else:
        return sum(A)/B

def iterar(A,B):
    for i in A:


def voraz():
    A=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    B=[0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]

    bloquesA=bloques(A)
    bloquesB=bloques(B)

    if len(bloquesA)> len(bloques(B)):
        iterar(bloquesA,bloquesB)
    else:
        iterar(bloquesB,bloquesA)



    print(bloquesA)
    print(bloquesB)
   # print(sum([1,2,3]))


if __name__ == "__main__":
    voraz()
