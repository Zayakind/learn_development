def checking_palindrom(data: str):
    if len(data) < 1:
        return True
    if data[0] != data[-1]:
        return False
    return checking_palindrom(data)
