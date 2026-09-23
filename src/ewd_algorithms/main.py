import random

from ewd_algorithms.drivers import drivers

def gen_target():
    number= random.randint(1, 10000)
    padded = f"DRV{number:05d}"
    return padded

def linear_search(data, target):
    for driver_id, name in data.items():
        if driver_id == target:
            return name, driver_id
    return None

def binary_search(data, target):
    # Convert the dictionary into a sorted list of (driver_id, name)
    sorted_data = sorted(data.items())

    left = 0
    right = len(sorted_data) - 1

    while left <= right:
        middle = (left + right) // 2

        driver_id, name = sorted_data[middle]

        if driver_id == target:
            return name, driver_id

        elif driver_id < target:
            # Target is in the right half
            left = middle + 1

        else:
            # Target is in the left half
            right = middle - 1

    return None


def hashmap(data):
    pass

target = gen_target()
print(linear_search(drivers, target))
print(binary_search(drivers, target))