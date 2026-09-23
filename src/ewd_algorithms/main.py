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

def binary_search(data):
    pass

def hashmap(data):
    pass

target = gen_target()
print(linear_search(drivers, target))