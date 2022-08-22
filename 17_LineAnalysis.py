
def LineAnalysis(line: str) -> bool:

    if line[0] != '*' and line[-1] != '*':
        return False

    line = line[1:-1]

    parse_string = line.split('*')
    check = True
    example = parse_string[0]

    for i in parse_string:
        if i != example:
            check = False

    return check


print(LineAnalysis("*"))

