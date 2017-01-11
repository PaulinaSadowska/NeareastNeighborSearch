import fileUtil as fu
import datetime as d

before = d.datetime.now()
file_paths = fu.read_json("../paths.json")

input_path = file_paths["folderPath"] + file_paths["dataPath"]
output_path = file_paths["folderPath"] + file_paths["outputPath"]
expected_output_path = file_paths["folderPath"] + file_paths["expectedOutputPath"]

print(input_path)
print(output_path)
users = {}
with fu.open_file(input_path) as f:
    for line in f:
        userId = line.split(",")[1]
        users[userId] = 1

print(len(users))

print("executed in {0}".format(d.datetime.now() - before))

