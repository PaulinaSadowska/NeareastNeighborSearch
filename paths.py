import file_util as fu

file_paths = fu.read_json("../paths.json")

# input
input_path = file_paths["folderPath"] + file_paths["dataPath"]
input_path_short = file_paths["folderPath"] + file_paths["shortDataPath"]

# slow
prepared_data_path = file_paths["folderPath"] + file_paths["preparedDataPath"]
first100_users_path = file_paths["folderPath"] + file_paths["first100"]

output_path_100 = file_paths["folderPath"] + file_paths["outputPath100"]

sparse_data_path = file_paths["folderPath"] + file_paths["sparseDataPath"]
first100_ids_users_path = file_paths["folderPath"] + file_paths["sparseFirst100"]

# faster?
users_id_map_path = file_paths["folderPath"] + file_paths["usersId"]
prepared_data_hashes_path = file_paths["folderPath"] + file_paths["preparedHashPath"]

output_path = file_paths["folderPath"] + file_paths["outputPath"]
