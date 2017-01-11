import file_util as fu
import datetime as d


def prepare_data(input_path, first_100_users_path, prepared_data_path):
    before = d.datetime.now()
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
            if user_id in users:
                if song_id not in users[user_id]:
                    users[user_id].append(song_id)
            else:
                users[user_id] = [song_id]
                if len(users) == 100:
                    fu.write_text(first_100_users_path, ",".join(users.keys()))
    fu.write_json(prepared_data_path, users)

    print("data prepared in {0}".format(d.datetime.now() - before))
