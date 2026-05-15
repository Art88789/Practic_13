from itertools import combinations


def get_k_element_subsets():
    """Получает список всех K‑элементных подмножеств для заданного множества."""
    numbers = list(map(int, input().split()))
    k = int(input())
    
    subsets = list(combinations(numbers, k))
    
    for subset in subsets:
        print(' '.join(map(str, subset)))

get_k_element_subsets()
