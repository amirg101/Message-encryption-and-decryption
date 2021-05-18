# Method-2
## ENCODING
from collections import deque

al=[chr(i) for i in range(65,ord('Z')+1)]
org=[chr(i) for i in range(65,ord('Z')+1)]
org=deque(org)

message=input('Enter the message to be encoded: ').upper()
shift=int(input("key: "))
st=""

org.rotate(-1*shift)

for j in message:
    if j.isalnum():
        st+=org[al.index(j)]
    else:
        st+=j

print(st)

##DECODING

from collections import deque

al=[chr(i) for i in range(65,ord('Z')+1)]
org=[chr(i) for i in range(65,ord('Z')+1)]
org=deque(org)

message=input('Enter the msg to be decoded: ').upper()
key=int(input("key: "))
st=""

org.rotate(key)

for j in message:
    if j.isalnum():
        st+=org[al.index(j)]
    else:
        st+=j

print(st)
