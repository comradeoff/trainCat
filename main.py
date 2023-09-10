from load import *
from platformU import *
from calc_mass_center import *
from draw_platform_with_loads import *

loads = []

length1 = int(input("Введите длину груза: "))
width1 = int(input("Введите ширину груза: "))
height1 = int(input("Введите высоту груза: "))
weight1 = int(input("Введите вес груза: "))

load1 = Load(length1, width1, height1, weight1)

answ = input("Хотите ли вы добавить ещё один груз?(y/n): ")
if answ == "y":
    length2 = int(input("Введите длину второго груза: "))
    width2 = int(input("Введите ширину второго груза: "))
    height2 = int(input("Введите высоту второго груза: "))
    weight2 = int(input("Введите вес второго груза: "))
    
    load2 = Load(length2, width2, height2, weight2)
    
    loads = [
    (load1.length, load1.width, load1.height, load1.weight),
    (load2.length, load2.width, load2.height, load2.weight),
    ]
else:
    loads = [
    (load1.length, load1.width, load1.height, load1.weight),
    ]



tcom = (transverse_centers_of_mass(loads))
lcom = (longitudinal_centers_of_mass(loads))

p = Platform(13400, 2870)

draw_platform_with_loads_2d(p.length, p.width, loads, tcom, lcom, 1000)