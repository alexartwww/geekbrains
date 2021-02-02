import re


def input_value(prompt='Input: ', pattern='^.+$', type=str):
    value = input(prompt)
    while not re.search(pattern, value):
        value = input(prompt)
    return type(value)


def format_value(value, pattern='^.+$', type=str):
    if re.search(pattern, value):
        return type(value)
    else:
        return None


def readfile(filename):
    result = ''
    try:
        with open(filename, 'r') as f:
            for line in f:
                result += line
    except IOError:
        return None
    return result
