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

def merge_sort(listA):
    if len(listA)>1:
        mid = len(listA) // 2
        half1 = listA[mid:]
        half2 = listA[:mid]
        sortedHalf1 = merge_sort(half1)
        sortedHalf2 = merge_sort(half2)
        return merge_lists(sortedHalf1, sortedHalf2)
    else:
        return listA




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

def test_sort():
    list1 = [1, 5, 4, 3]
    expected1 = [1, 3, 4, 5]
    assert expected1 == merge_sort(list1)

    list2 = [1]
    expected2 = [1]
    assert expected2 == merge_sort(list2)

    list3 = [1, 1, 1]
    expected3 = [1, 1, 1]
    assert expected3 == merge_sort(list3)

def main():
    listA = [1, 2]
    listB = [2, 3]
    testMerge()
    print(merge_sort([4, 3, 2, 5]))
    test_sort()
    pass

if __name__ == '__main__':
    main()