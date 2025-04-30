import random

num_processes = 5
state = [True] * num_processes
leader = num_processes

def election(pid):
    global leader
    print(f"Process {pid} is starting election")
    for i in range(pid + 1, num_processes + 1):
        if state[i - 1]:
            print(f"Process {pid} -> Process {i}")
            pid = i
    leader = pid
    print(f"Process {leader} is now coordinator\n")

def up(pid):
    if state[pid - 1]:
        print(f"Process {pid} already up")
    else:
        state[pid - 1] = True
        print(f"Process {pid} is up")
        election(pid)

def down(pid):
    global leader
    if not state[pid - 1]:
        print(f"Process {pid} already down")
    else:
        state[pid - 1] = False
        print(f"Process {pid} is down")
        if leader == pid:
            active = [i + 1 for i in range(num_processes) if state[i]]
            if active:
                election(active[0])

def message(pid):
    if not state[pid - 1]:
        print(f"Process {pid} is down")
    elif not state[leader - 1]:
        print("Coordinator down. Starting election...")
        election(pid)
    else:
        print("OK")

if __name__ == "__main__":
    print("Processes up: p1 p2 p3 p4 p5")
    print(f"Initial coordinator: Process {leader}\n")
    
    while True:
        print("1) Up  2) Down  3) Message  4) Exit")
        ch = int(input("Choice: "))
        if ch == 4: break
        pid = int(input("Process ID: "))
        if ch == 1: up(pid)
        elif ch == 2: down(pid)
        elif ch == 3: message(pid)
