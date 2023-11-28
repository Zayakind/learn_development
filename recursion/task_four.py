def checking_palindrom(data: str):
    if len(data) < 1:
        return True
    if data[0] == data[-1]:
        return checking_palindrom(data[1:-1])
    return False
