#!/usr/bin/env python
import sys

def partitions():
    l = []
    for s in range(5,13):
        l1 = []
        for i in range(len(c) - (s-1)):
            l1.append(c[i:i + s])
        l.append(l1)
    return l

def find_Pattern(l):
    s=5
    for lista in l:
        while len(lista) !=0 :
            pattern = lista.pop()
            if pattern in lista:
                spaceBtwPattern(pattern,s)
            else:
                continue
        s+=1

def spaceBtwPattern(pattern, s):
    first_index = c.find(pattern) + (s - 1)
    last_index = c.find(pattern, first_index) + (s - 1)
    tabela[pattern] = last_index - first_index

def get_key():
    find_Pattern(partitions())
    distancias = tabela.values()#debug

    if not distancias:
        return -1

    result = distancias[0]
    for i in distancias[1:]: #calcula o mdc do espaco amostral
        result = gcd(result, i)
    return result

def gcd(a, b):
    while b > 0:a, b = b, a % b
    return a

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        c = ""
        tabela = {}
        for linha in file:
              c += linha.replace(' ', '').replace('\n','')
        print "Size of key is" , get_key()
