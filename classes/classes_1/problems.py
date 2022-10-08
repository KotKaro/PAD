from typing import List

def check_range(value: int, start: int, stop: int) -> str:
    return "%s %s jest miedzy %s a %s" % (value, "" if start <= value <= stop else "NIE", start, stop)


def bool_range(value: int, start: int, stop: int) -> bool:
    return start <= value <= stop


def unique_list(elements: List[int]) -> List[int]:
    result = []
    for value in elements:
        if value not in result:
            result.append(value)
    return result


my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
my_list = list(set(my_list))


def volume_of_sphere(radius: int) -> float:
    pi_value = 3.14
    return round(pi_value * (radius ** 2), 2)


def num_fact(to: int) -> int:
    result = 1
    for value in range(1, to + 1):
        result *= value
    return result
