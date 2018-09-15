def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    if ltype not in ltypes:
        return to_iterable(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


def to_iterable(obj):
    if obj:
        if type(obj) is str:
            return [obj]
        try:
            iter(obj)
            return obj
        except TypeError:
            return [obj]
    return None


def to_list_of_dicts(objects):
    return [obj.dict() for obj in objects]


def get_or_create_array(dict, key):
    if key not in dict:
        dict[key] = []
    return dict[key]
