def generate_input_stacks(filename):
    input_stacks = []
    for i in range(0, 9):
        input_stacks.append([])
    with open(filename) as f:
        for line in f:
            if line[1:2] == '1':
                break
            for x in range(0, 9):
                curr_letter = line[1 + (x * 4):2 + (x * 4)]
                if curr_letter != ' ':
                    input_stacks[x].insert(0, (line[1 + (x * 4):2 + (x * 4)]))
    return input_stacks


def print_solution(filename):
    output = ''
    input_stacks = generate_input_stacks(filename)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line[:1] == 'm':
                split_line = line.split(' ')
                crates_to_move = int(split_line[1])
                source_stack = int(split_line[3]) - 1
                destination_stack = int(split_line[5]) - 1
                for x in range(0, crates_to_move):
                    input_stacks[destination_stack].append(input_stacks[source_stack].pop())
    for i in range(len(input_stacks)):
        output += input_stacks[i].pop()
    print(output)


if __name__ == '__main__':
    print_solution('input.txt')
