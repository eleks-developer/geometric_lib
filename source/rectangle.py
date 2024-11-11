def area(a: float, b: float) -> float:
    '''
    Вычисляет и возвращает площадь прямоугольника.
            Параметры:
                    a (float): ширина прямоугольника, вещественное число
                    b (float): длина прямоугольника, вещественное число
            Возвращаемое значение:
                    r_area (float): площадь прямоугольника, вычесленная по формуле r_area = a * b

            Пример вызова:
                Входные данные: 3.0, 5.0 
                Результат: 15.0
    '''
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")
    
    if a <= 0 or b <= 0:
        raise ValueError("An invalid value was passed. Expected: a, b in the range (0, +infinity)")

    r_area = a * b
    return r_area


def perimeter(a: float, b: float) -> float:
    '''
    Вычисляет и возвращает периметр прямоугольника.
            Параметры:
                    a (float): ширина прямоугольника, вещественное число
                    b (float): длина прямоугольника, вещественное число
            Возвращаемое значение:
                    r_perimeter (float): периметр прямоугольника, вычесленный по формуле r_perimeter = (a + b) * 2

            Пример вызова:
                Входные данные: 3.0, 5.0 
                Результат: 16.0
    '''
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise ValueError("An invalid type was passed. Expected: float / int")

    if a <= 0 or b <= 0:
        raise ValueError("An invalid value was passed. Expected: a, b in the range (0, +infinity)")

    r_perimeter = (a + b) * 2
    return r_perimeter
