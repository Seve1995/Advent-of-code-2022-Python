def print_solution(filename):
    max_sum = 0
    curr_sum = 0
    with open(filename) as f:
        for line in f:
            if line.strip():
                curr_sum += int(line)
            else:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                curr_sum = 0
    print(max_sum)


if __name__ == '__main__':
    print_solution('input.txt')

