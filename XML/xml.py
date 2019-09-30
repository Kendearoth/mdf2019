#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def takeSecond(elem):
    return elem[1]

lines = []
listChar = []
for line in sys.stdin:
    sys.stderr.write(str(line))
    res = []
    p = 0
    i = 0
    while i < len(line):
        if line[i] != "-" and line[i] != "\n":
            p+=1
            res.append([line[i],p])
            i+=1
        elif line[i] == "-":
            p-=1
            i+=2
        else:
            i+=1
    res.sort(key=takeSecond)
    sys.stderr.write(str(res))


#lines.append(line.rstrip('\n'))