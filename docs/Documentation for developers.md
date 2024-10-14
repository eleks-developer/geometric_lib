# Библиотека для работы с различными фигурами

## Общее описание

Библиотека, разработанная на языке **Python**, предназначена для работы с основными геометрическими фигурами. Она включает в себя **четыре основных файла**: circle.py, rectangle.py, square.py, triangle.py, в каждом из которых реализованы две функции: вычисление площади и периметра фигуры.

## Основные файлы библиотеки, их функции с примерами вызовов

### circle.py

#### Площадь окружности
Функция **принимает вещественное число** (*радиус окружности*) в качестве аргумента и **возвращает площадь окружности**, которая вычисляется по формуле:
```
S = πR²
```

```python
def area(r: float) -> float:
    c_area = math.pi * r * r
    return c_area
```

**Пример вызова:**
```python
area(3.0)
```

**Вывод:**
```
28.27433
```

#### Периметр окружности
Функция **принимает вещественное число** (*радиус окружности*) в качестве аргумента и **возвращает периметр окружности**, который вычисляется по формуле:
```
P = 2πR
```

```python
def perimeter(r: float) -> float:
    c_perimeter = 2 * math.pi * r
    return c_perimeter
```

**Пример вызова:**
```python
perimeter(3.0)
```

**Вывод:**
```
18.84955
```

### rectangle.py

#### Площадь прямоугольника
Функция **принимает вещественные числа** (*стороны прямоугольника*) в качестве аргументов и **возвращает площадь прямоугольника**, которая вычисляется по формуле:
```
S = ab
```

```python
def area(a: float, b: float) -> float:
    r_area = a * b
    return r_area
```

**Пример вызова:**
```python
area(3.0, 5.0)
```

**Вывод:**
```
15.0
```

#### Периметр прямоугольника
Функция **принимает вещественные числа** (*стороны прямоугольника*) в качестве аргументов и **возвращает периметр прямоугольника**, который вычисляется по формуле:
```
P = 2a + 2b
```

```python
def perimeter(a: float, b: float) -> float:
    r_perimeter = (a + b) * 2
    return r_perimeter
```

**Пример вызова:**
```python
perimeter(3.0, 5.0)
```

**Вывод:**
```
16.0
```

### square.py

#### Площадь квадрата
Функция **принимает вещественное число** (*сторона квадрата*) в качестве аргумента и **возвращает площадь квадрата**, которая вычисляется по формуле:
```
S = a²
```

```python
def area(a: float) -> float:
    s_area = a * a
    return s_area
```

**Пример вызова:**
```python
area(5.0)
```

**Вывод:**
```
25.0
```

#### Периметр квадрата
Функция **принимает вещественное число** (*сторона квадрата*) в качестве аргумента и **возвращает периметр квадрата**, который вычисляется по формуле:
```
P = 4a
```

```python
def perimeter(a: float) -> float:
    s_perimeter = 4 * a
    return s_perimeter
```

**Пример вызова:**
```python
perimeter(5.0)
```

**Вывод:**
```
20.0
```

### triangle.py

#### Площадь треугольника
Функция **принимает вещественные числа** (*сторона треугольника и высота, падающая на эту сторону*) в качестве аргументов и **возвращает площадь треугольника**, которая вычисляется по формуле:
```
S = ah/2
```

```python
def area(a: float, h: float) -> float:
    t_area = a * h / 2
    return t_area
```

**Пример вызова:**
```python
area(4.0, 6.0)
```

**Вывод:**
```
12.0
```

#### Периметр треугольника
Функция **принимает вещественные числа** (*стороны треугольника*) в качестве аргументов, проверяет треугольник на существование:
```
a + b > c
a + c > b
b + c > a
```

и **возвращает периметр треугольника**, который вычисляется по формуле:
```
P = a + b + c
```

```python
def perimeter(a: float, b: float, c: float) -> float:
    
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return -1.0

    t_perimeter = a + b + c
    return t_perimeter
```

**Примеры вызова:**
```python
perimeter(3.0, 4.0, 5.0)
```

```python
perimeter(100.0, 3.0, 5.0)
```

**Выводы:**
```
12.0
```

```
-1.0
```

## История изменений проекта

* **31dead1** - *Added documentation for file functions **rectangle.py**, and also added a check for the existence of a triangle to the **'perimeter'** function*
* **13fe350** - *Added documentation for file functions **rectangle.py***
* **bb1b73e** - *Documented the functions in a file **square.py**. I made a cosmetic edit **circle.py***
* **7992220** - *Added an example of calling each function of the file **circle.py***
* **6981648** - *Added documentation for file functions **circle.py**, and also slightly changed the functions themselves*
* **86b0e77** - *Fixed an error in the formula of the **'perimeter'** function in the file **rectangle.py** and added new **triangle.py** file*
* **2954fc3** - *Create a new **rectangle.py** file and make a cosmetic correction of the **circle.py** and **square.py** files*
* **d078c8d** - *L-03: Docs added*
* **8ba9aeb** - *L-03: Circle and square added*
