def read_input(filename, line_parse_function=None):
    output = []
    with open(filename, 'r') as f:
        for line in f:
            if not line_parse_function:
                output.append(line.strip())
            else:
                output.append(line_parse_function(line.strip()))

    return output 


def read_input_matrix(filename):
    output = []
    with open(filename, 'r') as f:
        for line in f:
            output.append(list(line.strip()))

    return output