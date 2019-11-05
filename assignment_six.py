#By Kwame Boamah on Tuesday, November 5, 2019


def main():
    chosen_number = int(input("Pick a number"))
    list_1 = []
    for x in range(2, chosen_number + 1):
        list_1.append(x)
    empty_list = []
    for x in range(len(list_1)):
        if list_1[x] / list_1[x] == 1:
            empty_list.append(x)
            if x % list_1:
                list_1.remove(x)
                print(empty_list)


main()
