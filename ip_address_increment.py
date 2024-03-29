# ipaddress
# IPv4/IPv6 manipulation library

# https://pypi.org/project/ipaddress/
# https://docs.python.org/dev/library/ipaddress.html

# pip install ipaddress

#  IP address representations:
from __future__ import unicode_literals
import ipaddress

ipaddress.ip_address('1.2.3.4')
IPv4Address(u'1.2.3.4')

# or

ipaddress.ip_address(u'1.2.3.4')
IPv4Address(u'1.2.3.4')

# but not !!!
ipaddress.ip_address(b'1.2.3.4')

# IPv4Address(3691907365)  # From an int
# IPv4Address('220.14.9.37')

IPv4Address(b"\xdc\x0e\t%")  # From bytes (packed form)
# IPv4Address('220.14.9.37')


# ipaddress.ip_network
# The ipaddress.ip_network function allows you to create an object that describes a network(IPv4 или IPv6):
subnet_1 = ipaddress.ip_network('80.0.1.0/28')

subnet1.broadcast_address
IPv4Address('80.0.1.15')
subnet1.with_netmask
# '80.0.1.0/255.255.255.240'
subnet1.with_hostmask
# '80.0.1.0/0.0.0.15'
subnet1.prefixlen
# 28
subnet1.num_addresses
# 16

# ipaddress.ip_address
import ipaddress

ipv4 = ipaddress.ip_address('10.0.1.1')
# ipv4
IPv4Address('10.0.1.1')

# Methods ipv4.
ipv4.compressed       ipv4.is_loopback      ipv4.is_unspecified   ipv4.version
ipv4.exploded         ipv4.is_multicast     ipv4.max_prefixlen
ipv4.is_global        ipv4.is_private       ipv4.packed
ipv4.is_link_local    ipv4.is_reserved      ipv4.reverse_pointer
 
# check which range an address belongs to
ipv4.is_loopback
# False
ipv4.is_multicast
# False
ipv4.is_reserved
# False
ipv4.is_private
# True

# Arithmetic Operation on IPv4 address
print (ipaddress.IPv4Address(u'0.0.0.0')-1)
print(ipaddress.IPv4Address(u'129.117.0.0')-6)
print (ipaddress.IPv4Address(u'175.199.42.211')+55)
print (ipaddress.IPv4Address(u'255.255.255.255')+1)
 
  
# Arithmetic Operation on IPv6 address
print (ipaddress.IPv6Address(u'0000::0000')-1)
print (ipaddress.IPv6Address(u'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')+1)
print (ipaddress.IPv6Address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334')-330)
print (ipaddress.IPv6Address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334')+1000)

# Conversion to Strings and Integers
str(ipaddress.IPv4Address('192.168.0.1'))
# '192.168.0.1'
int(ipaddress.IPv4Address('192.168.0.1'))
# 3232235521
str(ipaddress.IPv6Address('::1'))
# '::1'
int(ipaddress.IPv6Address('::1'))

# ipaddress.ip_interface - allows you to create an object
# ipaddress.ip_interface
int1 = ipaddress.ip_interface('10.0.1.1/24')

int1.ip
IPv4Address('10.0.1.1')

int1.network
IPv4Network('10.0.1.0/24')
 
int1.netmask
IPv4Address('255.255.255.0')


# Module usage example
IP1 = '10.0.1.1/24'
IP2 = '10.0.1.0/24'


# Hosts
list(ip_network('192.0.2.0/29').hosts())  
[IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
 IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
 IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]
list(ip_network('192.0.2.0/31').hosts())
[IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')]
list(ip_network('192.0.2.1/32').hosts())
[IPv4Address('192.0.2.1')]


# Example
IP1 = '10.0.1.1/24'
IP2 = '10.0.1.0/24'

def check_if_ip_is_network(ip_address):
    try:
        ipaddress.ip_network(ip_address)
        return True
    except ValueError:
        return False

check_if_ip_is_network(IP1)
# False
check_if_ip_is_network(IP2)
# True

# IP address of connected mobile device
import socket

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)


#  Classless Inter-Domain Routing (CIDR)
from ipaddress import IPv4Network

net = IPv4Network("192.4.2.0/24")
print(net.num_addresses)


# IPv4Address are also hashable
hash(IPv4Address("220.14.9.37"))
# 4035855712965130587

num_connections = {
    IPv4Address("220.14.9.37"): 2,
    IPv4Address("100.201.0.4"): 16,
    IPv4Address("8.240.12.2"): 4,
}


# reverse_pointer
ipaddress.ip_address("127.0.0.1").reverse_pointer
# '1.0.0.127.in-addr.arpa'
ipaddress.ip_address("2001:db8::1").reverse_pointer
# '1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'


# ipaddress.collapse_addresses(addresses)
[ipaddr for ipaddr in
ipaddress.collapse_addresses([ipaddress.IPv4Network('192.0.2.0/25'),
ipaddress.IPv4Network('192.0.2.128/25')])]
[IPv4Network('192.0.2.0/24')]

# ipaddress.get_mixed_type_key(obj)
IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')


from ipaddress import IPv4Network
net = IPv4Network("192.4.2.0/24")
net.num_addresses
# 256

net.prefixlen
# 24

# netmask
net.netmask
IPv4Address('255.255.255.0')

net = IPv4Network("192.4.2.0/24")
IPv4Address("192.4.2.12") in net
# True
IPv4Address("192.4.20.2") in net
# False

net.network_address
# IPv4Address('192.4.2.0')

net.prefixlen
# 24
net.netmask
# IPv4Address('255.255.255.0')  # 11111111 11111111 11111111 00000000

IPv4Network("192.4.2.0/255.255.255.0")
# IPv4Network('192.4.2.0/24')

net.broadcast_address
# IPv4Address('192.4.2.255')

net = IPv4Network("100.64.0.0/10")
net.num_addresses
# 4194304
net.netmask
# IPv4Address('255.192.0.0')
