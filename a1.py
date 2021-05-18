# Method-1
## ENCODING

message=input('Message to be encoded :')
shift=int(input('key: '))
st=""
message=message.upper()
print(message)
for i in message:
    if i.isalnum():
        y=ord(i)+shift
        if y>ord('Z'):
            y=y-ord('Z')+64
            print(y,ord('Z'),end=' ')
            print(chr(y))            
        st+=chr(y)
    else:
        st+=i
print(st)

## DECODING

message=input('Message to be decoded :')
key=int(input('key: '))
st=""
message=message.upper()
print(message)
for i in message:
    if i.isalnum():
        y=ord(i)-key
        if y<ord('A'):
            y=ord('Z')-(ord('A')-y)+1
            # print(y,ord('A'),end=' ')
            # print(chr(y))            
        st+=chr(y)
    else:
        st+=i
print(st)