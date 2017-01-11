import nn.input_paths as inp
import nn.data_preparation as dp
import file_util as fu
import operator
import datetime as d


def intersect(a, b):
    """ return the intersection of two lists """
    return len(list(set(a) & set(b)))


def union(a, b):
    """ return the union of two lists """
    return len(list(set(a) | set(b)))


def jaccard(u1, u2):
    return intersect(u1, u2) / union(u1, u2)


dp.prepare_data(inp.input_path, inp.prepared_data_path)

before = d.datetime.now()
users_data = fu.read_json(inp.prepared_data_path)

users_results = {}
for user in users_data:
    user_results = {}
    for other_user in users_data:
        u1 = users_data[user]
        u2 = users_data[other_user]
        j = jaccard(u1, u2)
        user_results[other_user] = j
    users_results[user] = sorted(user_results.items(), key=operator.itemgetter(1), reverse=True)[:100]

fu.write_json(inp.output_path, users_results)

print("NN Search for {0} users took {1}".format(len(users_data), d.datetime.now() - before))