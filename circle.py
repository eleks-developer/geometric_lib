import math


def area(r: float) -> float:
    '''
    Вычисляет и возвращает площадь круга.
            Параметры:
                    r (float): радиус круга, вещественное число
            Возвращаемое значение:
                    c_area (float): площадь круга, вычесленная по формуле c_area = pi * r ^ 2
    '''
    c_area = math.pi * r * r
    return c_area


def perimeter(r: float) -> float:
    '''
    Вычисляет и возвращает периметр круга.
            Параметры:
                    r (float): радиус круга, вещественное число
            Возвращаемое значение:
                    c_perimeter (float): периметр круга, вычесленный по формуле c_perimeter = 2 * pi * r
    '''
    c_perimeter = 2 * math.pi * r
    return c_perimeter
