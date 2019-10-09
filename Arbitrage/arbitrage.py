#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
montant = float(10000)
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

sys.stderr.write(str(lines))
l = lines[0].split()
N = l[0]
M = l[1]
sys.stderr.write("\n")
convM = []
for i in range(1, int(N)+1):
    l = lines[i].split()
    taux = [float(l[j]) for j in range(0, len(l))]
    convM.append(taux)
sys.stderr.write(str(convM))
sys.stderr.write("\n")
k = 0
currency = 0
while k < int(M) or int(M)-k > int(N):
    sys.stderr.write(str(k))
    sys.stderr.write(str(" "))
    if k+1 % int(N) != 0:
        montant *= max(convM[currency % int(N)])
    else:
        montant *= convM[currency][0]
    sys.stderr.write(str(montant))
    currency += 1
    k += 1
    sys.stderr.write("\n")
print(montant)

