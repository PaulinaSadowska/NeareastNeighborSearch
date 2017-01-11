import nn.input_paths as inp
import nn.data_preparation as dp
import file_util as fu

dp.prepare_data(inp.input_path_short, inp.prepared_data_path)

users_data = fu.read_json(inp.prepared_data_path)
users_results = {}
#for user in users_data:
    