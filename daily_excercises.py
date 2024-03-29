# By Kwame Boamah

# names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen", "Jackie", "Kurt",
#          "Linda"]
# print(names[3:5])
# print(names[1:6])
# print(names[5:13])
# print(names[5:])
# print(names[11])
# print(names[-1])
# print(names[1:8:2])
# print(names[::2])
# print(names[0:12:2])
# print(names[12:8:-1])
# print(names[::-1])
# print(names[12::-1])


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


def add_numbers(nums):
    total = 0
    for x in nums:
        total += x
    print(total)


def has22(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == 2 and nums[y] == 2:
                return True
    return False


def is_sorted(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] < nums[y]:
                return True
    return False


def remove_duplicates(nums):
    blank = []
    for x in nums:
        if x not in blank:
            blank.append(x)
    print(blank)


def get_max(nums):
    bigest_number = nums[0]
    for x in nums:
        if x > bigest_number:
            bigest_number = x
    print(bigest_number)


def get_min(nums):
    smallest_number = nums[0]
    for x in nums:
        if x < smallest_number:
            smallest_number = x
    print(smallest_number)


def main():
    print(are_duplicates([1, 2, 3, 4, 5, 6, 3, 7]))
    add_numbers([1, 2, 3, 6, 6, 7])
    print(has22([1, 2, 2, 3]))
    print(is_sorted([1, 2, 3]))
    remove_duplicates([1, 3, 5, 7, 8, 8, 3, 9])
    get_max([1, 23, 43, 54, 93, 56, 19, 30, 28, 5, 1, 53, 99])
    get_min([1, 2, 66, 83, 321, -8, -2, -53, -62, 26, -24578, -43])

main()
