def game_core_v3(number: int = 1) -> int:
    """Сначала указываем возможный максимум и минимум, потом находим значение посередине. 
       Если загаданное значение больше предсказания, то приравниваем минимум к предсказанию, если больше - то приравниваем максимум к предсказанию, 
       таким образом сокращаем область поиска. Цикл повторяем, пока не найдем загаданное значение.
       Функция принимает загаданное число и возвращает число попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0
    min_num = 1
    max_num = 101

    while True:
        predict = (min_num + max_num) // 2
        count += 1
        if number == predict:
            break
        elif number > predict:
            min_num = predict     
        elif number < predict:
            max_num = predict

    # Ваш код заканчивается здесь

    return count
