def check_repeated_number():
    numbers = list(map(int, input().split()))
    target = int(input())
    
    # Считаем количество вхождений target напрямую
    return numbers.count(target) > 1

if check_repeated_number():
    print("YES")
else:
    print("NO")

