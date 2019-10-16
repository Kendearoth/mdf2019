#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def convertToMin(s):
    l = s.split(":")
    return int(l[0])*60 + int(l[1])

def keyToWatch(s, voitures):
    res = []
    if s=='S' or s=='N':
        if 'O' in voitures:
            res.append('O')
        if 'E' in voitures:
            res.append('E')
        return res
    else:
        if 'N' in voitures:
            res.append('N')
        if 'S' in voitures:
            res.append('S')
        return res

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
N = int(lines[0])
sys.stderr.write(str(N))
sys.stderr.write("\n")
voitures = {}
for i in range(1, N+1):
    l = lines[i].split()
    if l[1] not in voitures:
        voitures[l[1]] = [convertToMin(l[0])]
    else:
        voitures[l[1]]  = voitures[l[1]] + [convertToMin(l[0])]
sys.stderr.write(str(voitures))
sys.stderr.write("\n")
collision =  False
for direction in voitures:
    # Pour toutes les voitures dans la direction à vérifer
    voituresTest = voitures[direction]
    for iVtest in range(0, len(voituresTest)):
        directionToWatch = keyToWatch(direction, voitures)
        for d in directionToWatch:
            voituresCible = voitures[d]
            # Pour toutes les voitures dans la direction cible 
            for iVCible in range(0, len(voituresCible)):
                if abs(voituresTest[iVtest] - voituresCible[iVCible]) < 3:
                    collision = True
                    break
if collision:
    print("COLLISION")
else:
    print("OK")
sys.stderr.write(collision)
sys.stderr.write("\n")