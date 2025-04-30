import socket, time, json, random

SERVER_IP, PORT = "127.0.0.1", 5000

def main():
    clinet_socket = socket.socket()
    clinet_socket.connect((SERVER_IP, PORT))
    print(f"Connected to {SERVER_IP}:{PORT}")

    local_time = time.time()

    while True:
        msg = json.loads(clinet_socket.recv(1024).decode())
        
        if msg["operation"] == "time_req":
            print(f"Local time: {local_time}")
            clinet_socket.send(json.dumps({"client_time": local_time}).encode())

        elif msg["operation"] == "time_adj":
            print(f"Time adjustment: {msg['adjusted_time']}")
            local_time += float(msg["adjusted_time"])
            print(f"Adjusted time: {local_time}")
            break

    clinet_socket.close()

if __name__ == "__main__":
    main()
