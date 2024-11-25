from task import *

def test():
    
    numbers1 = [0, 5, 9, 2, 1]
    master1 = SortingMaster(numbers1)
    assert master1.bubble_sort() == [0, 1, 2, 5, 9]

    numbers2 = [0, 5, 9, 2, 1]
    master2 = SortingMaster(numbers2)
    assert master2.quick_sort() == [0, 1, 2, 5, 9]

    numbers3 = [0, 5, 9, 2, 1]
    master3 = SortingMaster(numbers3)
    assert master3.insertion_sort() == [0, 1, 2, 5, 9]


test()