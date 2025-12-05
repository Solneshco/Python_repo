import math

def square(side):

    area = side * side 
    if isinstance(side, int):
        return area
   
    return math.ceil(area)

print(square(5))      # 25 (целое число)
print(square(3.2))    # 11 (3.2 * 3.2 = 10.24 → округляем вверх до 11)
print(square(7.8))    # 61 (7.8 * 7.8 = 60.84 → округляем вверх до 61)
print(square(4.0))    # 16 (4.0 * 4.0 = 16.0 → целое число)