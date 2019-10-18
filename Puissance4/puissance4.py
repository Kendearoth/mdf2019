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

J = ['JJJJJJJJ','JJJJJJJ','JJJJJJ','JJJJJ','JJJJ']
R = ['RRRRRRRR','RRRRRRR','RRRRRR','RRRRR','RRRR']

countJ = 0
countR = 0

def sizeLine(line):
    res = []
    for elem in J:
        if elem in line:
            res.append(['J', 8 - J.index(elem)])
            break
    for elem_ in R:
        if elem_ in line:
            res.append(['R', 8 - R.index(elem_)])
            break
    return res

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
for l in lines:
    res = sizeLine(l)
    if res != None:
        for res_item in res:
            if res_item[0] == 'R':
                countR += res_item[1] - 3
            else:
                countJ += res_item[1] - 3
    print_ln(str(sizeLine(l)))
print_ln(str(lines))
col = invLigneColonne(lines)
for c in col:
    res = sizeLine(c)
    if res != None:
        for res_item in res:
            if res_item[0] == 'R':
                countR += res_item[1] - 3
            else:
                countJ += res_item[1] - 3
    print_ln(str(sizeLine(c)))
print_ln(str(col))
print_ln("R : " + str(countR))
print_ln("J : " + str(countJ))

if countR > countJ:
    print("R")
elif countJ > countR:
    print("J")
else:
    print("NOBODY")


def invLigneColonne(lines):
    col = []
    for j in range(8):
        col.append("")
        for k in range(8):
            col[j] = str(col[j]) + str(lines[k][j])
    return col
