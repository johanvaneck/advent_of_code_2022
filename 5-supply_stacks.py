start_stack = '''
[T]     [Q]             [S]        
[R]     [M]             [L] [V] [G]
[D] [V] [V]             [Q] [N] [C]
[H] [T] [S] [C]         [V] [D] [Z]
[Q] [J] [D] [M]     [Z] [C] [M] [F]
[N] [B] [H] [N] [B] [W] [N] [J] [M]
[P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
[B] [W] [N] [P] [D] [V] [G] [L] [T]
 1   2   3   4   5   6   7   8   9 
 '''.strip()

steps = '''
move 5 from 4 to 9
move 3 from 5 to 1
move 12 from 9 to 6
move 1 from 6 to 9
move 3 from 2 to 8
move 6 from 3 to 9
move 2 from 2 to 9
move 2 from 3 to 5
move 9 from 8 to 1
move 1 from 6 to 9
move 1 from 8 to 3
move 14 from 1 to 2
move 8 from 2 to 6
move 2 from 2 to 7
move 2 from 5 to 8
move 5 from 2 to 6
move 9 from 7 to 8
move 1 from 9 to 8
move 5 from 6 to 9
move 1 from 3 to 8
move 1 from 7 to 5
move 1 from 1 to 5
move 4 from 1 to 7
move 15 from 6 to 1
move 4 from 7 to 6
move 2 from 5 to 7
move 9 from 8 to 7
move 13 from 1 to 3
move 8 from 6 to 9
move 1 from 6 to 8
move 1 from 7 to 5
move 2 from 1 to 3
move 4 from 7 to 1
move 13 from 3 to 6
move 2 from 1 to 3
move 1 from 5 to 8
move 2 from 3 to 4
move 5 from 7 to 1
move 4 from 1 to 9
move 2 from 4 to 5
move 4 from 6 to 2
move 3 from 2 to 5
move 6 from 8 to 1
move 7 from 6 to 7
move 1 from 3 to 5
move 1 from 2 to 4
move 8 from 1 to 8
move 4 from 6 to 2
move 3 from 5 to 3
move 1 from 4 to 3
move 2 from 1 to 3
move 8 from 8 to 5
move 2 from 3 to 8
move 4 from 5 to 3
move 1 from 9 to 2
move 1 from 8 to 3
move 1 from 2 to 1
move 15 from 9 to 3
move 6 from 7 to 5
move 1 from 7 to 3
move 2 from 2 to 8
move 6 from 9 to 4
move 22 from 3 to 6
move 3 from 8 to 6
move 1 from 1 to 2
move 2 from 9 to 8
move 6 from 4 to 7
move 6 from 7 to 2
move 16 from 6 to 9
move 8 from 2 to 1
move 4 from 6 to 1
move 2 from 3 to 4
move 9 from 5 to 4
move 1 from 7 to 9
move 1 from 6 to 2
move 3 from 5 to 7
move 16 from 9 to 4
move 2 from 7 to 1
move 4 from 6 to 3
move 1 from 9 to 5
move 1 from 9 to 7
move 1 from 7 to 6
move 1 from 7 to 9
move 2 from 9 to 2
move 1 from 6 to 1
move 2 from 8 to 1
move 11 from 4 to 2
move 9 from 2 to 6
move 9 from 6 to 1
move 15 from 4 to 6
move 1 from 4 to 2
move 1 from 5 to 3
move 6 from 6 to 4
move 3 from 2 to 1
move 2 from 4 to 6
move 3 from 6 to 2
move 7 from 6 to 2
move 1 from 4 to 7
move 1 from 7 to 2
move 5 from 3 to 6
move 1 from 5 to 4
move 1 from 4 to 5
move 8 from 1 to 6
move 1 from 4 to 8
move 12 from 6 to 1
move 1 from 3 to 4
move 1 from 4 to 1
move 1 from 3 to 4
move 2 from 6 to 5
move 31 from 1 to 7
move 2 from 5 to 7
move 1 from 8 to 2
move 1 from 5 to 8
move 1 from 8 to 6
move 3 from 4 to 9
move 3 from 9 to 4
move 2 from 4 to 3
move 2 from 1 to 6
move 2 from 3 to 8
move 1 from 4 to 9
move 4 from 2 to 9
move 17 from 7 to 8
move 3 from 8 to 2
move 2 from 9 to 4
move 4 from 2 to 5
move 1 from 1 to 4
move 1 from 9 to 3
move 8 from 8 to 4
move 1 from 9 to 4
move 4 from 8 to 3
move 8 from 2 to 5
move 2 from 2 to 3
move 1 from 2 to 1
move 1 from 8 to 4
move 2 from 8 to 1
move 1 from 7 to 2
move 1 from 8 to 6
move 3 from 4 to 5
move 8 from 4 to 7
move 1 from 2 to 8
move 1 from 8 to 1
move 2 from 4 to 7
move 8 from 5 to 9
move 7 from 5 to 2
move 6 from 3 to 1
move 6 from 1 to 2
move 9 from 9 to 4
move 5 from 7 to 4
move 2 from 1 to 2
move 9 from 4 to 2
move 3 from 6 to 2
move 1 from 6 to 8
move 1 from 8 to 9
move 1 from 3 to 5
move 6 from 7 to 5
move 4 from 4 to 2
move 19 from 2 to 3
move 1 from 4 to 6
move 7 from 7 to 5
move 2 from 1 to 8
move 12 from 3 to 4
move 3 from 4 to 1
move 1 from 6 to 3
move 8 from 5 to 9
move 3 from 9 to 7
move 6 from 4 to 3
move 3 from 1 to 2
move 13 from 3 to 7
move 3 from 4 to 6
move 4 from 9 to 4
move 14 from 7 to 8
move 3 from 5 to 2
move 3 from 2 to 6
move 1 from 6 to 2
move 1 from 3 to 9
move 4 from 4 to 6
move 11 from 2 to 7
move 2 from 9 to 6
move 3 from 5 to 6
move 1 from 9 to 7
move 14 from 6 to 5
move 1 from 5 to 1
move 4 from 5 to 8
move 2 from 5 to 6
move 4 from 2 to 5
move 1 from 2 to 9
move 14 from 8 to 5
move 2 from 8 to 4
move 3 from 8 to 7
move 5 from 5 to 4
move 13 from 5 to 7
move 5 from 7 to 6
move 31 from 7 to 9
move 7 from 6 to 7
move 6 from 5 to 7
move 1 from 8 to 9
move 1 from 5 to 3
move 1 from 3 to 5
move 1 from 1 to 8
move 6 from 4 to 3
move 1 from 8 to 5
move 1 from 4 to 1
move 33 from 9 to 3
move 13 from 7 to 1
move 29 from 3 to 2
move 3 from 3 to 8
move 1 from 5 to 2
move 20 from 2 to 6
move 19 from 6 to 4
move 1 from 7 to 4
move 5 from 1 to 7
move 1 from 8 to 7
move 2 from 8 to 5
move 10 from 2 to 8
move 6 from 3 to 9
move 4 from 7 to 1
move 1 from 3 to 5
move 1 from 1 to 2
move 1 from 7 to 6
move 1 from 2 to 8
move 1 from 8 to 7
move 4 from 9 to 7
move 2 from 5 to 2
move 1 from 8 to 5
move 1 from 8 to 6
move 7 from 8 to 3
move 2 from 9 to 4
move 3 from 5 to 1
move 2 from 2 to 5
move 5 from 7 to 8
move 10 from 4 to 1
move 5 from 8 to 5
move 10 from 1 to 3
move 2 from 6 to 4
move 1 from 7 to 3
move 1 from 8 to 1
move 3 from 5 to 8
move 12 from 4 to 7
move 3 from 5 to 3
move 16 from 1 to 7
move 2 from 3 to 7
move 1 from 5 to 6
move 3 from 8 to 4
move 1 from 4 to 7
move 1 from 6 to 3
move 14 from 3 to 1
move 5 from 3 to 8
move 1 from 3 to 5
move 1 from 7 to 6
move 1 from 6 to 2
move 13 from 7 to 2
move 1 from 5 to 3
move 3 from 4 to 2
move 1 from 3 to 5
move 3 from 8 to 9
move 2 from 8 to 9
move 1 from 6 to 4
move 5 from 2 to 4
move 3 from 2 to 5
move 7 from 7 to 3
move 7 from 4 to 7
move 5 from 3 to 7
move 8 from 2 to 3
move 5 from 9 to 5
move 11 from 1 to 9
move 4 from 3 to 1
move 1 from 2 to 7
move 4 from 1 to 7
move 22 from 7 to 3
move 5 from 3 to 4
move 1 from 7 to 1
move 1 from 1 to 4
move 3 from 4 to 6
move 3 from 1 to 3
move 2 from 6 to 1
move 2 from 4 to 9
move 13 from 9 to 1
move 1 from 6 to 5
move 4 from 7 to 1
move 3 from 1 to 6
move 19 from 3 to 9
move 5 from 3 to 1
move 18 from 9 to 8
move 1 from 9 to 3
move 11 from 1 to 7
move 1 from 4 to 5
move 13 from 8 to 1
move 7 from 5 to 8
move 7 from 8 to 5
move 3 from 6 to 5
move 2 from 3 to 9
move 1 from 3 to 7
move 5 from 5 to 2
move 10 from 1 to 5
move 9 from 7 to 9
move 11 from 5 to 2
move 2 from 8 to 4
move 1 from 4 to 3
move 2 from 7 to 3
move 1 from 7 to 4
move 3 from 8 to 3
move 8 from 5 to 2
move 2 from 3 to 8
move 4 from 3 to 8
move 6 from 2 to 6
move 5 from 1 to 8
move 8 from 2 to 7
move 2 from 4 to 7
move 9 from 2 to 9
move 4 from 7 to 8
move 5 from 1 to 8
move 3 from 7 to 4
move 1 from 8 to 3
move 3 from 7 to 2
move 3 from 1 to 9
move 1 from 4 to 9
move 1 from 6 to 3
move 18 from 8 to 5
move 1 from 8 to 2
move 2 from 4 to 9
move 3 from 2 to 1
move 2 from 2 to 3
move 24 from 9 to 8
move 3 from 3 to 7
move 15 from 8 to 2
move 12 from 2 to 5
move 1 from 7 to 4
move 1 from 3 to 1
move 28 from 5 to 4
move 1 from 7 to 9
move 2 from 2 to 1
move 4 from 6 to 3
move 1 from 5 to 3
move 1 from 5 to 9
move 1 from 2 to 6
move 5 from 3 to 5
move 8 from 4 to 2
move 2 from 6 to 2
move 1 from 7 to 3
move 4 from 2 to 8
move 3 from 1 to 2
move 5 from 2 to 5
move 3 from 5 to 4
move 2 from 1 to 5
move 2 from 2 to 1
move 4 from 9 to 2
move 7 from 8 to 9
move 1 from 3 to 1
move 1 from 1 to 7
move 2 from 8 to 3
move 4 from 9 to 3
move 9 from 5 to 7
move 3 from 3 to 5
move 1 from 5 to 3
move 7 from 7 to 9
move 1 from 7 to 9
move 1 from 5 to 9
move 1 from 5 to 1
move 1 from 8 to 5
move 9 from 9 to 1
move 2 from 7 to 2
move 1 from 5 to 6
move 4 from 3 to 2
move 11 from 2 to 4
move 1 from 8 to 4
move 1 from 8 to 2
move 1 from 2 to 8
move 1 from 6 to 5
move 1 from 8 to 6
move 6 from 1 to 7
move 1 from 5 to 6
move 1 from 6 to 5
move 3 from 9 to 8
move 3 from 8 to 1
move 3 from 7 to 8
move 1 from 6 to 9
move 1 from 2 to 4
move 1 from 9 to 7
move 2 from 7 to 9
move 10 from 1 to 6
move 2 from 9 to 3
move 1 from 5 to 7
move 3 from 7 to 5
move 3 from 5 to 3
move 4 from 6 to 3
move 18 from 4 to 2
move 3 from 4 to 1
move 1 from 1 to 3
move 2 from 1 to 2
move 8 from 2 to 9
move 1 from 4 to 7
move 1 from 7 to 1
move 3 from 9 to 2
move 3 from 8 to 6
move 1 from 4 to 9
move 7 from 2 to 8
move 7 from 6 to 7
move 3 from 9 to 2
move 3 from 2 to 5
move 6 from 4 to 6
move 2 from 5 to 6
move 3 from 3 to 6
move 6 from 6 to 3
move 5 from 7 to 5
move 2 from 4 to 8
move 5 from 5 to 2
move 1 from 7 to 2
move 4 from 6 to 4
move 1 from 7 to 8
move 1 from 6 to 4
move 1 from 5 to 7
move 1 from 3 to 4
move 1 from 6 to 4
move 2 from 9 to 1
move 3 from 1 to 3
move 1 from 3 to 1
move 9 from 2 to 1
move 8 from 1 to 5
move 1 from 7 to 1
move 1 from 9 to 1
move 4 from 5 to 7
move 4 from 7 to 5
move 1 from 1 to 9
move 5 from 2 to 4
move 1 from 9 to 6
move 8 from 8 to 9
move 18 from 4 to 9
move 3 from 5 to 4
move 2 from 6 to 5
move 1 from 8 to 5
move 17 from 9 to 6
move 2 from 8 to 1
move 1 from 4 to 6
move 8 from 6 to 3
move 1 from 1 to 8
move 5 from 5 to 3
move 1 from 1 to 7
move 1 from 8 to 6
move 2 from 4 to 5
move 6 from 9 to 4
move 1 from 7 to 5
move 7 from 6 to 8
move 2 from 6 to 5
move 6 from 8 to 3
move 1 from 9 to 6
move 2 from 9 to 5
move 1 from 3 to 1
move 1 from 8 to 6
move 7 from 5 to 6
move 7 from 6 to 7
move 5 from 4 to 9
move 1 from 4 to 5
move 2 from 9 to 6
move 3 from 1 to 7
move 5 from 6 to 8
move 1 from 1 to 5
move 21 from 3 to 6
move 3 from 7 to 2
move 2 from 9 to 3
move 1 from 9 to 7
move 5 from 5 to 7
move 7 from 6 to 7
move 14 from 7 to 1
move 3 from 2 to 8
move 12 from 1 to 4
move 5 from 7 to 6
move 1 from 7 to 4
move 8 from 8 to 3
move 8 from 3 to 5
move 6 from 5 to 6
move 1 from 5 to 3
move 2 from 1 to 8
move 2 from 8 to 3
move 10 from 3 to 7
move 8 from 4 to 3
move 3 from 4 to 9
move 3 from 9 to 2
move 1 from 2 to 5
move 2 from 2 to 9
move 13 from 3 to 1
move 1 from 4 to 1
move 2 from 1 to 7
move 1 from 5 to 8
move 1 from 9 to 6
move 1 from 9 to 2
move 1 from 4 to 9
move 8 from 6 to 2
move 1 from 9 to 5
move 1 from 2 to 8
move 1 from 5 to 9
move 2 from 2 to 3
move 12 from 6 to 8
move 1 from 3 to 7
move 8 from 8 to 4
move 1 from 9 to 1
move 13 from 1 to 3
move 2 from 4 to 5
move 12 from 7 to 2
move 1 from 5 to 8
move 3 from 3 to 8
move 2 from 4 to 1
move 1 from 1 to 9
'''.strip()

import re
from time import sleep

def decode_stack(processed):
    stacks = []
    for line in processed.split('\n'):
        for index, char in enumerate(line):
            stack_number = int((index-1)/4)
            if len(stacks) <= stack_number:
                stacks.append([])
            if (index-1)%4 == 0 and char != ' ':
                stacks[stack_number].append(char)
    return [stack[::-1][1:] for stack in stacks] 

def encode_stack(raw_matrix):
    n_stacks = len(raw_matrix)
    height = len(max(raw_matrix, key = len))
    stack_string = ''
    base_string = ''.join([f' {n+1}  ' for n in range(n_stacks)])
    for m in range(height):
        row_string = ''
        for n in range(n_stacks):
            try:
                item = raw_matrix[n][m]
                row_string += f'[{item}] '
            except:
                row_string += '    '
        stack_string = row_string + '\n' + stack_string
    return stack_string + base_string


# part 1
stacks = decode_stack(start_stack)
for instruction in steps.split('\n'):
    regex_groups = re.search(r'(\d+).*(\d+).*(\d+)', instruction).groups()
    count, from_stack, to_stack = [int(d) for d in regex_groups]
    for _ in range(count):
        stacks[to_stack-1].append(stacks[from_stack-1].pop())

print(encode_stack(stacks))
print(''.join([stack[-1] for stack in stacks if len(stack) > 0]))


# part 2
stacks = decode_stack(start_stack)
for instruction in steps.split('\n'):
    regex_groups = re.search(r'(\d+).*(\d+).*(\d+)', instruction).groups()
    count, from_stack, to_stack = [int(d) for d in regex_groups]
    stacks[to_stack-1].extend(stacks[from_stack-1][-count:])
    stacks[from_stack-1] = stacks[from_stack-1][:-count]

print(encode_stack(stacks))
print(''.join([stack[-1] for stack in stacks if len(stack) > 0]))
