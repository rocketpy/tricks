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
# Commands executed after this point will see the forwarded agent on
# the remote end.
session.exec_command("git clone https://my.git.repository/")
