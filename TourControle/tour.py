#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import time


def convertToMin(s):
    l = s.split(":")
    return int(l[0])*60 + int(l[1])

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
N = int(lines[0])
sys.stderr.write(str(N))
sys.stderr.write("\n")
X = int(lines[1])
sys.stderr.write(str(X))
sys.stderr.write("\n")
P = []
H = []

aeroport = {}
for j in range(2, N+2):
    l = lines[j].split()
    if l[1] not in aeroport:
        aeroport[l[1]] = [convertToMin(l[0])]
    else:
        aeroport[l[1]]  = aeroport[l[1]] + [convertToMin(l[0])]
sys.stderr.write(str(aeroport))
sys.stderr.write("\n")

collision = False
for key in aeroport:
    val = aeroport[key]
    for k in range(0, len(aeroport[key])-1):
        if val[k+1] - val[k] < 6:
            collision = True
            break
    for l in range(0, len(aeroport[key])-X):
        if val[l+X] - val[l] <= 45:
            collision = True
            break

if collision:
    print("COLLISION")
else:
    print("OK")