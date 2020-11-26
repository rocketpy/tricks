import socket
import concurrent.futures


def check_open_port(host, port):
    s = socket.socket()
    s.settimeout(0.1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        code = s.connect_ex((host, port))
        s.close()

        if code == 0:
            return True
        else:
            return False
    except socket.error:
        return False


def get_open_ports(host, max_port=65535):
    open_ports = []

    def worker(port):
        if check_open_port(host, port):
            open_ports.append(port)


    pool = ThreadPoolExecutor(max_workers=10)  # try change quantity max_workers=
    [pool.submit(worker, port) for port in range(1, max_port + 1)]
    pool.shutdown(wait=True)

    return open_ports

"""
import socket
import threading
from queue import *


print_lock = threading.Lock()
target = input("Enter websit or IP Adress to scan: ")
minPort = int(input("Enter minimum Port to scan (1 is the smallest): "))
maxPort = int(input("Enter maximum Port to scan: "))
threadNo = int(input("Enter No. of threads to use(500 is a good all around number): "))

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print("Port", port, "is open!")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(threadNo):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range (minPort, maxPort):
     q.put(worker)

q.join()
"""
