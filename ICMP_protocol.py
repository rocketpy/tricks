#  icmplib - Easily forge ICMP packets and make your own ping and traceroute.

# PyPi:  https://pypi.org/project/icmplib/
#  pip install icmplib
#  pip install --upgrade icmplib

"""
Features
🌳 Ready-to-use: icmplib offers ready-to-use functions such as the most popular ones: ping, multiping and traceroute.
💎 Modern: This library uses the latest technologies offered by Python 3.6+ and is fully object-oriented.
🚀 Fast: Each class and function has been designed and optimized to deliver the best performance. Some functions are
          also multithreaded like the multiping function. You can ping the world in seconds!
⚡️ Powerful: Use the library without root privileges, set the traffic class of ICMP packets, customize their payload and more!
🔩 Evolutive: Easily build your own classes and functions with ICMPv4 and ICMPv6 sockets.
🔥 Seamless integration of IPv6: Use IPv6 the same way you use IPv4. Automatic detection is done without impacting performance.
🌈 Broadcast support (you must use the ICMPv4Socket class to enable it).
🍺 Support of all operating systems. Tested on Linux, macOS and Windows.
🤘 No dependency: icmplib is a pure Python implementation of the ICMP protocol. It does not use any external dependencies.
"""

# For simple use
from icmplib import ping, multiping, traceroute, resolve, Host, Hop

# For advanced use (sockets)
from icmplib import ICMPv4Socket, ICMPv6Socket, ICMPRequest, ICMPReply

# Exceptions
from icmplib import ICMPLibError, NameLookupError, ICMPSocketError
from icmplib import SocketAddressError, SocketPermissionError
from icmplib import SocketUnavailableError, SocketBroadcastError, TimeoutExceeded
from icmplib import ICMPError, DestinationUnreachable, TimeExceeded


#  Ping
# Send ICMP Echo Request packets to a network host.
ping(address, count=4, interval=1, timeout=2, id=PID, source=None, privileged=True, **kwargs)

"""
Example
>>> host = ping('1.1.1.1', count=10, interval=0.2)

>>> host.address            # The IP address of the host that responded
'1.1.1.1'                   # to the request

>>> host.min_rtt            # The minimum round-trip time
12.2

>>> host.avg_rtt            # The average round-trip time
13.2

>>> host.max_rtt            # The maximum round-trip time
17.6

>>> host.packets_sent       # The number of packets transmitted to the
10                          # destination host

>>> host.packets_received   # The number of packets sent by the remote
9                           # host and received by the current host

>>> host.packet_loss        # Packet loss occurs when packets fail to
0.1                         # reach their destination. Returns a float
                            # between 0 and 1 (all packets are lost)
>>> host.is_alive           # Indicates whether the host is reachable
True
"""

