#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
N, Q = lines[0].split()
N = int(N)
Q = int(Q)
sys.stderr.write(str(N))
sys.stderr.write("\n")
sys.stderr.write(str(Q))
sys.stderr.write("\n")
assesseurs = []
for i in range(2, N+1):
    assesseur_corruptible = lines[i].split()
    assesseurs.append([int(assesseur_corruptible[0]),int(assesseur_corruptible[1])])
assesseurs.sort(key=lambda elem: elem[1])
montant = 0
for i in range(0, len(assesseurs)):
    if Q <= 0:
        break
    montant += assesseurs[i][0]
    Q -= assesseurs[i][1]
if Q > 0:
    print("MANIPULATION")
else:
    print(montant)
sys.stderr.write(str(montant))
sys.stderr.write("\n")



sys.stderr.write(str(assesseurs))