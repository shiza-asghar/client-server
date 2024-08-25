import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            message = input("Enter message to send to server: ")
            if message.lower() == 'exit':
                print("Closing connection.")
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
