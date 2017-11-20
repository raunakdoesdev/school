import functools

l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

def compare(item1, item2):
    item1 = item1.split(".")
    item2 = item2.split(".")

    for i in range (min(len(item1), len(item2))):
        if int(item1[i]) < int(item2[i]):
            return -1
        elif int(item1[i]) > int(item2[i]):
            return 1
    if len(item1) < len(item2):
        return -1
    else:
        return 1

return sorted(l, key=functools.cmp_to_key(compare))
