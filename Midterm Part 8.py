# Unique Common Elements
# sample: print(unique_common([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7]))
def add_to_list(the_list, value):
    if value not in the_list:
        the_list.append(value)

def unique_common(a, b):
    common_list = []
    for i in a:
        if i in b:
            add_to_list(common_list, i)

    for i in b:
        if i in a:
            add_to_list(common_list, i)

    if (len(common_list) > 0):
        return sorted(common_list)
    else:
        return None

