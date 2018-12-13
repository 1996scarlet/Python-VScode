def find_mid(a, b, c, d, e):
    if a < b:
        a, b = b, a
    if c < d:
        c, d, = d, c
    if a < c:
        a, c = c, a
        b, d = d, b
    if b < e:
        b, e = e,
    if b < c:
        b, c = c, b
        d, e = e, d
    if e < c:
        return c
    else:
        return e


def sort_five_in_seven_compare(a, b, c, d, e):
    if a < b:
        a, b = b, a
    if c < d:
        c, d, = d, c
    if a < c:
        a, c = c, a
        b, d = d, b
    if c < e:
        if a < e:
            if b < c:
                if b < d:
                    b, d = d, b
                a, d = d, a
                return a, b, c, d, e
            else:
                a, d = d, a
                b, c = c, b
                return a, b, c, d, e
        else:
            c, e = e, c
            d, e = e, d
    elif d < e:
        d, e = e, d

    if b < d:
        if b < e:
            b, e = e, b
        a, e = e, a
        c, d = d, c
    elif b < c:
        b, c = c, b
    else:
        a, e = e, a
        b, d = d, b

    return a, b, c, d, e


print(find_mid(6, 9, 2, 3, 5))
print(sort_five_in_seven_compare(7, 6, 9, 2, 4))
