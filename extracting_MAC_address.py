import uuid

print (hex(uuid.getnode()))

# or
import uuid
# after each 2 digits, join elements of getnode().
print ("The formatted MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))
