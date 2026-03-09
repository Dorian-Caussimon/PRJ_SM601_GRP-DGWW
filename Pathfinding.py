class Graph:
    def __init__(self):
        self.nb_sommet = 0
        self.nb_arc = 0
        self.liste_arc = []

def lecture(nb):
    newGraph=Graph()
    with open("résultats"+str(nb)+".txt","w+") as g:
        with open("graphes/"+str(nb),"r") as f:
            a=0

            for line in f.readlines():
                g.write(line)
                if a == 0:
                    newGraph.nb_sommet=line[:len(line)-1]
                if a == 1:
                    newGraph.nb_arc=line[:len(line)-1]
                if line[len(line)-1:len(line)] != "\n":
                    newGraph.liste_arc.append(line)
                elif a >= 2:
                    newGraph.liste_arc.append(line[:len(line)-1])
                a+=1
    print(newGraph.nb_sommet,newGraph.nb_arc,newGraph.liste_arc)
    return newGraph

def afficher(graph):
    liste_arc=graph.liste_arc
    for i in range (len(liste_arc)):
        liste_arc[i]=liste_arc[i].split(" ")
    print(liste_arc)
    num_list=[]
    for i in range (len(liste_arc)):
        num_list.append([])
        for j in range (len(liste_arc[i])):
            num_list[i].append(int(liste_arc[i][j]))
    print("num_list")
    print(num_list)
    matrice= [["-" for i in range(int(graph.nb_sommet))]for j in range(int(graph.nb_sommet))]
    print(matrice)
    for i in range(int(graph.nb_sommet)):
       for j in range(len(num_list)):
           print(num_list[j])
           print(i)
           if num_list[j][0] == i:
               print("hit")
               matrice[i][num_list[j][1]]=num_list[j][2]
           #else:
               #print("miss")
               #print(num_list[j][1])
               #matrice[i][num_list[j][1]]="-"
    return matrice

def adjacent(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "-":
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix




def algo_Floyd_Warshall(matrice,n):
    L = [["∞" for i in range(n)] for j in range(n)]
    P = [["-" for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if matrice[i][j]!="-":
                L[i][j]=matrice[i][j]
            P[i][j]=i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if L[i][k]+L[k][j]<L[i][j]:
                    L[i][j]=L[i][k]+L[k][j]
                    P[i][j]=P[k][j]
        affichage_mat(L,P)
    return 0

def affichage_mat(L,P):
    a=0







