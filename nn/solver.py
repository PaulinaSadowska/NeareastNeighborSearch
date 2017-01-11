import paths as inp
import nn.data_preparation_hashes as pd
import file_util as fu

pd.prepare_data_ids(inp.input_path, inp.users_id_map_path, inp.prepared_data_hashes_path)

#SIGS =
#with fu.open_file(inp.prepared_data_hashes_path) as f:
#    user_id = -1
#    for line in f:
#        user_id += 1

