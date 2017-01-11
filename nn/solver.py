import paths as inp
import nn.data_preparation_hashes as pd

pd.prepare_data_ids(inp.input_path_short, inp.users_id_map_path, inp.prepared_data_hashes_path)
