
def LineAnalysis(line: str) -> bool:

    if line[0] != '*' and line[-1] != '*':
        return False

    line = line[1:-1]

    parse_string = line.split('*')
    equal = True
    example = parse_string[0]

    for i in parse_string:
        if i != example:
            equal = False

    return equal
