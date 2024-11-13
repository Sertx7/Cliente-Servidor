# Sistema Cliente-Servidor / Client-Server System

Este projeto implementa uma aplicação cliente-servidor simples em Python, onde o cliente envia duas notas para o servidor, que calcula a média e envia o resultado de volta ao cliente. A comunicação entre o cliente e o servidor é realizada utilizando sockets com o protocolo TCP/IP.

en_US

This project implements a simple client-server application in Python, where the client sends two grades to the server, which calculates the average and sends the result back to the client. The communication between the client and the server is achieved using sockets with the TCP/IP protocol.

# Tecnologias Utilizadas

- Python: Linguagem de programação para implementação do sistema.
- Sockets (TCP/IP): Utilizados para comunicação entre cliente e servidor.

  en-US

- Python: Programming language used for the implementation of the system.
- Sockets (TCP/IP): Used for communication between the client and the server.

# Funcionalidade / Functionality

**Cliente**: / **Client**:

- Solicita ao usuário que insira duas notas.
- Envia as notas para o servidor.
- Recebe a média calculada pelo servidor e exibe o resultado.

en-US

- Requests the user to enter two grades.
- Sends the grades to the server.
- Receives the average calculated by the server and displays the result.

**Servidor**: / **Server**:

- Escuta uma porta específica e aguarda a conexão do cliente.
- Recebe as notas enviadas pelo cliente.
- Calcula a média das notas e envia a resposta de volta para o cliente.

en-US

- Listens on a specific port and waits for a client connection.
- Receives the grades sent by the client.
- Calculates the average of the grades and sends the result back to the client.
