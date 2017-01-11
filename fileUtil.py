import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf8') as json_file:
        return json.load(json_file)


def write_json(file_path, json_data):
    with open(file_path, 'w', encoding='utf8') as json_file:
        json.dump(json_data, json_file)


def getArray(file_path):
    output = []
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            output.append(line.strip("\n"))

    return output


def write_text(file_path, data):
    with open(file_path, mode='wt', encoding='utf-8') as f:
        f.write(data)


def open_file(file_path):
    return open(file_path, 'r', encoding='utf8')