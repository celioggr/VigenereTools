#!/usr/bin/env python
import sys
def stats(pointer, size):
    freqs = dict([(chr(i), 0) for i in range(ord('a'), ord('z') + 1)])
    count=0
    while 1:
        if( pointer < len(c) ):
            freqs[c[pointer]] += 1
            pointer += size
            count += 1
        else:
            break

    for n in freqs.keys():
        freqs[n] = freqs.get(n) * 100 / count
    return freqs


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        min = raw_input("Define lowest length of the key to work with:\n")
        max = raw_input("As well as the maximum:\n")
        c = ""
        icPT = 7.77 #Index of coincidence of language
        list_of_ics = []
        for line in file:
            c += line.replace(' ', '').replace('\n', '').lower()
        index = 0
        for col in range(int(min),int(max)):
            somatorio = 0.0
            q2 = 0.0
            for freq in stats(index,col).values():
                q2= float(freq*freq)
                somatorio += q2
            list_of_ics.append(somatorio / 100)
            index+=1
        print "Key length will be the closest number to ", icPT, ". ( Notice that the first element of the list corresponds to a key length of",min,")\n"
        print list_of_ics

