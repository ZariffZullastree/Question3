import socket

def main():
    host = '192.168.121.136'
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))

    while True:
        radius = input("Enter the radius of the sphere (or 'end' to quit): ")
        if radius.lower() == 'end':
            break

        try:
            radius_float = float(radius)
            client_socket.send(str(radius_float).encode())
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the radius.")

    client_socket.close()

if __name__ == "__main__":
    main()
