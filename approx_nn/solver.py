import paths as inp
import approx_nn.jaccard as jac
import file_util as fu
import datetime as d
import approx_nn.hash_helper as hh
import numpy as np


def add_pair(i, j, possible_pairs):
    if i in possible_pairs:
        if j not in possible_pairs[i]:
            possible_pairs[i].append(j)
    else:
        possible_pairs[i] = [j]


def get_possible_pairs(prepared_data):
    possible_pairs = {}
    indx = -1
    for k in range(len(prepared_data)):
        indx += 1
        if indx % 4 == 0:
            print(indx)
            for i in range(len(prepared_data[indx])):
                for o in range(len(prepared_data[indx]) - i):
                    j = o + i
                    if i != j:
                        if prepared_data[indx][i] == prepared_data[indx][j]:
                            if prepared_data[indx + 1][i] == prepared_data[indx + 1][j]:
                                if prepared_data[indx + 2][i] == prepared_data[indx + 2][j]:
                                    if prepared_data[indx + 3][i] == prepared_data[indx + 3][j]:
                                        add_pair(i, j, possible_pairs)
                                        add_pair(j, i, possible_pairs)
    return possible_pairs


def calculate_nn(input_path):
    num_of_hashes = 16
    p = 1583539
    before = d.datetime.now()
    users_id = {}
    songs_id = {}
    users = {}
    with fu.open_file(input_path) as f:
        i = 0
        for line in f:
            if i == 0:  # ignore first line
                i += 1
                continue

            data = line.split(",")
            user_id = data[1]
            if user_id in users_id:
                new_user_id = users_id[user_id]
            else:
                new_user_id = len(users_id)
            users_id.setdefault(user_id, new_user_id)

            song_id = data[0]
            if song_id in songs_id:
                new_song_id = songs_id[song_id]
            else:
                new_song_id = len(songs_id)

            songs_id.setdefault(song_id, new_song_id)

            if new_user_id in users:
                if new_song_id not in users[new_user_id]:
                    users[new_user_id].append(new_song_id)
            else:
                users[new_user_id] = [new_song_id]

    # CREATE TABLE OF SIG(n, c)
    sorted_songs = sorted(songs_id.values())
    hashes = hh.generate_hashes(list(sorted_songs), num_of_hashes, p)

    num_of_users = len(users)

    h, w = num_of_hashes, num_of_users
    prepared_data = np.arange(h * w, dtype='int')
    prepared_data = prepared_data.reshape(h, w)

    for i in range(num_of_hashes):
        for user_id in users:
            min_occ = hh.min_occurring_hash(hashes, i, users[user_id])
            prepared_data[i][user_id] = min_occ

    users_id_inv = {y: x for x, y in users_id.items()}
    # SAVE USERS MAP
    # fu.write_json(users_path, users_id_inv)

    print("data prepared in {0}".format(d.datetime.now() - before))

    possible_pairs = get_possible_pairs(prepared_data)
    all_results = {}
    print("{0} possible pairs found after {1}".format(len(possible_pairs), d.datetime.now() - before))
    for i in possible_pairs:
        results = {}
        for j in possible_pairs[i]:
            J = jac.jaccard(prepared_data[:, i], prepared_data[:, j])
            # print("{0}, {1} <= {2} (approx)".format(i, j, J))
            J2 = jac.jaccard(users[i], users[j])
            results[j] = "${0:.3f}  minhash:  ${1:.3f}".format(J2, J)
            # print("{0}, {1} <= {2}".format(i, j, J2))
        all_results[users_id_inv[i]] = results

    fu.write_json("../data/wyniki_200tys.json", all_results)
    print("for {0} users all took {1}".format(len(prepared_data[0]), d.datetime.now() - before))


calculate_nn(inp.input_path_short)
