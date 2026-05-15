from itertools import combinations

def get_all_subsets():
    """Получает список всех подмножеств для заданного множества чисел."""
    numbers = list(map(int, input().split()))
    subsets = []

    for r in range(len(numbers) + 1):
        for subset in combinations(numbers, r):
            subsets.append(list(subset))

    return subsets

all_subsets = get_all_subsets()
for subset in all_subsets:
    print(' '.join(map(str, subset)))
