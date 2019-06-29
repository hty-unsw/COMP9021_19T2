# Written by Eric Martin for COMP9021
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys
from collections import deque


def check_sign(param, arity):
    if param.find('(') > 0 or param.find(")") > 0:
        return False

    if len(param.split(",")) == arity:
        return True

    return False


def is_valid_1(word, arity):
    result = False
    param_word = word.replace(" ", "")
    if param_word:
        stack = [""]
        for item in param_word:
            # check 有效性
            if item == "(":
                stack.append("(")
                stack.append("")
            elif item == ")":
                temp = stack.pop()
                bracket = stack.pop()
                if check_sign(temp, arity) and bracket == "(":
                    continue
                else:
                    return False
            else:
                if not item.isalpha() and item != "_" and item != ",":
                    return False
                stack[-1] = stack[-1] + item

        if len(stack) == 1:
            return True
    return result


def is_valid(word, arity):
    result = False
    param_word = word.replace(" ", "")

    valid_chars = ["_", "(", ")", ","]
    # check valid
    for item in param_word:
        if not item.isalpha() and item not in valid_chars:
            return False

    if param_word.count("(") != param_word.count(")"):
        return False

    if param_word.count("(") == 0:
        return True

    if param_word:
        while param_word.find(")") > 0:
            right_index = param_word.index(")")
            right_part = param_word[right_index + 1:]

            left_index = param_word[0:right_index].rindex("(")
            left_part = param_word[left_index + 1:right_index]

            if len(left_part.split(",")) == arity:
                param_word = param_word[:left_index] + right_part
            else:
                result= False
                break
        else:
            result = True

    return result


try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
# word = "ff(ff(ff(a,b,ff(aa,bb,cc))  ,  b ,  ff(a,b,c))  ,  b  ,  ff(a,ff(a,b,c),c))"
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
