import paths as inp
import approx_nn.data_preparation_hashes as pd
import file_util as fu

pd.prepare_data_ids(inp.input_path_short, inp.users_id_map_path, inp.prepared_data_hashes_path)

possible_pairs = []

with fu.open_file(inp.prepared_data_hashes_path) as f:
    bucket = []
    for line in f:
        bucket.append(line.strip("\n").split(","))
        if len(bucket) == 4:
            for i in range(len(bucket[0])-1):
                for j in range(len(bucket[0]) - 1):
                    if i != j and bucket[0][i] == bucket[0][j]:
                        if bucket[1][i] == bucket[1][j]:
                            if bucket[2][i] == bucket[2][j]:
                                if bucket[3][i] == bucket[3][j]:
                                    possible_pairs.append("{0}, {1}".format(i, j))
            bucket = []
            



