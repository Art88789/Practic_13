from itertools import permutations


def get_lexicographic_permutations():
    """Получает все перестановки множества чисел в лексикографическом порядке."""
    numbers = sorted(map(int, input().split()))
    perms = permutations(numbers)

    for perm in perms:
        print(' '.join(map(str, perm)))

get_lexicographic_permutations()
