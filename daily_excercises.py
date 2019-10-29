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


def main():
    print(are_duplicates([1, 2, 3, 4, 5, 6, 3, 7]))
    print(add_numbers([1, 2, 3, 6, 6, 7]))


main()
