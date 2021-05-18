# Method-2 ; for both upper and lower case
## ENCODING
from collections import deque

al=[chr(i) for i in range(65,ord('Z')+1)]
al1=[chr(j) for j in range(97,ord('z')+1)]

org=[chr(i) for i in range(65,ord('Z')+1)]
org1=[chr(j) for j in range(97,ord('z')+1)]

org=deque(org)
org1=deque(org1)

message=input('Enter the message to be encoded: ')
shift=int(input("key: "))
st=""

org.rotate(-1*shift)
org1.rotate(-1*shift)


for j in message:
    if j.isalnum():
        if j.isupper():
            st+=org[al.index(j)]
        else:
            st+=org1[al1.index(j)]
    else:
        st+=j

print(st)

##DECODING

from collections import deque

al=[chr(i) for i in range(65,ord('Z')+1)]
al1=[chr(j) for j in range(97,ord('z')+1)]

org=[chr(i) for i in range(65,ord('Z')+1)]
org1=[chr(j) for j in range(97,ord('z')+1)]

org=deque(org)
org1=deque(org1)


message=input('Enter the msg to be decoded: ')
key=int(input("key: "))
st=""

org.rotate(key)
org1.rotate(key)

for j in message:
    if j.isalnum():
        if j.isupper():
            st+=org[al.index(j)]
        else:
            st+=org1[al1.index(j)]

    else:
        st+=j

print(st)
