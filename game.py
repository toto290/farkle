import random
# import keyboard


def roll_dices(amount):
    print("Rolling the dices...")
    result = list()
    for n in range(0, amount):
        result.append(random.randint(1, 6))
    result.sort()
    return result


def calculate_points(_dices_list):
    _points_per_eye = list()
    _eyes_counted = list()
    for _eye in range(1, 7):
        _eye_count = _dices_list.count(_eye)
        _eyes_counted.append(_eye_count)
        _triple_count = (_eye_count // 3)
        _single_count = _eye_count - _triple_count

        _eye_points = 0
        # triple-eyes
        _eye_points += _triple_count * _eye * 100 if _eye > 1 else _triple_count * _eye * 1000
        # eye is 1
        if _eye == 1 and _single_count > 0:
            _eye_points += _single_count * 100
        # eye is 5
        elif _eye == 5 and _single_count > 0:
            _eye_points += _single_count * 50
        _points_per_eye.append(_eye_points)

    return _eyes_counted, _points_per_eye


def display_dices(not_selected_dices, selected_dices):
    print("available dices:")
    for n in range(0, len(not_selected_dices)):
        print(str(chr(97 + n)) + ": [" + str(not_selected_dices[n]) + "]")
    if len(selected_dices) > 0:
        print("counted dices:")
    for n in range(0, len(selected_dices)):
        print("[" + str(not_selected_dices[n]) + "]")


def display_points(_eyes_counted, _eyes_points):
    _sum = 0
    for i in range(0, 6):
        eye = i + 1
        if _eyes_counted[i] > 0:
            print(str(_eyes_counted[i]) + "x[" + str(eye) + "] = " + str(_eyes_points[i]))
            _sum += _eyes_points[i]
    print("total score = " + str(_sum))


# def user_choices(_available_dices, _counted_dices):
#     _round_over = False
#     _waiting_for_input = True
#     while _waiting_for_input:
#         if keyboard.read_key() == "space":
#             _round_over = True
#             _waiting_for_input = False
#         letter = ["a", "b", "c", "d", "e", "f"]
#         for i in range(0, len(letter)):
#             if keyboard.read_key() == letter[i]:
#                 _counted_dices.append(_available_dices[i])
#                 _available_dices.pop(i)
#                 _waiting_for_input = False
#
#     return _available_dices, _counted_dices, _round_over


winning_score = 0
score = 0
game_over = False
# game loop
while not game_over:
    dices = roll_dices(6)
    counted_dices = list()
    #display_dices(dices, counted_dices)
    eyes_counted, eyes_points = calculate_points(dices)
    display_points(eyes_counted, eyes_points)

    if score >= winning_score:
        game_over = True
