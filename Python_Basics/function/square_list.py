def mapper(lox, fn_x):
    lofn_x = []
    for x in lox:
        lofn_x.append(fn_x(x))
    return lofn_x


square = lambda num: num**2

lon = [1, 2, 3, 4, 5, 6, 7, 8, 9]

losq = mapper(lon, square)
print(lon)
print(losq)

c_to_f = lambda c: 1.8 * c + 32
lot_c = [20, 25, 30, 35, -40]
lot_f = mapper(lot_c, c_to_f)
print(lot_c)
print(lot_f)

str_of_hot = []
hot_or_not = lambda x: str_of_hot.append(x) if x >= 37 else "no"
c = [20, 37, 12, 39, 40, 29]
f = mapper(c, hot_or_not)
print(f)
print(str_of_hot)

def filterer(lox, fn_x_b):
    lox_filtered = []
    for x in lox:
        if x in lox:
            lox_filtered.append(x)
    return lox_filtered


above_body_temp = lambda t_c: t_c > 36
temp_readings = [20, 30, 25, 35, 40, 45]
temp_filtered = filterer(temp_readings, above_body_temp)
print(temp_readings)
print(temp_filtered)

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = [1, 1, 1, 1, 1]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))           #adds three list
