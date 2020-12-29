import re


def input_value(prompt='Input: ', pattern='^.+$', type=str):
    value = input(prompt)
    while not re.search(pattern, value):
        value = input(prompt)
    return type(value)
