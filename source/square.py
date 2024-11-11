def area(a: float) -> float:
    '''
    Вычисляет и возвращает площадь квадрата.
            Параметры:
                    a (float): длина стороны квадрата, вещественное число
            Возвращаемое значение:
                    s_area (float): площадь квадрата, вычесленная по формуле s_area = a ^ 2

            Пример вызова:
                Входные данные: 5.0
                Результат: 25.0
    '''
    if not isinstance(a, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")

    if a <= 0:
        raise ValueError("An invalid value was passed. Expected: a in the range (0, +infinity)")

    s_area = a * a
    return s_area


def perimeter(a: float) -> float:
    '''
    Вычисляет и возвращает периметр квадрата.
            Параметры:
                    a (float): длина стороны квадрата, вещественное число
            Возвращаемое значение:
                    s_perimeter (float): периметр квадрата, вычесленный по формуле s_perimeter = 4 * a

            Пример вызова:
                Входные данные: 5.0
                Результат: 20.0
    '''
    if not isinstance(a, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")

    if a <= 0:
        raise ValueError("An invalid value was passed. Expected: a in the range (0, +infinity)")
    
    s_perimeter = 4 * a
    return s_perimeter
