def intersect(a, b):
    return len(set(a) & set(b))


def union(a, b):
    return len(set(a) | set(b))


def jaccard(u1, u2):
    inters = intersect(u1, u2)
    if inters == 0:
        return 0
    return inters / (len(u1) + len(u2) + inters)
