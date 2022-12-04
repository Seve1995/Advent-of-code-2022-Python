def print_solution(filename):
    points = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            first_pair, second_pair = line.split(',')
            start_1, end_1 = [int(x) for x in first_pair.split("-")]
            start_2, end_2 = [int(x) for x in second_pair.split("-")]
            if start_1 <= start_2:
                if start_2 <= end_1:
                    points += 1
            else:
                if start_1 <= end_2:
                    points += 1
    print(points)


if __name__ == '__main__':
    print_solution('input.txt')
