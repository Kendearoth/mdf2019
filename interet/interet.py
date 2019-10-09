#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
i = 0
solde = intPast = intNow = 0.0
nbJourNegatif = 0
for line in sys.stdin:
    if i == 0:
        nbJours = int(line)
        sys.stderr.write("jours ")
        sys.stderr.write(str(nbJours))
        sys.stderr.write(str("\n"))

    elif i == 1:
        solde = float(line)
        sys.stderr.write("solde ")
        sys.stderr.write(str(solde))
        sys.stderr.write(str("\n"))

    else:
        variation = int(line)
        sys.stderr.write(str(line))
        solde += variation
        sys.stderr.write(" | ")
        sys.stderr.write(str(solde))
        sys.stderr.write(str("\n"))
        if solde < 0 and nbJourNegatif > 3:
            intPast += ((abs(solde) * 10) / 100)
            intNow += ((abs(solde) * 30) / 100)
            nbJourNegatif += 1
        elif solde < 0 and nbJourNegatif > 2:
            intNow += ((abs(solde) * 20) / 100)
            intPast += ((abs(solde) * 10) / 100)
            nbJourNegatif += 1
        elif solde < 0:
            intNow += ((abs(solde) * 20) / 100)
            nbJourNegatif += 1
        else:
            nbJourNegatif = 0


    i += 1
#	lines.append(line.rstrip('\n'))

print(abs(intNow - intPast))