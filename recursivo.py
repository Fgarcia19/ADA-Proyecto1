import math

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
    v_A=0
    v_B=0
    t_A=-1
    t_B=-1
    for i in m:
        if(i[0]!=t_A):
            v_A+=peso(A[i[0]])
            t_A=i[0]
        if(i[1]!=t_B):
            v_B+=peso(B[i[1]])
            t_B=i[1]
    return (v_A/v_B)

def recursivo(A,B,i,j,k,l):
    matchs = []
    if i==j:
        for a in range(k,l+1):
            matchs.append((i,a))
        peso=peso_matching(A,B,matchs)
        return matchs, peso
    if k==l:
        for a in range(i,j+1):
            matchs.append((a,k))
        peso=peso_matching(A,B,matchs)
        return matchs, peso

    match_primer_loop=((),math.inf)
    for a in range(l-1,k-1,-1):

        first=(recursivo(A,B,i,i,k,a))
        second=(recursivo(A,B,i+1,j,a+1,l))
        result=(first[0]+second[0],first[1]+second[1])
        if(result[1]<match_primer_loop[1]):
            match_primer_loop=result
    match_segundo_loop=((),math.inf)
    for a in range(j-1,i-1,-1):
        first=recursivo(A,B,i,a,k,k)
        second=recursivo(A,B,a+1,j,k+1,l)
        result=(first[0]+second[0],first[1]+second[1])
        if(result[1]<match_segundo_loop[1]):
            match_segundo_loop=result

    if match_primer_loop[1]>match_segundo_loop[1]:
        return match_segundo_loop

    return match_primer_loop




if __name__ == "__main__":

    # A = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    # B = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    A=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    B=[0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]

    # A=[0,1,0,1,0,1,0,1,0,1]
    # B=[1,1,1,1,1,0,1,0]
    print(bloques(A))
    print(bloques(B))
    m=(recursivo(bloques(A),bloques(B),0,len(bloques(A))-1,0,len(bloques(B))-1))
    print(m)
