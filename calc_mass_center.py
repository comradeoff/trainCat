def transverse_centers_of_mass(objects):
    """
    Вычисление поперечного центра масс для списка объектов, где каждый объект представлен в виде кортежа: длина, ширина, высота, вес.
    Вы можете использовать эту функцию, предоставив список объектов, где каждый объект представлен в виде кортежа, содержащего длину, 
    ширину, высоту и вес. Функция вычислит поперечный центр масс для каждого объекта и вернет набор их центров масс в том же порядке, 
    в каком они отображаются в списке.

    Аргументы:
        objects (list): список объектов, где каждый объект представлен в виде кортежа (длина, ширина, высота, вес).

    Результат:
        кортеж, содержащий поперечные центры масс для каждого объекта в том же порядке, в каком они отображаются в списке.
    """
    total_mass = sum(obj[3] for obj in objects)  # Вычисление общей массы всех объектов.
    if total_mass <= 0:
        raise ValueError("Общий вес объектов должен быть больше нуля.")

    centers_of_mass = []  # Инициализация списка для хранения центров масс.

    for obj in objects:
        length, width, height, weight = obj
        transverse_com = (length * weight) / (2 * (length + width + height))
        centers_of_mass.append(transverse_com)

    return tuple(centers_of_mass)


def longitudinal_centers_of_mass(objects):
    """
    Вычисление продольного центра масс для списка объектов, где каждый объект представлен в виде кортежа: длина, ширина, рост, вес.
    Эта функция аналогична предыдущей, но вычисляет продольный центр масс для каждого объекта в списке на основе их длины, ширины, 
    высоты и веса. Он возвращает набор их продольных центров масс в том же порядке, в каком они отображаются в списке.

    Аргументы:
        objects (list): список объектов, где каждый объект представлен в виде кортежа (длина, ширина, высота, вес).

    Результат:
        кортеж, содержащий продольный центр масс для каждого объекта в том же порядке, в каком они отображаются в списке.
    """
    total_mass = sum(obj[3] for obj in objects)  # Calculate the total mass of all objects
    if total_mass <= 0:
        raise ValueError("Total weight of objects must be greater than zero.")

    centers_of_mass = []  # Initialize a list to store centers of mass

    for obj in objects:
        length, width, height, weight = obj
        longitudinal_com = (width  * weight) / (2 * (length + width + height))
        centers_of_mass.append(longitudinal_com)

    return tuple(centers_of_mass)