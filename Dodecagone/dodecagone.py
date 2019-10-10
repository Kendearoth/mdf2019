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
D = [["."] * N for i in range(0,N)]
sys.stderr.write(str(D))
nb = (N - 1) // 2
milieu = (N - 1) // 2
sys.stderr.write(str(milieu))
#init
for k in range(0, len(D)):
    D[k] = list(D[k])
D[milieu][milieu] = '*'
D[milieu-1][milieu] = "*"
D[milieu+1][milieu] = "*"
D[milieu][milieu-1] = "*"
D[milieu][milieu+1] = "*"
sys.stderr.write("\n")
sys.stderr.write(str(D))

def remplit(i,j):
    if D[i][j] == "*":
        if D[i-1][j] == ".":
            D[i-1][j] == "#"
        if D[i-1][j-1] == ".":
            D[i-1][j] == "#"
        if D[i-1][j+1] == ".":
            D[i-1][j+1] == "#"
        if D[i][j+1] == ".":
            D[i][j+1] == "#"
        if D[i][j-1] == ".":
            D[i][j-1] == "#"
        if D[i+1][j] == ".":
            D[i+1][j] == "#"
        if D[i+1][j-1] == ".":
            D[i+1][j-1] == "#"
        if D[i+1][j+1] == ".":
            D[i+1][j+1] == "#"
    else:
        if D[i-1][j] == ".":
            D[i-1][j] == "*"
        if D[i-1][j-1] == ".":
            D[i-1][j] == "*"
        if D[i-1][j+1] == ".":
            D[i-1][j+1] == "*"
        if D[i][j+1] == ".":
            D[i][j+1] == "*"
        if D[i][j-1] == ".":
            D[i][j-1] == "*"
        if D[i+1][j] == ".":
            D[i+1][j] == "*"
        if D[i+1][j-1] == ".":
            D[i+1][j-1] == "*"
        if D[i+1][j+1] == ".":
            D[i+1][j+1] == "*"
    return

for nbDode in range(0,nb-1):
    for l in range(0, N):
        for c in range(0, N):
            if D[l][c] != ".":
                if D[l][c] == "*":
                    if D[l-1][c] == ".":
                        sys.stderr.write("ok")
                        D[l-1][c] = "#"
                    if D[l-1][c-1] == ".":
                        D[l-1][c] = "#"
                    if D[l-1][c+1] == ".":
                        D[l-1][c+1] = "#"
                    if D[l][c+1] == ".":
                        D[l][c+1] = "#"
                    if D[l][c-1] == ".":
                        D[l][c-1] = "#"
                    if D[l+1][c] == ".":
                        D[l+1][c] = "#"
                    if D[l+1][c-1] == ".":
                        D[l+1][c-1] = "#"
                    if D[l+1][c+1] == ".":
                        D[l+1][c+1] = "#"
                else:
                    if D[l-1][c] == ".":
                        sys.stderr.write("ok")
                        D[l-1][c] = "*"
                    if D[l-1][c-1] == ".":
                        D[l-1][c-1] = "*"
                    if D[l-1][c+1] == ".":
                        D[l-1][c+1] = "*"
                    if D[l][c+1] == ".":
                        D[l][c+1] = "*"
                    if D[l][c-1] == ".":
                        D[l][c-1] = "*"
                    if D[l+1][c] == ".":
                        D[l+1][c] = "*"
                    if D[l+1][c-1] == ".":
                        D[l+1][c-1] = "*"
                    if D[l+1][c+1] == ".":
                        D[l+1][c+1] = "*"
        sys.stderr.write("\n")
        for ligne in D:
            sys.stderr.write(str(ligne))
            sys.stderr.write("\n")