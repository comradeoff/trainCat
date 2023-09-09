from load import *
from platformU import *
from calc_mass_center import *
from draw_platform_with_loads import *

load1 = Load(3650, 3320, 1500, 6670)
load2 = Load(3870, 2890, 1020, 4085)
load3 = Load(1080, 1580, 390, 395)
load4 = Load(3650, 3320, 1500, 6670)

loads = [
    (load1.length, load1.width, load1.height, load1.weight),
    (load2.length, load2.width, load2.height, load2.weight),
    (load3.length, load3.width, load3.height, load3.weight),
]

tcom = (transverse_centers_of_mass(loads))
lcom = (longitudinal_centers_of_mass(loads))

p = Platform(13400, 2870)

draw_platform_with_loads_2d(p.length, p.width, loads, tcom, lcom, 1000)