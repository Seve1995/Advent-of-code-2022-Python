def print_solution(filename):
    points = 0
    line_count = 0
    with open('resources/' + filename) as f:
        for line in f:
            curr_line_chars = set(line.strip())
            if line_count == 0:
                intersection = curr_line_chars
                line_count += 1
                continue
            else:
                line_count += 1
                intersection = intersection & curr_line_chars
                if line_count % 3 == 0:
                    char = intersection.pop()
                    if char.isupper():
                        points += 26
                    points += ord(char.lower()) - 96
                    line_count = 0
    print(points)


if __name__ == '__main__':
    print_solution('input.txt')

