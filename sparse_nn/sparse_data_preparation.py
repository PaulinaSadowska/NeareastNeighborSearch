import datetime as d
import file_util as fu
import paths as inp
import sparse_util as su
from scipy.sparse import csr_matrix


def prepare_sparse_data(input_path, first_100_users_path, prepared_data_path):
    before = d.datetime.now()
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

            song_id = data[0]
            if song_id in songs_id:
                new_song_id = songs_id[song_id]
            else:
                new_song_id = len(songs_id)
            songs_id.setdefault(song_id, new_song_id)

            if user_id in users:
                if new_song_id not in users[user_id]:
                    users[user_id].append(new_song_id)
            else:
                users[user_id] = [new_song_id]
                if len(users) == 100:
                    fu.write_text(first_100_users_path, ",".join(users.keys()))

    # SAVE DATA
    fu.write_json(prepared_data_path, users)
    print("data prepared in {0}".format(d.datetime.now() - before))


def prepare_sparse_features(prepared_data, sparse_data_path):
    indptr = [0]
    indices = []
    data = []

    for record in prepared_data:
        songs = prepared_data[record]
        for song_id in songs:
            indices.append(song_id)
            data.append(1)

        indptr.append(len(indices))

    csr = csr_matrix((data, indices, indptr), dtype=int)
    #print(csr.toarray())
    su.save_sparse_csr(sparse_data_path, csr)


