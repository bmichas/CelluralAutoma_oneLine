# RULE_DICT = {'0': '000', '1': '001',
#              '0': '010', '1': '011', '1': '100',
#              '0': '101', '1': '110', '0': '111'}
import time
# RULE_DICT = {'000': '0', '001': '1',
#              '010': '0', '011': '1', '100': '1',
#              '101': '0', '110': '1', '111': '0'}
RULE_DICT = {'000': '1', '001': '1',
             '010': '0', '011': '0', '100': '1',
             '101': '0', '110': '1', '111': '1'}


def get_ascii(lst):
    ascii_lst = []
    for i in lst:
        i = int(i)
        if i == 1:
            ascii_lst.append('█')
        else:
            ascii_lst.append(' ')
    return ascii_lst


def get_line(lst):
    lst_after = []
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


def visualize(f_line):
    lst_print = get_ascii(f_line)
    print(lst_print)
    while True:
        next_line = get_line(f_line)
        lst_print = get_ascii(next_line)
        print(lst_print)
        time.sleep(0.2)
        f_line = next_line


lst = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
       '1', '0',  '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

visualize(lst)
