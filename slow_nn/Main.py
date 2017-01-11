import datetime as d
import operator

import file_util as fu
import paths as inp
import slow_nn.data_preparation as dp


def intersect(a, b):
    """ return the intersection of two lists """
    return len(list(set(a) & set(b)))


def union(a, b):
    """ return the union of two lists """
    return len(list(set(a) | set(b)))


def jaccard(u1, u2):
    return intersect(u1, u2) / union(u1, u2)


def find_nn():
    before = d.datetime.now()

    # dp.prepare_data(inp.input_path, inp.first100_users_path, inp.prepared_data_path)

    users_data = fu.read_json(inp.prepared_data_path)
    first100_users = []
    with fu.open_file(inp.first100_users_path) as f:
        for line in f:
            first100_users = line.split(",")

    users_results = {}
    i = -1
    for user in first100_users:
        user_results = {}
        i += 1
        for other_user in users_data:
            u1 = users_data[user]
            u2 = users_data[other_user]
            j = jaccard(u1, u2)
            user_results[other_user] = j
        users_results[user] = sorted(user_results.items(), key=operator.itemgetter(1), reverse=True)[:100]
        print(i)

    fu.write_json(inp.output_path_100, users_results)

    print("NN Search for {0} users took {1}".format(len(users_data), d.datetime.now() - before))


#dp.prepare_data(inp.input_path, inp.first100_users_path, inp.prepared_data_path)
