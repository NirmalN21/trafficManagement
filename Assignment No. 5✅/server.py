import socket
import threading

TOKEN = "TOKEN"
PORT = 8080
clients = []
running = True

def handle_client(c):
    global clients, running
    while running:
        try:
            data = c.recv(1024).decode()
            if data == "CLOSE":
                if c in clients:
                    clients.remove(c)
                c.close()
                break
            if data == TOKEN:
                if c in clients:
                    next_index = (clients.index(c) + 1) % len(clients)
                    next_c = clients[next_index]
                    next_c.send(TOKEN.encode())
        except:
            break

def stop_server(s):
    global running
    running = False
    for c in clients:
        try:
            c.send("CLOSE".encode())
            c.close()
        except:
            pass
    s.close()
    
def start_server():
    global clients, running
    server_socket = socket.socket()
    server_socket.bind(("localhost", PORT))
    server_socket.listen()
    print("Server started.")
    try:
        while running:
            c, _ = server_socket.accept()
            clients.append(c)
            print("Client connected.")
            print(clients)
            if len(clients) == 1:
                c.send(TOKEN.encode())
            threading.Thread(target=handle_client, args=(c,)).start()
    except KeyboardInterrupt:
        stop_server(server_socket)

if __name__ == "__main__":
    start_server()
