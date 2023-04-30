from random import randint
def array(size: int, min: int, max: int) -> list:
    """Генерация одномерного массива размером size от min до max"""
    massiv = [randint(min, max) for _ in range(size)]
    return massiv
