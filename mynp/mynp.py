# Created Date: Thursday, November 7th 2019, 9:58:46 pm
import numpy as np

# mode, sort,


class MyNp:
    def __init__(self):
        def say_hello(self):
            print("Hello!")

    @staticmethod
    def sum(arr: list) -> float:
        sum = 0
        for i in arr:
            sum += i
        return sum

    @staticmethod
    def mean(arr: list) -> float:
        sum = MyNp.sum(arr)
        mean = sum / len(arr)
        return mean

    @staticmethod
    def median(arr: list) -> float:
        arr_len = len(arr)
        div = arr_len % 2

        if arr_len % 2 == 0:
            return MyNp.mean([arr[div], arr[div + 1]])
        else:
            return arr[div]

    @staticmethod
    def deviation(arr: list) -> float:
        mean = MyNp.mean(arr)
        return [(i - mean) for i in arr]

    @staticmethod
    def var(arr: list) -> float:
        deviation = MyNp.deviation(arr)
        pow_dev_arr = [(i**2) for i in deviation]
        return MyNp.mean(sum(pow_dev_arr))
