def merge_lists(listA, listB):
    listAB = []
    a = 0
    b = 0
    for i in range(0, (len(listA)+len(listB))):
        if a >= len(listA):
            listAB.append(listB[b])
            b+=1
        elif b >= len(listB):
            listAB.append(listA[a])
            a+=1
        else:
            if listA[a] < listB[b]:
                listAB.append(listA[a])
                a+=1
            else:
                listAB.append(listB[b])
                b+=1
    return listAB

def testMerge():
    listA1 = []
    listB1 = [1, 2]
    expected1 = [1, 2]
    assert expected1 == merge_lists(listA1, listB1)

    listA2 = [1, 2]
    listB2 = []
    expected2 = [1, 2]
    assert expected2 == merge_lists(listA2, listB2)

    listA3 = [1, 2, 3]
    listB3 = [1, 2, 3]
    expected3 = [1, 1, 2, 2, 3, 3]
    assert expected3 == merge_lists(listA3, listB3)

    listA4 = [2, 3, 4]
    listB4 = [1, 2, 3]
    expected4 = [1, 2, 2, 3, 3, 4]
    assert expected4 == merge_lists(listA4, listB4)

    listA5 = [1, 2, 3]
    listB5 = [2, 3, 4]
    expected5 = [1, 2, 2, 3, 3, 4]
    assert expected5 == merge_lists(listA5, listB5)


def main():
    listA = [1, 2]
    listB = [2, 3]
    testMerge()
    pass

if __name__ == '__main__':
    main()