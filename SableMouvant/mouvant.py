#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import re

lines = []
j = 0
H = 1
for line in sys.stdin:
    maxProfondeur = 0 #init
    #strTmp2 = "j : " + str(j) + " | H : " + str(H) + "\n"
    #sys.stderr.write(strTmp2)
    if re.match("^[0-9]+ [0-9]+", line):
        maxProfondeur = 0 #reinit
        form = line.split()
        H = form[0]
        L = form[1]
        strTmp = "H : " + str(H) + " | L : " + str(L) + "\n"
        sys.stderr.write(strTmp)
    elif j < int(H) - 1:
        sys.stderr.write(str(j))
        #sys.stderr.write(line)
        lines.append(line[:-1])
        j += 1
    elif j == int(H) - 1:
        sys.stderr.write(str(lines))
        lines = []
        j = 0
        H = 1
        print("ok")

    #lines.append(line.rstrip('\n'))

def parcours(i,j,p):
    coords = [[i,j+1],[i-1,j],[i,j-1],[i+1,j]]
    for coord in coords:
        if  0 <= coord[0] < H and 0 <= coord[1] < L: #si nous ne sommes pas aux limites
            if lines[coord[0]][coord[1]] != ".":
                return 
            