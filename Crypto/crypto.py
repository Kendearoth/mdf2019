#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = int(lines[0])
sys.stderr.write(str(N))
coursE = []
coursB = []
for i in range(1, N+1):
    l = lines[i].split()
    coursE.append(int(l[0]))
    coursB.append(int(l[1]))
sys.stderr.write("\n")
sys.stderr.write(str(coursE))
sys.stderr.write("\n")
sys.stderr.write(str(coursB))
variationE = 0
variationB = 0
etatE = -2
etatB = -2
for i in range(0, N-1):
    if coursE[i] == coursE[i+1] and etatE == -2:
        variation += 1
        etat = 0
    if coursE[i] < coursE[i+1] and etatE != 1:
        variationE += 1
        etatE = 1
    if coursE[i] > coursE[i+1] and etatE != -1:
        variationE += 1
        etatE = -1
    if coursE[i] == coursE[i+1] and etatB == -2:
        variation += 1
        etat = 0
    if coursB[i] < coursB[i+1] and etatB != 1:
        variationB += 1
        etatB = 1
    if coursB[i] > coursE[i+1] and etatB != -1:
        variationB += 1
        etatB = -1
sys.stderr.write("\n")
sys.stderr.write(str(variationE))
sys.stderr.write("\n")
sys.stderr.write(str(variationB))
sys.stderr.write("\n")
if variationE == variationB:
    print("KO")
elif variationE < variationB:
    print("ETHEREUM")
else:
    print("BITCOIN")