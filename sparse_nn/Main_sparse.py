import datetime as d
import operator

import file_util as fu
import paths as inp
import sparse_nn.sparse_data_preparation as dp


def intersect(a, b):
    return len(set(a) & set(b))


def union(a, b):
    return len(set(a) | set(b))


def jaccard(u1, u2):
    inters = intersect(u1, u2)
    if inters == 0:
        return 0
    return inters / union(u1, u2)


def find_nn(first_100_users_path, data_path, result_path):
    before = d.datetime.now()

    users_data = fu.read_json(data_path)
    first100_users = []
    with fu.open_file(first_100_users_path) as f:
        for line in f:
            first100_users = line.split(",")

    users_results = {}
    i = -1
    for user in first100_users:
        user_results = {}
        i += 1
        for other_user in users_data:
            j = jaccard(users_data[user], users_data[other_user])
            if j != 0:
                user_results[other_user] = j
        users_results[user] = sorted(user_results.items(), key=operator.itemgetter(1), reverse=True)[:100]
        print(i)

    fu.write_json(result_path, users_results)

    print("NN Search for {0} users took {1}".format(len(first100_users), d.datetime.now() - before))


dp.prepare_sparse_data(inp.input_path, inp.first100_ids_users_path, inp.sparse_data_path)
find_nn(inp.first100_ids_users_path, inp.sparse_data_path, inp.output_path_100)
