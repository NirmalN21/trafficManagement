import socket
import time

ADDR = ("localhost", 8080)

def start_client():
    client_socket = socket.socket()
    client_socket.connect(ADDR)
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if data == "TOKEN":
                print("Token received. Using resource...")
                if input("Is the prcess of current client done? (y/n): ").lower() == "y":
                    print("Done. Passing token.")
                    client_socket.send("TOKEN".encode())
            elif data == "CLOSE":
                break
    except KeyboardInterrupt:
        try:
            client_socket.send("CLOSE".encode())
        except:
            pass
    client_socket.close()

if __name__ == "__main__":
    start_client()
