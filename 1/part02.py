list1, list2 = [], []

def sortLists(input):
    for line in input.readlines():
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

    list1.sort()
    list2.sort()

    return(str(calcSimilarity(list1, list2)))

def calcSimilarity(l1, l2):
    similarity = 0
    counter = 0

    for i in l1:
        for j in l2:
            if i == j:
                counter = counter + 1
        
        similarity = similarity + (i * counter)
        counter = 0

    return similarity


if __name__ == "__main__":
    with open('./input') as file:
        print("Similarity is " + sortLists(file))