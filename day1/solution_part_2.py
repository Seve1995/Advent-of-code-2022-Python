import heapq


def print_solution(filename):
    curr_sum = 0
    h = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                curr_sum += int(line)
            else:
                heapq.heappush(h, curr_sum)
                curr_sum = 0
    print(sum(heapq.nlargest(3, h)))


if __name__ == '__main__':
    print_solution('input.txt')

