import random
import keyboard


def roll_dices(amount):
    print("Rolling the dices...")
    result = list()
    for n in range(0, amount):
        result.append(random.randint(1, 6))
    result.sort()
    return result


def count_points(dices_list):
    counted_points = 0
    counts = [1, 2, 3, 4, 5, 6]
    for n in range(0, 6):
        counts[n] = dices_list.count(n + 1)
    return counted_points


def display_dices(not_selected_dices, selected_dices):
    print("available dices:")
    for n in range(0, len(not_selected_dices)):
        print(str(chr(97 + n)) + ": [" + str(not_selected_dices[n]) + "]")
    if len(selected_dices) > 0:
        print("counted dices:")
    for n in range(0, len(selected_dices)):
        print("[" + str(not_selected_dices[n]) + "]")


def user_choices(_available_dices, _counted_dices):
    _round_over = False
    _waiting_for_input = True
    while _waiting_for_input:
        if keyboard.read_key() == "space":
            _round_over = True
            _waiting_for_input = False
        letter = ["a", "b", "c", "d", "e", "f"]
        for i in range(0, len(letter)):
            if keyboard.read_key() == letter[i]:
                _counted_dices.append(_available_dices[i])
                _available_dices.pop(i)
                _waiting_for_input = False

    return _available_dices, _counted_dices, _round_over

# test

winning_score = 10000
score = 0
game_over = False
# game loop
while not game_over:
    dices = roll_dices(6)
    round_over = False
    counted_dices = list()
    while not round_over:
        display_dices(dices, counted_dices)
        dices, counted_dices, round_over = user_choices(dices, counted_dices)
    
    
    if score >= winning_score:
        game_over = True
