num_process = 5
active = set(range(1, num_process + 1))
coordinator = num_process

def election(pid):
    global coordinator
    print(f"Process {pid} starts election.")
    max_id = pid
    nxt = (pid % num_process) + 1
    while nxt != pid:
        if nxt in active:
            print(f"Process {pid} -> Process {nxt}")
            if nxt > max_id:
                max_id = nxt
        else:
            print(f"Process {nxt} is down.")
        nxt = (nxt % num_process) + 1
    coordinator = max_id
    print(f"Coordinator is Process {coordinator}\n")

def bring_up(pid):
    if pid in active:
        print(f"Process {pid} already up.")
    else:
        active.add(pid)
        print(f"Process {pid} is up.")
        election(pid)  # Start election from the newly added process

def bring_down(pid):
    global coordinator
    if pid not in active:
        print(f"Process {pid} already down.")
    else:
        active.remove(pid)
        print(f"Process {pid} is down.")
        if pid == coordinator and active:
            election(min(active))  # Trigger election from lowest active

def print_active():
    print("Active processes:", sorted(active))

def print_coordinator():
    print(f"Coordinator: Process {coordinator}" if coordinator else "Coordinator: None")

if __name__ == "__main__":
    while True:
        print("1) Start Election  2) Bring Up  3) Bring Down  4) Active  5) Coordinator  6) Exit")
        ch = int(input("Choice: "))
        if ch == 6: break
        pid = int(input("Process ID: ")) if ch in [1, 2, 3] else None
        if ch == 1: election(pid)
        elif ch == 2: bring_up(pid)
        elif ch == 3: bring_down(pid)
        elif ch == 4: print_active()
        elif ch == 5: print_coordinator()
