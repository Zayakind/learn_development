def calculating_len(data: list):
    if not data:
        return 0
    return 1 + calculating_len(data)
