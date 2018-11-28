# print(3 * 'a' 's' 'jkl')
# print(3 * 'a' + 's' 'jkl')

# nn = 25

# # print ('ss {}'.format(nn))

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# letters[2:5] = []

# print(letters)

# a, b = 0, 1
# while a < 1000:
#     # print(a, end=',')
#     a, b = b, a + b

# words = ['cat', 'window', 'defenestrate', 'window1', 'wind', 'window2']
# for w in words[:]:  # 循环遍历整个列表的切片副本。
#     if len(w) > 6:
#         words.remove(w)

# print(words)

# def f(a, L=[]):
#     L.append(a)
#     return L

# # def f(a, L=None):
# #     if L is None:
# #         L = []
# #     L.append(a)
# #     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def my_function():
#     '''ojbk

#     oplk
#     jkl
#     '''
#     pass

# print (my_function.__doc__)

# la = [0,1,2,3,4]

# print(la.pop(2))

# from collections import deque

# queue = deque(["Eric", "John", "Michael"])

# print (queue.popleft())
# print (queue.popleft())
# print (queue)

# martix = [
#     [0, 1, 2, 3],
#     [2, 2, 2, 2],
#     [3, 3, 4, 4],
# ]

# martix = [1, 2, 3]
# print(list(zip(martix*3)))
# print(list(zip(*[martix] * 3)))

# a = set('abracadabra')
# b = set('alacazam')

# print(a, b)
# print('a-b:', a - b)
# print('a|b:', a | b)
# print('a&b:', a & b)
# print('a^b:', a ^ b)

# dd = {x: x**2 for x in (2, 4, 6)}

# print(dd)

# dd = dict(sape=4139, guido=4127, jack=4098)

# print(dd)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

# import fibo

# fib = fibo.fib
# fib(1000)

# print (dir(fibo))

# year = 8102
# date = 11

# print(f'{year}--{date}')

# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')

# import json
# json.dump(x, f)
# x = json.load(f)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(2, 9.9)
print(x.r, x.i)
