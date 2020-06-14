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

def peso(A,B,m):
    v_A=0
    v_B=0
    t_A=-1
    t_B=-1
    for i in m:
        if(i[0]!=t_A):
            v_A+=valor(A[i[0]])
            t_A=i[0]
        if(i[1]!=t_B):
            v_B+=valor(B[i[1]])
            t_B=i[1]
    return (v_A/v_B)


def valor(a):
    return a[1]-a[0]+1


def iterar(A,B):
    peso_m=0
    matchings=[]
    match=[]
    j=0
    i=0
    sum1=valor(A[0])
    sum2=valor(B[0])
    while(i<len(A)):
        match.append((i, j))
        print("A ",i,end=' ')
        print("B ",j)
        if j==len(B)-1:
            i+=1
        elif i==len(A)-1:
            j+=1
        elif sum1 == sum2:
            print("A ", i, end=' ')
            print("B ", j)
            i += 1
            j += 1
            match.append((i, j))
            peso_m += peso(A, B, match)
            matchings.append(match)
            match=[]
        elif sum1 > sum2:
            j+=1
            if j<len(B)-1:
                sum2 += valor(B[j])
                if sum1<=sum2 :
                    print("A ", i, end=' ')
                    print("B ", j)
                    match.append((i, j))
                    peso_m += peso(A, B, match)
                    matchings.append(match)
                    match=[]
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
        elif sum1 < sum2:
            i+=1
            if i<len(A)-1:
                sum1 += valor(A[i])
                if sum1 >= sum2:
                    print("A ", i, end=' ')
                    print("B ", j)
                    match.append((i, j))
                    peso_m += peso(A, B, match)
                    matchings.append(match)
                    match = []
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
    peso_m+=peso(A,B,match)
    matchings.append(match)
    print(matchings)
    print(peso_m)



def voraz():

    A=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    # A=[0,1,0,1,0,1,0,1,0,1]
    # B=[1,1,1,1,1,0,1,0]
    # A=[0,1,0,1,1,0,0,1,1,1,1,1,1,0,1]
    # B=[0,1,1,1,0,1,0,1,0]
    B=[0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    # A=[0, 1 , 0 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1]
    # B=[0, 0,  1 , 1 , 0 , 1 , 1, 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0]
    bloquesA=bloques(A)
    bloquesB=bloques(B)
    print(bloquesA)
    print(bloquesB)
    if len(bloquesA)> len(bloques(B)):
        iterar(bloquesA,bloquesB)
    else:
        iterar(bloquesB,bloquesA)




   # print(sum([1,2,3]))


if __name__ == "__main__":
    voraz()
