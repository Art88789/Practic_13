def check_repeated_number():
    """Проверяет, встречается ли введенное число в списке более одного раза."""
    numbers = list(map(int, input().split()))
    target = int(input())

    return numbers.count(target) > 1


if check_repeated_number():
    print("YES")
else:
    print("NO")
