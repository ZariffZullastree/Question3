import socket
import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def main():
    host = '192.168.121.136'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024).decode()
        if not data:
            break

        try:
            radius = float(data)
            volume = calculate_sphere_volume(radius)
            response = f"Volume of sphere with radius {radius} is {volume:.2f}"
        except ValueError:
            response = "Invalid radius value. Please send a valid numeric value."

        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    main()
