import random as r


def generate_hash_functions(p):
    a = []
    b = []
    for i in range(p):
        a.append(r.randint(1, p - 1))
        b.append(r.randint(0, p - 1))
    return a, b


def generate_hashes(songs, num_of_hashes):
    num_of_rows = len(songs)
    h, w = num_of_rows, num_of_hashes
    hashes = [[0 for x in range(w)] for y in range(h)]
    [a, b] = generate_hash_functions(num_of_hashes)
    for row_num in range(num_of_rows):
        for col_num in range(num_of_hashes):
            hashes[songs[row_num]][col_num] = (a[col_num] * row_num + b[col_num]) % p % num_of_rows

    return hashes


def min_occurring_hash(hashes, col_num, songs):
    min_hash = 9999
    for i in range(len(songs)):
        row = songs[i]
        if hashes[row][col_num] < min_hash:
            min_hash = hashes[songs[i]][col_num]
    return min_hash
