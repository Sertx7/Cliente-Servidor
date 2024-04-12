import socket

# Configurações do cliente
HOST = 'localhost'
PORT = 12345

# Solicita as notas ao usuário
nota1 = input('Insira a primeira nota: ')
nota2 = input('Insira a segunda nota: ')

# Criação do socket do cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Envia as notas para o servidor
    client_socket.sendall(f"{nota1} {nota2}".encode())

    # Recebe a média do servidor
    media = client_socket.recv(1024).decode()

    print('A média das notas é:', media)
