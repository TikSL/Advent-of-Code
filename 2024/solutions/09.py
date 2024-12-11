# ADVENT-OF-CODE 2024
# Jour 9
# https://adventofcode.com/2024/day/9

# --- Day 9: Disk Fragmenter ---

def checksum(disk_zones):
    return sum(zone[0] * k for zone in disk_zones for k in range(zone[2], zone[2] + zone[1]))

with open("../inputs/09.txt") as file:
    disk_map = file.readlines()[0].strip()

# Partie 1

disk = []
disk_none = []
value = 0
index_zone = 0
is_filled_zone = True

for i, char in enumerate(disk_map):
    nbr = int(char)
    if is_filled_zone:
        zone_data = (value, nbr, index_zone)
        disk.append(zone_data)
        value += 1
    else:
        if nbr != 0:
            zone_none = (nbr, index_zone)
            disk_none.append(zone_none)

    is_filled_zone = not is_filled_zone
    index_zone += nbr

data_zones = disk.copy()
none_zones = disk_none.copy()

disk_final = []

while none_zones:
    zone_none = none_zones[0]
    nbr_none = zone_none[0]
    index_none = zone_none[1]

    zone_data = data_zones[-1]
    value_data = zone_data[0]
    nbr_data = zone_data[1]
    index_data = zone_data[2]

    if index_none > index_data:
        break
    if nbr_data > nbr_none:
        disk_final.append((value_data, nbr_none, index_none))
        none_zones.pop(0)
        data_zones.pop()
        data_zones = data_zones + [(value_data, nbr_data - nbr_none, index_data)]

    elif nbr_data == nbr_none:
        disk_final.append((value_data, nbr_none, index_none))
        none_zones.pop(0)
        data_zones.pop()

    else:
        disk_final.append((value_data, nbr_data, index_none))
        none_zones.pop(0)
        none_zones = [(nbr_none - nbr_data, index_none + nbr_data)] + none_zones
        data_zones.pop()

print(f"Partie 1 : {checksum(disk_final) + checksum(data_zones)}")

# Partie 2

data_zones = disk.copy()
none_zones = disk_none.copy()

disk_final = []

for i in range(len(data_zones)):
    zone_data = data_zones[len(data_zones) - i - 1]

    value_data = zone_data[0]
    nbr_data = zone_data[1]
    index_data = zone_data[2]

    found = False
    for j, zone_none in enumerate(none_zones):

        nbr_none = zone_none[0]
        index_none = zone_none[1]
        if index_none < index_data:
            if nbr_none > nbr_data:
                disk_final.append((value_data, nbr_data, index_none))
                none_zones.remove(zone_none)
                none_zones = none_zones[:j] + [(nbr_none - nbr_data, index_none + nbr_data)] + none_zones[j:]
                found = True
                break

            elif nbr_data == nbr_none and index_none < index_data:
                disk_final.append((value_data, nbr_data, index_none))
                none_zones.remove(zone_none)
                found = True
                break

    if not found:
        disk_final.append((value_data, nbr_data, index_data))

print(f"Partie 2 : {checksum(disk_final)}")
