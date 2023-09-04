import socket

host = '10.0.84.203'
porta = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, porta))

while True:
    command = input("Digite o comando (d/h/dh para data/hora/data e hora, ou /sair para sair): ")
    client_socket.send(command.encode())

    if command == "/sair":
        print("Cliente encerrado.")
        break

    resposta = client_socket.recv(1024).decode()
    print("Resposta do servidor:", resposta)

client_socket.close()
