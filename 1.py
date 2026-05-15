def check_repeated_number():
    """Проверяет, принадлежит ли заданное число множеству повторяющихся чисел в последовательности."""
    numbers = list(map(int, input().split()))
    target = int(input())

    # Считаем, сколько раз встречается каждое число
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Находим все числа, которые встречаются больше одного раза
    repeated = set()
    for num, count in counts.items():
        if count > 1:
            repeated.add(num)

    return target in repeated


if check_repeated_number():
    print("YES")
else:
    print("NO")
