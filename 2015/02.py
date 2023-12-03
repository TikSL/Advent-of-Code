# ADVENT-OF-CODE 2015
# Jour 2
# https://adventofcode.com/2015/day/2

# --- Day 2: I Was Told There Would Be No Math ---

# Partie 1 et 2

lines = open('02.txt', 'r').readlines()
dimensions = []
for line in lines :
    dimensions.append(line.strip().split("x"))

surface = 0
ribbon = 0

for l,w,h in dimensions:
    l, w, h = int(l), int(w), int(h)
    surface += 2*l*w +2*w*h + 2*h*l + min(l*w,w*h,h*l)
    ribbon += l*w*h + 2* (l+h+w - max(l,h,w))


print(f'Partie 1 : {surface}')
print(f'Partie 2 : {ribbon}')
