import socket, time, json

SERVER_IP, PORT = "127.0.0.1", 5000

def main():
    server_socket = socket.socket()
    server_socket.bind((SERVER_IP, PORT))
    server_socket.listen()
    print(f"Time server running at {SERVER_IP}:{PORT}")

    server_time = time.time()
    print(f"Server time: {server_time}")

    clients, client_times = [], []

    while input("Add clients? (y/n): ").lower() == "y":
        client, addr = server_socket.accept()
        print(f"Connected with {addr}")
        clients.append(client)

    for client in clients:
        client.send(json.dumps({"operation": "time_req"}).encode())
        resp = json.loads(client.recv(1024).decode())
        client_times.append(float(resp["client_time"]))

    offsets = [client_time - server_time for client_time in client_times]
    avg_offset = sum(offsets) / (len(client_times) + 1)

    for i, client in enumerate(clients):
        adj_time = json.dumps({
            "operation": "time_adj",
            "adjusted_time": avg_offset -(client_times[i] - server_time)
        })
        client.send(adj_time.encode())
        print(f"Adjusted time sent to {client.getpeername()}")

    server_socket.close()

if __name__ == "__main__":
    main()
