import fileUtil as fu
import datetime as d

before = d.datetime.now()
file_paths = fu.read_json("../paths.json")

input_path = file_paths["folderPath"] + file_paths["dataPath"]
input_path_short = file_paths["folderPath"] + file_paths["shortDataPath"]
output_path = file_paths["folderPath"] + file_paths["outputPath"]
expected_output_path = file_paths["folderPath"] + file_paths["expectedOutputPath"]

users = {}
with fu.open_file(input_path_short) as f:
    i = 0
    for line in f:
        if i == 0:  # ignore first line
            i += 1
            continue
        data = line.split(",")
        userId = data[1]
        songId = data[0]
        if userId in users:
            if songId not in users[userId]:
                users[userId].append(songId)
        else:
            users[userId] = [songId]

for u in users:
    print(u + " {0}".format(len(users[u])))

print("executed in {0}".format(d.datetime.now() - before))
