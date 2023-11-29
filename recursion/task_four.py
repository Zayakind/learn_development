def checking_palindrom(data: str, index: int = 0):
    if len(data) < 1 or index == len(data):
        return True
    if data[0] != data[-1]:
        return False
    return checking_palindrom(data, index + 1)
