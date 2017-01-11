import file_util as fu

file_paths = fu.read_json("../paths.json")
input_path = file_paths["folderPath"] + file_paths["dataPath"]
input_path_short = file_paths["folderPath"] + file_paths["shortDataPath"]
prepared_data_path = file_paths["folderPath"] + file_paths["preparedDataPath"]
first100_users_path = file_paths["folderPath"] + file_paths["first100"]
output_path = file_paths["folderPath"] + file_paths["outputPath"]
output_path_100 = file_paths["folderPath"] + file_paths["outputPath100"]
expected_output_path = file_paths["folderPath"] + file_paths["expectedOutputPath"]