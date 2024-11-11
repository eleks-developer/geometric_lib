import math


def area(r: float) -> float:
    '''
    Вычисляет и возвращает площадь круга.
            Параметры:
                    r (float): радиус круга, вещественное число
            Возвращаемое значение:
                    c_area (float): площадь круга, вычесленная по формуле c_area = pi * r ^ 2

            Пример вызова:
                Входные данные: 3.0
                Результат: 28.27433
    '''
    if not isinstance(r, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")
    
    if r <= 0:
        raise ValueError("An invalid value was passed. Expected: r in the range (0, +infinity)")

    c_area = math.pi * r * r
    return c_area


def perimeter(r: float) -> float:
    '''
    Вычисляет и возвращает периметр круга.
            Параметры:
                    r (float): радиус круга, вещественное число
            Возвращаемое значение:
                    c_perimeter (float): периметр круга, вычесленный по формуле c_perimeter = 2 * pi * r

            Пример вызова:
                Входные данные: 3.0
                Результат: 18.84955
    '''
    if not isinstance(r, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")
    
    if r <= 0:
        raise ValueError("An invalid value was passed. Expected: r in the range (0, +infinity)")
    
    c_perimeter = 2 * math.pi * r
    return c_perimeter
