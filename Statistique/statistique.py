#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def print_ln(s):
    sys.stderr.write(s)
    sys.stderr.write("\n")

def invLigneColonne(lines):
    col = []
    for j in range(len(lines)):
        col.append("")
        for k in range(len(lines[0])):
            col[j] = str(col[j]) + str(lines[k][j])
    return col

def ints():
    return list(map(int, input().split()))

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
N = int(lines[0])
releve = [int(lines[i]) for i in range(0, len(lines)-1)]
print_ln(str(releve))
max_global = max(releve)
index_max_global = releve.index(max_global)
