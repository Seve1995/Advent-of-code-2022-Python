def calc_points(opponent_hand, my_hand):
    dict_points = {'X': 1, 'Y': 2, 'Z': 3}
    dict_winning = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    dict_drawing = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    dict_losing = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    score = 0
    if my_hand == 'X':
        chosen_output = dict_losing[opponent_hand]
        score += 0 + dict_points[chosen_output]
    elif my_hand == 'Y':
        chosen_output = dict_drawing[opponent_hand]
        score += 3 + dict_points[chosen_output]
    else:
        chosen_output = dict_winning[opponent_hand]
        score += 6 + dict_points[chosen_output]
    return score


def print_solution(filename):
    points = 0
    with open('resources/' + filename) as f:
        for line in f:
            line = line.strip()
            opponent_hand, my_hand = line.split(' ')
            points += calc_points(opponent_hand, my_hand)
    print(points)


if __name__ == '__main__':
    print_solution('input.txt')

