import random

#
# я просто взял код сортирок из открытых источников (т.е. нагло скопировал)
#
class SortingMaster:

    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        arr = self.array[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.array[:]
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def insertion_sort(self):
        arr = self.array[:]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    