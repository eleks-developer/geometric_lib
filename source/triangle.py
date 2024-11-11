def area(a: float, h: float) -> float:
    '''
    Вычисляет и возвращает площадь треугольника.
            Параметры:
                    a (float): сторона треугольника, вещественное число
                    h (float): высота треугольника, падающая на сторону a, вещественное число
            Возвращаемое значение:
                    t_area (float): площадь треугольника, вычесленная по формуле t_area = a * h / 2

            Пример вызова:
                Входные данные: 4.0, 6.0
                Результат: 12.0
    '''
    if not isinstance(a, (float, int)) or not isinstance(h, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")

    if a <= 0 or h <= 0:
        raise ValueError("An invalid value was passed. Expected: a, h in the range (0, +infinity)")

    t_area = a * h / 2 
    return t_area


def perimeter(a: float, b: float, c: float) -> float:
    '''
    Проверяет существование треугольника, вычисляет и возвращает его периметр.
            Параметры:
                    a (float): 1 сторона треугольника, вещественное число
                    b (float): 2 сторона треугольника, вещественное число
                    c (float): 3 сторона треугольника, вещественное число
            Возвращаемое значение:
                    t_perimeter (float): периметр треугольника, вычесленный по формуле t_perimeter = a + b + c

            Пример вызова 1:
                Входные данные: 3.0, 4.0, 5.0
                Результат: 12.0

            Пример вызова 2:
                Входные данные: 100.0, 3.0, 5.0
                Результат: -1.0
    '''
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)) or not isinstance(c, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("An invalid value was passed. Expected: a, b, c in the range (0, +infinity)")

    if (a + b) <= c or (a + c) <= b or (b + c) <= a or c**2 != (a**2 + b**2):
        return -1.0

    t_perimeter = a + b + c 
    return t_perimeter
