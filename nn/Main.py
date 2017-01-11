import fileUtil as fu

file_paths = fu.read_json("../paths.json")

input_path = [file_paths["folderPath"] + file_paths["dataPath"]]
output_path = [file_paths["folderPath"] + file_paths["outputPath"]]

print(input_path)
print(output_path)