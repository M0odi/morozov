from task import binary_search

def test():
    numbers1 = list(range(1, 10))
    target1 = 5
    assert binary_search(numbers1, target1) == 4
    assert binary_search(numbers1, 1000) == -1

    numbers2 = list(range(1, 100))
    target2 = 99
    assert binary_search(numbers2, target2) == 98
    assert binary_search(numbers2, 1000) == -1

test()