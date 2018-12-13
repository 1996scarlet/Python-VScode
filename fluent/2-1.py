# a, b, *rest = range(5)
# print(a, b, rest)
# a, b, *rest = range(3)
# print(a, b, rest)
# a, b, *rest = range(2)
# print(a, b, rest)

# a, b, *rest, c, d = range(10)
# print(a, b, rest, c, d)

fmt = '{:15} | {:9.4f} | {:9.4f}'

# print(fmt.format(0.33,9856.25565,2356.2))

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)

s = 'bicycle'
print(s[::3], s[::-1], s[::-2])
