#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def takeSecond(elem):
    return elem[1]

lines = []
listChar = []
for line in sys.stdin:
    sys.stderr.write(str(line))
    #calcul de profondeur
    profondeur = []
    p = 0
    i = 0
    while i < len(line):
        if line[i] != "-" and line[i] != "\n":
            p+=1
            profondeur.append([line[i],p])
            i+=1
        elif line[i] == "-":
            p-=1
            i+=2
        else:
            i+=1

    #calcul du poids
    poids = [[],[]]
    for elem in  profondeur:
        if elem[0] in poids[0]:
            i = poids[0].index(elem[0])
            value = poids[1][i]
            poids[1][i] = value + 1/elem[1]
        else:
            poids[0].append(elem[0])
            poids[1].append(1/elem[1])

    #lettre max par ordre alphabétique
    maxLetter = ""
    maxValue = 0
    n = 0
    while n < len(poids[1]):
        if poids[1][n] > maxValue:
            maxValue = poids[1][n]
            maxLetter = poids[0][n]
        elif poids[1][n] == maxValue:
            if poids[0][n] < maxLetter:
                maxLetter = poids[0][n]
        n += 1
    sys.stderr.write(maxLetter)
    sys.stderr.write(str(maxValue))

    print(maxLetter)