def print_solution(filename):
    points = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            first_half = set(line[:len(line) // 2])
            second_half = set(line[len(line) // 2:])
            intersection = (set(first_half) & set(second_half)).pop()
            if intersection.isupper():
                points += 26
            points += ord(intersection.lower()) - 96
    print(points)


if __name__ == '__main__':
    print_solution('input.txt')

