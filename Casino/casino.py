#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import re

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
N = int(lines[0])
sys.stderr.write(str(N))
sys.stderr.write("\n")
nb_jetons_init = int(lines[1])
sys.stderr.write(str(nb_jetons_init))
sys.stderr.write("\n")
nb_jetons = nb_jetons_init

rachat = 0
for i in range(2,N+2):
    mise, quoi, nb_sorti = lines[i].split()
    #sys.stderr.write(mise)
    #sys.stderr.write(" ")
    #sys.stderr.write(quoi)
    #sys.stderr.write(" ")
    #sys.stderr.write(nb_sorti)
    #sys.stderr.write("\n")
    mise = int(mise)
    nb_sorti = int(nb_sorti)
    # Q = [0-36] ou I/P
    if (nb_jetons - mise) <= 0:
        rachat += 1
        nb_jetons += nb_jetons_init
    # on enlève la mise
    nb_jetons -= mise

    if not re.match(r"[I,P]",quoi):
        quoi = int(quoi)
        if quoi == nb_sorti:
            nb_jetons += mise * 35
        else:
            nb_jetons -= mise
    else:
        if quoi == "I":
            if nb_sorti % 2 != 0:
                nb_jetons += mise
            else:
                nb_jetons -= mise
        elif quoi == "P":
            if nb_sorti % 2 == 0 and nb_sorti != 0:
                nb_jetons += mise
            else:
                nb_jetons -= mise
        else:
            sys.stderr.write("ERROR")
    #sys.stderr.write("jetons : ")
    #sys.stderr.write(str(nb_jetons))
    #sys.stderr.write("\n")
sys.stderr.write("\n")
sys.stderr.write(str(rachat))
sys.stderr.write("\n")
sys.stderr.write("----")
sys.stderr.write("\n")
print(rachat)







