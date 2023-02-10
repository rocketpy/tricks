import ipaddress
# IPv4/IPv6 manipulation library
# https://pypi.org/project/ipaddress/

#  IP address representations:
from __future__ import unicode_literals

ipaddress.ip_address('1.2.3.4')
IPv4Address(u'1.2.3.4')
 

# Arithmetic Operation on IPv4 address
print(ipaddress.IPv4Address(u'129.117.0.0')-6)
print (ipaddress.IPv4Address(u'175.199.42.211')+55)
print (ipaddress.IPv4Address(u'0.0.0.0')-1)
print (ipaddress.IPv4Address(u'255.255.255.255')+1)
 
  
# Arithmetic Operation on IPv6 address
print (ipaddress.IPv6Address(u'0000::0000')-1)
print (ipaddress.IPv6Address(u'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')+1)
print (ipaddress.IPv6Address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334')-330)
print (ipaddress.IPv6Address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334')+1000)

