#By Kwame Boamah on Tuesday, November 5, 2019


def main():
    chosen_number = int(input("Pick a number"))
    list_1 = []
    for x in range(2, chosen_number + 1):
        list_1.append(x)
    empty_list = []
    while list_1 != []:
        empty_list.append(list_1[0])
        current_number = list_1[0]
        for x in list_1:
            if x % current_number == 0:
                list_1.remove(x)
    print(empty_list)


main()
