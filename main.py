from itertools import permutations, combinations
from input import input_string


def parse_input(string):
    reports = []
    for line in string.split('\n'):
        key, values = line.split()

        values = list(map(int, values.split(',')))
        reports.append((key, values))
    return reports


def fill_chars(string, chars):
    return string.replace('?', '{}').format(*chars)


def check_pattern(string, pattern):
    counts = [len(group) for group in string.split('.') if '#' in group]
    return counts == pattern


def get_variations_count(data):
    secret_slots = data[0].count('?')
    required_hashes = sum(data[1]) - data[0].count('#')
    pattern = required_hashes * '#' + (secret_slots - required_hashes) * '.'
    permutations_set = set(permutations(pattern))

    counter = 0
    for perm in permutations_set:
        if check_pattern(fill_chars(data[0], perm), data[1]):
            counter += 1

    return counter


def get_variation_sum(input_string):
    variation_sums = 0
    for i, data in enumerate(parse_input(input_string)):
        variation_sums += get_variations_count(data)
        print(f"Data set {i}: Variations count is {get_variations_count(data)}")
    print(f"Total variations sum: {variation_sums}")


if __name__ == '__main__':
    get_variation_sum(input_string)
