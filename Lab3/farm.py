def is_possible_to_place(aggressive_cows_number, sorted_stables, min_distance):
    cows_to_place_number = aggressive_cows_number - 1
    cur_stable_index = 0
    for stable_index in range(1, len(sorted_stables)):
        if (sorted_stables[stable_index] - sorted_stables[cur_stable_index]) >= min_distance:
            cur_stable_index = stable_index
            cows_to_place_number -= 1

        if cows_to_place_number == 0:
            return True

    return False


def find_max_min_distance(aggressive_cows_number, sorted_stable, possible_answers):
    if len(possible_answers) == 0:
        return 0

    if len(possible_answers) == 1:
        return possible_answers[0]

    current_answer = possible_answers[len(possible_answers) // 2]

    if is_possible_to_place(aggressive_cows_number, sorted_stable, current_answer):
        next_step = find_max_min_distance(aggressive_cows_number, sorted_stable,
                                          possible_answers[len(possible_answers) // 2:])
    else:
        next_step = find_max_min_distance(
            aggressive_cows_number, sorted_stable, possible_answers[:len(possible_answers) // 2])
    return next_step


def solve_farm(cows_number, aggressive_cows_number, stables):
    if len(stables) != cows_number:
        return "Number of cows doesn't match number of free stables"
    stables.sort()

    max_possible_answer = (
        stables[-1] - stables[0]) // (aggressive_cows_number - 1)
    possible_answers = [i for i in range(max_possible_answer + 1)]
    return find_max_min_distance(aggressive_cows_number, stables, possible_answers)


if __name__ == "__main__":
    input_file = open("input.txt", "r")
    cows_number, aggressive_cows_number = map(
        int, input_file.readline().split(sep=","))
    stables = [int(input_file.readline()) for _ in range(cows_number)]
    input_file.close()

    output_file = open("output.txt", "w")
    output_file.write(
        str(solve_farm(cows_number, aggressive_cows_number, stables)))
