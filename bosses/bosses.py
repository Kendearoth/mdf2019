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
sys.stderr.write("\n")
poteaux = []
for i in range(1, N+1):
    poteaux.append(int(lines[i]))
poteaux.sort()
sys.stderr.write(str(poteaux))
for j in range(0, )


1 2 3 4
1 3 2 4

1 2 3 4 5
1 3 2 4 5