import random
import time

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

def binary_search(sorted_data, target):
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


def hashmap(data, target):
    if target in data:
        return data[target], target
    return None

def time_search(func, data, target, runs=1000):
    start = time.perf_counter()
    for _ in range(runs):
        result = func(data, target)
    elapsed = time.perf_counter() - start
    avg_microseconds = (elapsed / runs) * 1_000_000
    return result, avg_microseconds


def compare(data, target):
    print(f"Total drivers: {len(data):,}")
    print(f"Target driver ID: {target}\n")

    linear_result, linear_time = time_search(linear_search, data, target)
    print(f"Linear search   (O(N)):      {linear_result}  -  {linear_time:.2f} µs")

    binary_result, binary_time = time_search(binary_search, sorted(data.items()), target)
    print(f"Binary search   (O(log N)):  {binary_result}  -  {binary_time:.2f} µs")

    hashmap_result, hashmap_time = time_search(hashmap, data, target)
    print(f"Hashmap lookup  (O(1)):      {hashmap_result}  -  {hashmap_time:.2f} µs")

    print("\n--- Summary ---")
    if binary_time > 0:
        print(f"Binary search was ~{linear_time / binary_time:,.1f}x faster than linear search.")
    if hashmap_time > 0:
        print(f"Hashmap was ~{linear_time / hashmap_time:,.1f}x faster than linear search.")
        print(f"Hashmap was ~{binary_time / hashmap_time:,.1f}x faster than binary search.")


def main():
    target = gen_target()
    compare(drivers, target)


if __name__ == "__main__":
    main()
