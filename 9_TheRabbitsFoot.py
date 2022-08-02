from math import sqrt


def create_matrix(lens: int) -> list[list]:

    size = round(sqrt(lens), 2)
    row_len, colomn_len = int(size), int(round(size, 0))
    if lens > (row_len * colomn_len):
        row_len += 1
    matrix = [[''] * colomn_len for _ in range(row_len)]

    return matrix


def format_space_to_string(s: str) -> tuple[str, int]:

    s = s.replace(' ', '')
    len_string = len(s)

    return s, len_string


def read_matrix(matrix: list[list], encode: bool) -> str:

    result = ''

    if encode:
        for index_row, _ in enumerate(matrix):
            for index_col, _ in enumerate(matrix[index_row]):
                result += matrix[index_col][index_row]
            result += ' '
    else:
        for index_row, _ in enumerate(matrix):
            for index_col, _ in enumerate(matrix[index_row]):
                result += matrix[index_row][index_col]
            result += ' '

    return result


def write_matrix(matrix: list[list], string_data: str, en_code: bool) -> list[list]:

    index = 0

    if en_code:
        for index_row, _ in enumerate(matrix):
            for index_col, _ in enumerate(matrix[index_row]):
                if index <= len(string_data) - 1:
                    matrix[index_row][index_col] = string_data[index]
                    index += 1
                else:
                    matrix[index_row][index_col] = ''
    else:
        string_data = string_data.split(' ')
        for index_row, _ in enumerate(matrix):
            for index_col, _ in enumerate(matrix[index_row]):
                if len(string_data[index_row]) - 1 < index_col:
                    matrix[index_row][index_col] = ''
                    continue
                matrix[index_col][index_row] = string_data[index_row][index_col]

    return matrix


def encode_string(matrix: list[list], string_data: str, en_code: bool) -> str:

    result_matrix = read_matrix(write_matrix(matrix, string_data, en_code), en_code)

    return result_matrix


def decode_string(data_string: str, lens: int, en_code: bool):

    matrix_clean = create_matrix(lens)
    result = write_matrix(matrix_clean, data_string, en_code)
    result_str = read_matrix(result, en_code)

    return result_str.replace(' ', '')


def TheRabbitsFoot(s: str, en_code: bool) -> str:

    str_no_space, lens = format_space_to_string(s)
    matrix = create_matrix(lens)
    if en_code:
        return encode_string(matrix, str_no_space, en_code).strip()
    else:
        return decode_string(s, lens, en_code)
