#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def print_ln(s):
    sys.stderr.write(s)
    sys.stderr.write("\n")

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
reservoir_init = reservoir = int(lines[0])                 #litre
consommation = int(lines[1])                     #litre par 100km
stations = [int(lines[i]) for i in range(2, 5)]
distance = int(lines[5])
print_ln(str(reservoir))
print_ln(str(consommation))
print_ln(str(stations))
print_ln(str(distance))
res = "OK"
currentKm = 0
if (reservoir * (100/consommation)) < stations[0]:
    res = "KO"
for i in range(1,len(stations)-1):
    if (reservoir * (100/consommation)) < (stations[i+1] - stations[i]):
        res = "KO"
        break
if (reservoir * (100/consommation)) < (distance - stations[-1]):
    res = "KO"
print_ln(res)
print_ln("---------")
print(res)

