import paths as inp
import file_util as fu

numOfLines = 200000
lines = []

with fu.open_file(inp.input_path) as f:
    i = 0
    for line in f:
        lines.append(line)
        i += 1
        if i > numOfLines:
            break

fu.write_text(inp.input_path_short, "".join(lines))
