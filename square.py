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
    
    s_perimeter = 4 * a
    return s_perimeter
