import matplotlib.pyplot as plt
from save_info_to_log import *

def draw_platform_with_loads_2d(
    platform_length, platform_width, loads, transverse_coms, longitudinal_coms, load_distance, output_filename="platform_with_loads.png"
):
    """
    Эта функция предназначена для создания визуального представления платформы с размещенными на ней грузами. Он использует Matplotlib 
    для построения графиков и принимает входные данные, такие как размеры платформы, свойства нагрузки и их центры масс. 
    Функция выполняет итерацию по списку грузов, рисует прямоугольники для их представления и помечает каждый груз его поперечным и 
    продольным центрами масс. Наконец, он отображает график и сохраняет его в файл.

    Аргументы:
        platform_length (float): Длина платформы.
        platform_width (float): ширина платформы.
        loads (список): список кортежей, каждый из которых содержит (load_length, load_width, load_height, load_weight).
        transverse_com (список): Список поперечных центров масс для каждого груза.
        longitudinal_com (список): Список продольных значений центра масс для каждого груза.
        load_distance (integer): Расстояние между грузами.
        output_filename (строка): Имя файла для сохранения изображения.

    Результат:
        Нет (отображает диаграмму с помощью matplotlib и сохраняет ее в файл)...
    """
    # Создание фигуры и осей
    fig, ax = plt.subplots()

    # Отрисовка груза
    ax.add_patch(plt.Rectangle((0, 0), platform_length, platform_width, color="lightblue"))

    # Инициализирование переменных для размещения грузов и их номеров
    current_x = 0
    current_y = 0
    load_number = 1

    # Списки для хранения информации о загрузке для отображения под диаграммой
    load_info = []
    load_info.append(f"Платформа: длина={platform_length}, ширина={platform_width}.")

    for i, (load_length, load_width, load_height, load_weight) in enumerate(loads):
        if current_x + load_length > platform_length:
        #Если груз превышает границу платформы по горизонтали, переходите к следующему ряду
            current_x = 0

        # Регулируем положение груза
        load_y = (platform_width - load_width) / 2

        # Отрисовка груза
        ax.add_patch(
            plt.Rectangle(
                (current_x, load_y),
                load_length,
                load_width,
                color="gray",
                edgecolor="black",
                lw=2,
                fill=False,
            )
        )

        # Отображение номера груза на самом грузе
        number_label = f"Груз №{load_number}"
        number_x = current_x + load_length * 0.5
        number_y = load_y + load_width * 0.5

        ax.text(
            number_x,
            number_y,
            number_label,
            fontsize=8,
            color="black",
            ha="center",
            va="center",
            weight='bold',
        )

        # Сохранение информацию о грузе для отображения под диаграммой
        load_info.append(
            f"Груз {load_number}: Длина={load_length}, Ширина={load_width}, Высота={load_height}, Вес={load_weight},Поперечный Ц.М.={transverse_coms[i]:.2f}, Продольный Ц.М.={longitudinal_coms[i]:.2f}"
        )

        # Обновление номера груза и текущего положения для следующего груза
        load_number += 1
        current_x += load_length + load_distance

    # Отображение информации о грузе под диаграммой
    # load_info_str = "\n".join(load_info)
    # plt.text(
    #     platform_length * 0.1,
    #     -platform_width * 0.15,
    #     load_info_str,
    #     fontsize=8,
    #     color="black",
    # )

    ax.set_xlim(-0.1 * platform_length, 1.1 * platform_length)
    ax.set_ylim(-0.1 * platform_width, 1.3 * platform_width)
    ax.set_xlabel("Ось-X (мм)")
    ax.set_ylabel("Ось-Y (мм)")

    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid()
    plt.title("Платформа с грузами")

    # plt.savefig(output_filename, bbox_inches="tight")
    plt.show() 
    
    save_info_to_log(load_info)