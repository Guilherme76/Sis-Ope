import socket
import threading
import datetime

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode()

        if command == "/sair":
            print("Cliente desconectado.")
            break
        elif command == "d":
            data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
            client_socket.send(data_atual.encode())
        elif command == "h":
            hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
            client_socket.send(hora_atual.encode())
        elif command == "dh":
            data_hora_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            client_socket.send(data_hora_atual.encode())
        else:
            client_socket.send("Comando inválido.".encode())

    client_socket.close()

host = '10.0.84.203'
porta = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, porta))
server_socket.listen(5)
print(f"Servidor escutando em {host}:{porta}")

while True:
    client_sock, client_addr = server_socket.accept()
    print(f"Cliente conectado: {client_addr[0]}:{client_addr[1]}")

    client_handler = threading.Thread(target=handle_client, args=(client_sock,))
    client_handler.start()
