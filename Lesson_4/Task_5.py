from random import randint

def create_coeffs(num: int) -> list:
    return [randint(1, 100) for _ in range(num + 1)]


def create_str(list_coeff: list) -> str:
    lenght = len(list_coeff)
    lst_str = [f"{el}*x^{lenght - idx - 1}" for idx, el in enumerate(list_coeff)]
    return " + ".join(lst_str)


def write_to_file(polynom_string: str, filename: str) -> None:
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(polynom_string)

def write_to_db(....):
    pass

write_to_file(create_str(create_coeffs(10)), "test.txt")
