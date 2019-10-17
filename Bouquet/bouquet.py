#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
V, R, J, O = lines[0].split()
V = int(V)
R = int(R)
J = int(J)
O = int(O)
sys.stderr.write(str(V))
sys.stderr.write(" ")
sys.stderr.write(str(R))
sys.stderr.write(" ")
sys.stderr.write(str(J))
sys.stderr.write(" ")
sys.stderr.write(str(O))
sys.stderr.write("\n")
bouquet = 0
Vstock = Rstock = Jstock = Ostock = 0
for i in range(1, 7):
    Vd, Rd, Jd, Od = lines[i].split()
    Vstock += int(Vd)
    Rstock += int(Rd)
    Jstock += int(Jd)
    Ostock += int(Od)
    while Vstock > V and Rstock > R and Jstock > J and Ostock > O:
        Vstock -= V
        Rstock -= R
        Jstock -= J
        Ostock -= O
        bouquet += 1
print(bouquet)
sys.stderr.write(str(bouquet))
sys.stderr.write("\n")
