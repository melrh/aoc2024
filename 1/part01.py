list1, list2 = [], []

def sortLists(input):
    for line in input.readlines():
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

    list1.sort()
    list2.sort()

    return(str(calcDistance(list1, list2)))

def calcDistance(l1, l2):
    distance = 0

    for i, j in zip(l1, l2):
        if i > j:
            distance = distance + (i-j)
        elif j > i:
            distance = distance + (j-i)
    
    return distance


if __name__ == "__main__":
    with open('./input') as file:
        print("Distance is " + sortLists(file))