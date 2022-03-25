import socket


def get_ip():
    name = input('URL:  ')
    try:
        return f'Hostname: {name}\nIP address: {socket.gethostbyname(name)}'
    except socket.gaierror as er:
        return f'Invalid name - {er}'


def main():
    print(get_ip())
    
    
if __name__ == '__main__':
    main()
  

# get an IP address
"""
import socket   

hostname = socket.gethostname()    
addr = socket.gethostbyname(hostname)    
print("Your IP address is:" + addr)  
"""
