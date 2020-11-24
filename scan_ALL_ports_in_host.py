#  need add imports !!!


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
