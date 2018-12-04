import math


def Simplify_Max_of_Domino(L, R, first, last):
    if last - first == 1:
        return R[first] * L[last]
    else:
        mid = math.ceil((first + last) / 2)

        if (L[mid] < R[mid]):
            L[mid], R[mid] = R[mid], L[mid]

        Max1 = Simplify_Max_of_Domino(
            L, R, first, mid) + Simplify_Max_of_Domino(L, R, mid, last)

        L[mid], R[mid] = R[mid], L[mid]

        Max0 = Simplify_Max_of_Domino(
            L, R, first, mid) + Simplify_Max_of_Domino(L, R, mid, last)

        if Max1 > Max0:
            return Max1
        else:
            global W
            W[mid] = 0
            return Max0

        # return max(Max1, Max0)


def Max_of_Domino(L, R, first, last):
    Max = -1
    if last - first > 0:
        Max = Simplify_Max_of_Domino(L, R, first, last)

    return Max


W = [1, 1, 1, 1, 1, 1, 1, 1]
L = [0, 5, 4, 9, 7, 3, 11, 0]
R = [0, 8, 2, 6, 7, 9, 10, 0]

print(Max_of_Domino(L, R, 0, 7))
print(W)
