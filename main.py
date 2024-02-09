from input import input_string


def parse_input(string):
    reports = []
    for line in string.split('\n'):
        key, values = line.split()

        values = list(map(int, values.split(',')))
        reports.append((key, values))
    return reports


cache = {}


def get_variation_sum(line, pattern):
    if line == '':
        return 1 if pattern == () else 0
    if not pattern:
        return 0 if '#' in line else 1

    key = (line, pattern)
    if key in cache:
        return cache[key]

    combinations = 0

    if line[0] in '.?':
        combinations += get_variation_sum(line[1:], pattern)

    if line[0] in '#?':
        if len(line) >= pattern[0] and '.' not in line[:pattern[0]] and (
                len(line) == pattern[0] or line[pattern[0]] != '#'):
            combinations += get_variation_sum(line[pattern[0] + 1:], pattern[1:])

    cache[key] = combinations
    return combinations


if __name__ == '__main__':
    comb_sum = 0
    for l, p in parse_input(input_string):
        comb_sum += get_variation_sum('?'.join([l] * 5), tuple(p) * 5)

    print(comb_sum)
