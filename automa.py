import time
# gdy chcesz zajac cała konsole użyj tego :)
# 000000000000000000010000000000000000000
# RULE_DICT = {'000': '0', '001': '1',
#              '010': '0', '011': '1', '100': '1',
#              '101': '0', '110': '1', '111': '0'}


def get_ascii(lst):
    ascii_lst = []
    for i in lst:
        i = int(i)
        if i == 1:
            ascii_lst.append('█')
        else:
            ascii_lst.append(' ')
    return ascii_lst


def get_line(lst, RULE):
    lst_after = []
    RULE_DICT = RULE
    for i in range(len(lst)):
        lst_len = len(lst)
        counter = i + 1
        if lst_len == counter:
            right = 0
        else:
            right = i + 1

        center_lst = lst[i]
        left = i - 1
        left_lst = lst[left]
        right_lst = lst[right]

        code = str(left_lst)+str(center_lst)+str(right_lst)
        value = RULE_DICT[code]
        lst_after.append(value)

    return lst_after


def visualize(f_line, RULE):
    lst_print = get_ascii(f_line)
    print(lst_print)
    while True:
        next_line = get_line(f_line, RULE)
        lst_print = get_ascii(next_line)
        print(lst_print)
        time.sleep(0.2)
        f_line = next_line


def check_matrix(matrix_toCheck):
    print(matrix_toCheck)
    for i in matrix_toCheck:
        if int(i) == 0 or int(i) == 1:
            state = True
            pass
        else:
            state = False
    return matrix_toCheck, state


def check_rules(rules_toCheck):
    rule_len = len(rules_toCheck)
    if rule_len == 1:
        state = True
        for i in rules_toCheck:
            if int(i) == 0 or int(i) == 1:
                state = True
                pass
            else:
                state = False
    else:
        state = False
    return rules_toCheck, state


def get_matrix():
    matrix_input = input("Wpisz pierwszy wiersz macierzy tylko 0 i 1: ")
    while True:
        if matrix_input.isdigit() == False:
            matrix_input = input("Wprowadziłeś znak: ")
            continue
        else:
            matrix_checked, state = check_matrix(matrix_input)
            if state:
                break
            else:
                matrix_input = input("W wierszu były liczby po za zakresem: ")
                continue

    return matrix_checked


def get_rules():
    rules = ['000', '001', '010', '011', '100', '101', '110', '111']
    rules_lst = []
    for rule in rules:
        rules_input = input(
            "Wpisz logike dla zasady %s : " % rule)
        while True:
            if rules_input.isdigit() == False:
                rules_input = input("Wprowadziłeś znak: ")
                continue
            else:
                rules_checked, state = check_rules(rules_input)
                if state:
                    break
                else:
                    rules_input = input(
                        "Zasada była za długa lub wystąpiła liczba po za zakresem: ")
                    continue
        rules_lst.append(rules_checked)

    return rules_lst


def main():
    matrix = get_matrix()
    rules = get_rules()
    print(rules[1])
    RULE_DICT = {'000': rules[0], '001': rules[1],
                 '010': rules[2], '011': rules[3], '100': rules[4],
                 '101': rules[5], '110': rules[6], '111': rules[7]}
    visualize(matrix, RULE_DICT)


if __name__ == "__main__":
    main()
