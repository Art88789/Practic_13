def check_in_intersection():
    """Определяет, принадлежит ли значение пересечению двух множеств."""
    set1 = set(input().split())
    set2 = set(input().split())
    target = input()
    intersection = set1 & set2
    return target in intersection

print("YES" if check_in_intersection() else "NO")

