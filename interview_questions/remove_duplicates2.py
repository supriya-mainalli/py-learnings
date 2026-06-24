nums = [1, 1, 2, 3, 3, 4, 5, 5]

# Expected output:
[1, 2, 3, 4, 5]


def remove_duplicates(nums):
    seen = set()
    for item in nums:
        if item not in seen:
            seen.add(item)

    return list(seen)

print(remove_duplicates(nums))