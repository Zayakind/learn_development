1) Инициализация во время компиляции кода:

DEFAULT_SERVER_PORT = 11000
<-- code here -->
server_address_info = '127.0.0.1', DEFAULT_SERVER_PORT
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.connect(server_adress_info)

Хранить значения важное для работы программы в одном месте и в случае его изменения, менять его только в одном месте.

2) Инициализация во время написания кода:

sammary_km = 0

for hour in range(1, len(oksana), 2):
    if hour != 1:
        summ_hour = oksana[hour-1] * (oksana[hour] - oksana[hour-2])
    else:
        summ_hour = oksana[hour-1] * oksana[hour]
    sammary_km += summ_hour
return sammary_km

В данном случае sammary_km суммирует в себе все посчитанные километры.

3) Инициализация во время выполнения программы:

nickname = input("Write You nickname")
print("you letter" + nickname)

Подобная инициализация необходима в случае, например, когда данные вводит пользователь, такие как свой nickname.