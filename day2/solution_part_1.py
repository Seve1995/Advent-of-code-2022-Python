def calc_points(opponent_hand, my_hand):
    dict_points = {'X': 1, 'Y': 2, 'Z': 3}
    dict_winning = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    dict_drawing = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    score = 0 + dict_points[my_hand]
    if my_hand == dict_drawing[opponent_hand]:
        score += 3
    elif my_hand == dict_winning[opponent_hand]:
        score += 6
    else:
        score += 0
    return score


def print_solution(filename):
    points = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            opponent_hand, my_hand = line.split(' ')
            points += calc_points(opponent_hand, my_hand)
    print(points)


if __name__ == '__main__':
    print_solution('input.txt')
