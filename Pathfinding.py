
class Graph:
    def __init__(self):
        self.nb_sommet = 0
        self.nb_arc = 0
        self.liste_arc = []

def lecture(nb):
    newGraph=Graph()
    #with open("résultats"+str(nb)+".txt","w+") as g:
    with open("graphes/"+str(nb),"r") as f:
            a=0

            for line in f.readlines():
                #g.write(line)
                if a == 0:
                    newGraph.nb_sommet=line[:len(line)-1]
                if a == 1:
                    newGraph.nb_arc=line[:len(line)-1]
                if line[len(line)-1:len(line)] != "\n":
                    newGraph.liste_arc.append(line)
                elif a >= 2:
                    newGraph.liste_arc.append(line[:len(line)-1])
                a+=1
    #print(newGraph.nb_sommet,newGraph.nb_arc,newGraph.liste_arc)
    return newGraph

def afficher(graph):
    liste_arc=graph.liste_arc
    for i in range (len(liste_arc)):
        liste_arc[i]=liste_arc[i].split(" ")
    #print(liste_arc)
    num_list=[]
    for i in range (len(liste_arc)):
        num_list.append([])
        for j in range (len(liste_arc[i])):
            num_list[i].append(int(liste_arc[i][j]))
    #print("num_list")
    #print(num_list)
    matrice= [["-" for i in range(int(graph.nb_sommet))]for j in range(int(graph.nb_sommet))]
    #print(matrice)
    for i in range(int(graph.nb_sommet)):
       for j in range(len(num_list)):
           #print(num_list[j])
           #print(i)
           if num_list[j][0] == i:
               #print("hit")
               matrice[i][num_list[j][1]]=num_list[j][2]
           #else:
               #print("miss")
               #print(num_list[j][1])
               #matrice[i][num_list[j][1]]="-"
    for i in range(int(graph.nb_sommet)):
        matrice[i][i]=0
    return matrice

def adjacent(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "-":
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix




def algo_Floyd_Warshall(matrice):
    #for i in range(len(matrice)):
        #L[i][i]=0
    mat=matrice
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i==j:
                mat[i][j]=0
            if matrice[i][j] != "-":
                mat[i][j] = int(matrice[i][j])
            else:
                mat[i][j] = 9999
    n=len(matrice)
    L = [[9999 for i in range(n)] for j in range(n)]
    P = [["-" for i in range(n)]for j in range(n)]
    for i in range(n):
        L[i][i]=0
    for i in range(n):
        for j in range(n):
            if matrice[i][j]!="-":
                L[i][j]=int(matrice[i][j])
            P[i][j]=i
    i=0
    for k in range(n):

        print("affichage énumération n°" + str(k))
        for i in range(n):
            for j in range(n):
                if L[i][k]+L[k][j]<L[i][j]:
                    L[i][j]=L[i][k]+L[k][j]
                    P[i][j]=P[k][j]
        affichage_mat(L,P)
    #affichage_mat(L,P)
    return L,P

def affichage_mat(L,P):
    print("affichage L")
    M = [[0 for i in range(len(L))] for j in range(len(L))]

    for i in range (len(L)):
        for j in range (len(L[i])):
            if L[i][j] >= 9000:
                M[i][j]='∞'
            else:
                M[i][j]=L[i][j]
    M1=np.array(M)
    print(M1)
    #print("affichage vrai L")
    #print(L)
    print("affichage P")
    #print(P)
    P2=np.array(P)
    print(P2)

import numpy as np


def click(x):
    print("click")
    graphe=lecture(str(x)+".txt")
    print("tableau d'adjacence du graphe")
    a=np.array(afficher(graphe))
    print(a)
    b,c=algo_Floyd_Warshall(a)
    #print(b,c)
    interface(b,c)

def circuit_absorbant(P):
    n=len(P)
    for i in range(n):
        if P[i][i]<0:
            return True
    return False

import math

def has_negative_cycle(P):
    return any(P[i][i] < 0 for i in range(len(P)))

def reconstruct_path(L, s, t):
    path = []
    current = t

    while current != s:
        path.append(current)
        current = L[s][current]
        if current is None:
            return None  # sécurité

    path.append(s)
    return path[::-1]

def interface(P, L):
    if has_negative_cycle(P):
        print("Circuit absorbant détecté")
        return

    n = len(P)

    while True:
        rep = input("Chemin ? (oui/non) : ")
        if rep.lower() != "oui":
            break

        s = int(input("Sommet de départ : "))
        t = int(input("Sommet d'arrivée : "))
        while(s<0 or s>len(P)-1 or t<0 or t>len(P)-1):
            print("sommets imcompatibles")
            s = int(input("Sommet de départ : "))
            t = int(input("Sommet d'arrivée : "))
        if P[s][t] >9000:
            print("Pas de chemin")
        else:
            path = reconstruct_path(L, s, t)
            print("Chemin :", path)
            print("Coût :", P[s][t])
    interfaceglobale()

def interfaceglobale():
    print("choisissez un graphe:")
    x=input()
    click(x)




def test_graphes():
    for i in range(13):
        with open("résultats" + str(i+1) + ".txt", "w+") as g:
            f=afficher(lecture(str(i+1)+".txt"))
            a=np.array(f)
            g.write("tableau d'adjacence du graphe")
            g.write("\n"+str(a)+"\n")
            g.write("affichage L")
            b,c=np.array(algo_Floyd_Warshall(a))
            g.write("\n"+str(b)+"\n")
            g.write("affichage P")
            g.write("\n"+str(c)+"\n")

#test_graphes()
interfaceglobale()
