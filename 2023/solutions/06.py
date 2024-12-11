# ADVENT-OF-CODE 2023
# Jour 6
# https://adventofcode.com/2023/day/6

# --- Day 6: Wait For It ---

# Partie 1 :

time = [46,68,98,66]
distance = [358,1054, 1807, 1080]

def mul_nbr_records(times, distances):
    sum = []
    for i, t in enumerate(times):
        record = distances[i]
        somme_record = 0
        for k in range(t):
            vitesse = k
            dist_essai = (t-k) * vitesse
            if dist_essai > record:
                somme_record += 1
        sum.append(somme_record)
    pdt = 1
    for x in sum:
        pdt *= x
    return pdt


print(f"Partie 1 : {mul_nbr_records(time, distance)}")

# Partie 2 :

time2 = [46689866]
distance2 = [358105418071080]

print(f"Partie 2 : {mul_nbr_records(time2, distance2)}")