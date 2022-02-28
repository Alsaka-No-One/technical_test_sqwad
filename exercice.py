def get_smaller_positive(list):
    smaller = 0
    for i in list:
        if (i < smaller and i > 0):
            smaller = i
    return smaller

def first_missing_positive(a):
    number = get_smaller_positive(a) + 1
    while True:
        if number not in a:
            return number
        number += 1
