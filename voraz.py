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

    if(def_inicio):
        A_bloques.append((inicio,len(A)-1))
    return A_bloques



def peso(A):
    return A[1]-A[0]+1

def peso_matching(A,B,m):
    peso_final = 0
    i=0
    while i<len(m):
        suma = peso(A[m[i][0]])
        sumb = peso(B[m[i][1]])
        aux = False
        if i != len(m)-1:
            while (m[i][0] == m[i+1][0]):
                sumb += peso(B[m[i + 1][1]])
                i+=1
                aux = True
                if i==len(m)-1:
                    break
            if (aux==False):
                while (m[i][1] == m[i+1][1]):
                    suma += peso(A[m[i+1][0]])
                    i+=1
                    if i == len(m) - 1:
                        break
        peso_final += suma / sumb
        i+=1

    print(peso_final)

def valor(a):
    return a[1]-a[0]+1


def iterar(A,B):
    matchings=[]
    j=0
    i=0
    sum1=valor(A[0])
    sum2=valor(B[0])
    while(i<len(A)):
        print("A ",i,end=' ')
        print("B ",j)
        matchings.append((i,j))
        if j==len(B)-1:
            i+=1
        elif i==len(A)-1:
            j+=1
        elif sum1 > sum2:
            j+=1
            if j<len(B)-1:
                sum2 += valor(B[j])
                if sum1<sum2 :
                    print("A ", i, end=' ')
                    print("B ", j)
                    matchings.append((i, j))
                    i+=1
                    if i==len(A):
                        break;
                    j+=1
                    if j==len(B):
                        break;
                    sum1 = valor(A[i])
                    sum2 = valor(B[j])

            else:
                i+=1
        elif sum1 <= sum2:
            i+=1
            if i<len(A)-1:
                sum1 += valor(A[i])
                if sum1 > sum2:
                    print("A ", i, end=' ')
                    print("B ", j)
                    matchings.append((i, j))
                    i += 1
                    if i==len(A):
                        break;
                    j += 1
                    if j==len(B):
                        break;
                    sum1 = valor(A[i])
                    sum2 = valor(B[j])

            else:
                j+=1
    print(matchings)
    peso_matching(A,B,matchings)



def voraz():

    A=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    B=[0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]


    # A=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    # A=[0,1,0,1,0,1,0,1,0,1]
    # B=[1,1,1,1,1,0,1,0]
    # A=[0,1,0,1,1,0,0,1,1,1,1,1,1,0,1]
    # B=[0,1,1,1,0,1,0,1,0]
    # B=[0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    # A=[0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1]
    # B=[0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0]
    # A=[1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0]
    # B=[1,1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,0,0]
    bloquesA=bloques(A)
    bloquesB=bloques(B)
    print(bloquesA)
    print(bloquesB)
    if len(bloquesA)>= len(bloques(B)):
        iterar(bloquesA,bloquesB)
    else:
        iterar(bloquesB,bloquesA)
if __name__ == "__main__":
    voraz()
