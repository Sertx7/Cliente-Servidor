import socket

# Configurações do servidor
HOST = 'localhost'
PORT = 12345

# Criação do socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print('Servidor esperando conexão...')

    # Aceita a conexão do cliente
    conn, addr = server_socket.accept()
    print('Conectado a', addr)

    # Recebe as notas do cliente
    data = conn.recv(1024).decode()
    notas = [float(nota) for nota in data.split()]

    # Calcula a média
    media = sum(notas) / len(notas)

    # Envia a média de volta para o cliente
    conn.sendall(str(media).encode())
