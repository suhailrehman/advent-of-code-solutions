
def sum_numbers(lines):
    """
    Solves AoC 2023 day 1 challenge
    """

    digits = [str(x) for x in range(0,10)]
    total = 0

    for line in lines:
        first = None
        last = None
        for char in line:
            if char in digits:
                if not first:
                    first = char
                last = char
        print(line, first, last)
        total = total + int(first+last)
    return total


if __name__ == '__main__':
    input_lines = []
    with open('input.txt') as f:
        for line in f:
            input_lines.append(line.strip())
    print(sum_numbers(input_lines))