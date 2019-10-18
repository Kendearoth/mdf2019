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
N, M = lines[0].split()
nb_personne = int(N)
relations = int(M)
#amities = [lines[i].split() for i in range(1, relations+1)]
amities = []
for i in range(1, relations+1):
    l = lines[i].split()
    amities.append([int(l[0]), int(l[1])])
print_ln(str(nb_personne))
print_ln(str(relations))
print_ln(str(amities))

myFriends = []
for elem in amities:
    if elem[0] == 1:
        myFriends.append(int(elem[1]))
print_ln(str(myFriends))
if myFriends == None:
    print(-1)

maxAmisCommun = 0
BFF = 0
for friend in myFriends:
    nbAmis = 0
    friendsOfMyFriends = []
    if elem[0] == friend:
        friendsOfMyFriends.append((int(elem[1])))
    myFriendsWithoutHim = myFriends.remove(friend)
    if myFriendsWithoutHim == None:
        print(friend)
    for f in myFriendsWithoutHim:
        if f in friendsOfMyFriends:
            nbAmis += 1
    if nbAmis > maxAmisCommun:
        maxAmisCommun = nbAmis
        BFF = friend
if maxAmisCommun == 0:
    print(-1)
else:
    print(BFF)
