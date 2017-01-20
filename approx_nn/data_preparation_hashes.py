import file_util as fu
import datetime as d
import approx_nn.hash_helper as hh


def prepare_data_ids(input_path, users_path, prepared_data_path):
    num_of_hashes = 2
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
    hashes = hh.generate_hashes(list(sorted_songs), num_of_hashes)
    prepared_data = [""] * len(users)

    for user_id in users:
        for i in range(num_of_hashes):
            min_occ = hh.min_occurring_hash(hashes, i, users[user_id])
            prepared_data[user_id] += "{0},".format(min_occ)

        prepared_data[user_id] = prepared_data[user_id].strip(',')

    users_id_inv = {y: x for x, y in users_id.items()}
    # SAVE DATA
    fu.write_json(users_path, users_id_inv)
    fu.write_text(prepared_data_path, "\n".join(prepared_data))

    print("data prepared in {0}".format(d.datetime.now() - before))
