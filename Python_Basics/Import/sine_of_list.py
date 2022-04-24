import math
from builtins import map

angles = map(lambda r: r * math.pi / 180, list(range(0, 91)))

print(list(map(math.sin, angles)))

to_pi_form = lambda r: r * math.pi / 180
angles = range(0, 91)

print(list(map(math.sin, map(to_pi_form, angles))))
