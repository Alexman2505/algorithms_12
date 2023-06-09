def sum_of_m_numbers(m, n):
    numbers = (0, 1)  # Инициализируем кортеж с первыми двумя числами (0 и 1)
    for _ in range(2, n):
        next_number = sum(
            numbers[-m:]
        )  # Суммируем последние m чисел в кортеже
        numbers += (next_number,)  # Добавляем сумму в кортеж
    return numbers


if __name__ == "__main__":
    n = int(input("Введите число n: "))
    m = int(input("Введите число m, 0 < m < n: "))
    result = sum_of_m_numbers(m, n)
    print(*result, sep=", ")
