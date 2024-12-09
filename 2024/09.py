# ADVENT-OF-CODE 2024
# Jour 9
# https://adventofcode.com/2024/day/9

# --- Day 9: Disk Fragmenter ---

disk_flat = []
disk_segmented = []

with open("input/09.txt") as file:
    lines = file.readlines()
    disk_map_flat = lines[0].strip()
    disk_map_segmented = lines[0].strip()

index_counter = 0
is_filled_zone = True

for char in disk_map_flat:
    if is_filled_zone:
        zone_data = [index_counter for _ in range(int(char))]
        index_counter += 1
        is_filled_zone = False
    else:
        zone_data = [None for _ in range(int(char))]
        is_filled_zone = True

    if zone_data:
        disk_segmented.append(zone_data)
    for item in zone_data:
        disk_flat.append(item)

def calculate_checksum(disk):
    checksum_value = 0
    for index, value in enumerate(disk):
        checksum_value += (value or 0) * index
    return checksum_value

# Partie 1
while None in disk_flat:
    empty_space_index = disk_flat.index(None)
    last_value = disk_flat[-1]
    disk_flat[empty_space_index] = last_value
    disk_flat.pop()

print(f"Partie 1 : {calculate_checksum(disk_flat)}")

# Partie 2
for i in range(len(disk_segmented)):
    segment_index = len(disk_segmented) - i - 1
    segment_to_move = disk_segmented[segment_index]

    if segment_to_move[0] is not None:
        segment_size = len(segment_to_move)
        for previous_segment in disk_segmented[:segment_index]:
            if previous_segment[0] is None and len(previous_segment) >= segment_size:

                disk_segmented.remove(segment_to_move)
                disk_segmented.insert(segment_index, [None for _ in range(segment_size)])

                previous_segment_index = disk_segmented.index(previous_segment)
                new_empty_segment = [None for _ in range(len(previous_segment) - segment_size)]

                disk_segmented.remove(previous_segment)
                disk_segmented.insert(previous_segment_index, segment_to_move)

                if new_empty_segment:
                    disk_segmented.insert(previous_segment_index + 1, new_empty_segment)
                break


def flatten_segmented_disk(segmented_disk):
    flat_disk = []
    for segment in segmented_disk:
        flat_disk.extend(segment)
    return flat_disk

flattened_disk = flatten_segmented_disk(disk_segmented)
print(f"Partie 2 : {calculate_checksum(flattened_disk)}")
