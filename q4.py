k = int(input("Enter how much you want to slice: "))
def bubblesort(list):
    indexlen = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexlen):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list [i+1] = list [i+1], list[i]

    return list

print(bubblesort([10,23,5,4,11])[-k:])