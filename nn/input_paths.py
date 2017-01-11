import file_util as fu

file_paths = fu.read_json("../paths.json")
input_path = file_paths["folderPath"] + file_paths["dataPath"]
input_path_short = file_paths["folderPath"] + file_paths["shortDataPath"]
prepared_data_path = file_paths["folderPath"] + file_paths["preparedDataPath"]
output_path = file_paths["folderPath"] + file_paths["outputPath"]
expected_output_path = file_paths["folderPath"] + file_paths["expectedOutputPath"]