def print_solution(filename):
    output = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            x = 0
            distinct_chars_len = 14
            while x < len(line) - distinct_chars_len:
                currSubstring = set(line[x:(distinct_chars_len + x)])
                if len(currSubstring) == distinct_chars_len:
                    output = x + distinct_chars_len
                    break
                x += 1
    print(output)


if __name__ == '__main__':
    print_solution('input.txt')
