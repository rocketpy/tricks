# by curl
# $ curl 'https://api.ipify.org?format=json'


# get local ip
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
