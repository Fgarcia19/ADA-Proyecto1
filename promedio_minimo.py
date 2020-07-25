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




def entrada(a):
    A=[]
    for i in a:
        A.append(int(i))
    return A




def calcular_u(A,B):
    u=0
    for i in A:
        b=0
        for j in B:
            b+=peso(j)
        u+=peso(i)/b
    return u


def dinamico(A,B):
     # a=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
     # b=[0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]

     # a=[0,1,1,0,1,0,1]
     # b=[0,1, 0,1,1]
     u=calcular_u(A,B)

     print(A)
     print(B)
     unionesA={}
     unionesB={}
     matchings={}


     for i in range(0,len(B)):
         s=0
         for j in range(i,len(B)):
             s+=peso(B[j])
             k=i
             while k<=j:
                s2 = 0
                l=k
                while(l<=j):
                    s2+=peso(B[l])
                    l+=1
                unionesB[(k,j)]=s2
                k += 1
         unionesB[(i,len(B)-1)]=s
         matchings[(len(A)-1,i)]=peso(A[len(A)-1])/s

     for i in range(0,len(A)):
         s=0
         for j in range(i,len(A)):
             s+=peso(A[j])
             k=i
             while k<=j:
                s2 = 0
                l=k
                while(l<=j):
                    s2+=peso(A[l])
                    l+=1
                unionesA[(k,j)]=s2
                k += 1
         unionesA[(i,len(A)-1)]=s
         matchings[(i,len(B)-1)]=s/peso(B[len(B)-1])

     for a in range(len(A)-2,-1,-1):
         for b in range(len(B)-2,-1,-1):
             match_primer_loop=math.inf
             for i in range(a,len(A)-1):
                s=unionesA[(a,i)]
                if abs(s/peso(B[b])+matchings[(i+1,b+1)]-u)<match_primer_loop:
                    match_primer_loop=abs(s/peso(B[b])+matchings[(i+1,b+1)]-u)
             match_segundo_loop=math.inf
             for i in range(b, len(B) - 1):
                 s=unionesB[(b,i)]
                 if abs(peso(A[a])/s + matchings[(a + 1, i + 1)]-u)<match_segundo_loop:
                     match_segundo_loop=abs(peso(A[a])/s + matchings[(a + 1, i + 1)]-u)
             if match_primer_loop<match_segundo_loop:
                 matchings[(a,b)]=match_primer_loop
             else:
                 matchings[(a,b)]=match_segundo_loop

     print(matchings[(0,0)])






if __name__ == "__main__":

    ia = input()
    ib = input()
    a = entrada(ia)
    b = entrada(ib)
    A = bloques(a)
    B = bloques(b)
    dinamico(A,B)
    # a=[0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    # b=[0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
    # a = [0, 1, 1, 0, 1, 0, 1]
    # b = [0, 1, 0, 1, 1,0,1]
    # a=input()
    # b=input()
    # A=entrada(a)
    # B=entrada(b)
    # print("Bloques de A")
    # print(bloques(A))
    # print("Bloques de B")
    # print(bloques(B))
    # m=(memoizado(bloques(A),bloques(B),0,len(bloques(A))-1,0,len(bloques(B))-1))
    # print("Matching minimo y su peso")
    # print(m)

    # min = math.inf
    # for c in range(l-1,k-1,-1):
        # if matriz
