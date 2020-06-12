matchings=[]

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

def valor(a):
    return a[1]-a[0]+1


def iterar(A,B):
    j=0
    i=0
    sum1=valor(A[0])
    sum2=valor(B[0])
    match=[]
    while(i<len(A)):
        match.append((i,j))
        if j==len(B)-1:
            i+=1
        elif sum1 > sum2:
            j+=1
            sum2 += valor(B[j])
            if sum1<=sum2:
                match.append((i, j))
                matchings.append(match)
                match=[]
                i+=1
                j+=1
                sum1 = valor(A[i])
                sum2 = valor(B[j])
        else:
            i+=1
            sum1 += valor(A[i])
            if sum1 >= sum2:
                match.append((i, j))
                i += 1
                j += 1
                matchings.append(match)
                match=[]
                sum1 = valor(A[i])
                sum2 = valor(B[j])
    matchings.append(match)
    print(matchings)
    print("Los conjuntos de matching son")
    for i in range(0,len(matchings)):
        print("Match ",i,end=' ')
        print(matchings[i])



def voraz():
    A=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    B=[0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]

    bloquesA=bloques(A)
    bloquesB=bloques(B)

    if len(bloquesA)> len(bloques(B)):
        iterar(bloquesA,bloquesB)
    else:
        iterar(bloquesB,bloquesA)


if __name__ == "__main__":
    voraz()
