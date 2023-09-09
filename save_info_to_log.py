def save_info_to_log (data, filename="log.txt"):
    """
    Данная функция  позволяет сохранить данные о грузе и платформе в отдельный файл.
    
    Аргументы:
        data (list): список строчных данных, которые будут загружены в файл.
        filename (string): строка, обозначающая название файла, который будет создан, в который будет сохранена вся информация.
    """
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"Вся информация сохранена в файл: {filename}.")
    except Exception as e:
        print(f"При записи файла произошла ошибка: {str(e)}.")