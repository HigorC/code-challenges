# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    n = len(q)

    listaDefault = list(range(1, n + 1))

    numMinTrocas = 0

    contadorDeTrocas = []
    for i in range(n):
        contadorDeTrocas.append(0)

    while q != listaDefault:

        listTrocasMaioresque2 = list(filter(lambda x: x > 2, contadorDeTrocas))
        if len(listTrocasMaioresque2) > 0:
            print("Too chaotic")
            # return

        distanciasDasPosicoesCorretas = []

        for k in listaDefault:
            distanciasDasPosicoesCorretas.append(abs((q.index(k) + 1) - k))

                # = [abs((q.index(k) + 1) - 1),
                #                          abs((q.index(k) + 1) - 2),
                #                          abs((q.index(k) + 1) - 3),
                #                          abs((q.index(4) + 1) - 4),
                #                          abs((q.index(5) + 1) - 5)]

        maiorTroca = max(distanciasDasPosicoesCorretas)

        # if maiorTroca > 2:
        #     print("Too chaotic")
        #     return


        indexDoNumeroComMaiorTrocaNoVetorCorreto = distanciasDasPosicoesCorretas.index(maiorTroca) + 1

        numComMaiorTrocas = listaDefault.index(indexDoNumeroComMaiorTrocaNoVetorCorreto) + 1

        indexDoNumeroComMaiorTrocaNoVetorErrado = q.index(numComMaiorTrocas) + 1

        estaParaEsquerda = q.index(numComMaiorTrocas) < indexDoNumeroComMaiorTrocaNoVetorCorreto

        if estaParaEsquerda:
            aux = q[indexDoNumeroComMaiorTrocaNoVetorErrado] # Sub e soma desnecessaria pq ja etou salvando com +1 >> - 1 + 1
            q[indexDoNumeroComMaiorTrocaNoVetorErrado] = q[indexDoNumeroComMaiorTrocaNoVetorErrado - 1]
            q[indexDoNumeroComMaiorTrocaNoVetorErrado - 1] = aux
            numMinTrocas += 1
            distanciasDasPosicoesCorretas[indexDoNumeroComMaiorTrocaNoVetorCorreto - 1] = -1
        else:
            aux = q[indexDoNumeroComMaiorTrocaNoVetorErrado - 1]  # Sub e soma desnecessaria pq ja etou salvando com +1 >> - 1 + 1
            q[indexDoNumeroComMaiorTrocaNoVetorErrado - 1] = q[indexDoNumeroComMaiorTrocaNoVetorErrado - 2]
            q[indexDoNumeroComMaiorTrocaNoVetorErrado - 2] = aux
            numMinTrocas += 1
            distanciasDasPosicoesCorretas[indexDoNumeroComMaiorTrocaNoVetorCorreto - 1] = -1

        # if contadorDeTrocas[indexDoNumeroComMaiorTrocaNoVetorCorreto - 1] == 0:
        #     contadorDeTrocas[indexDoNumeroComMaiorTrocaNoVetorCorreto - 1] = 1
        #
        # else:
        contadorDeTrocas[indexDoNumeroComMaiorTrocaNoVetorCorreto - 1] += 1

        pass
    print(numMinTrocas)




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
