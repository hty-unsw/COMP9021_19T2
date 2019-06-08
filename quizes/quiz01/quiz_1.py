# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange
from collections import Counter

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
    # ['0','4']
    # (0,4)
    # arg_for_seed, upper_bound  = (1,5)
    # arg_for_seed = 1
    # upper_bound = 5
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# 字典
mapping = {}
for i in range(1, upper_bound):
    # i = [1,5)
    # 1,2,3,4
    # -5 // 2
    # -upper_bound // 2 = -3
    # 在【-3，5)
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE
for index in range(1, upper_bound + 1):
    if index in mapping:
        continue
    else:
        nonkeys.append(index)

# 第一种写法。
# mapping_as_a_list = [None] * (upper_bound + 1)
# for key,value in mapping.items():
#     mapping_as_a_list[key] = value

# 第二种写法


for index in range(upper_bound + 1):
    # 0,1,2,3,4
    # {3:1}
    if index not in mapping:
        mapping_as_a_list.append(None)
    else:
        mapping_as_a_list.append(mapping[index])


values = [value for key, value in mapping.items()]
one_to_one_part_of_mapping = {key: value for key, value in mapping.items() if values.count(value) == 1}

# values  = [7,7]

counter = Counter(values)

# counter = {7:2}

for key, value in mapping.items():
    if counter[value] == 1:
        # if values.count(value) == 1:
        one_to_one_part_of_mapping[key] = value
    else:
        continue

# {4:7,8:7}
for key, value in mapping.items():
    # 设置初始化为0
    count = 0
    for key_1, value_1 in mapping.items():
        # 如果value相等，+1
        if value == value_1:
            count += 1
    # 如果重复的次数> 1
    if count > 1:
        continue
    else:
        one_to_one_part_of_mapping[key] = value


values = []
for index in range(upper_bound):
    if index not in mapping:
        if index > 0:
            nonkeys.append(index)
        mapping_as_a_list.append(None)
    else:
        mapping_as_a_list.append(mapping[index])
        values.append(mapping[index])

for k, v in mapping.items():
    if values.count(v) == 1:
        one_to_one_part_of_mapping[k] = v


print()
print(f'The mappings\'s so-called "keys" make up a set whose number of elements is {len(mapping)}.')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                              for key in sorted(one_to_one_part_of_mapping)
                              }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)
