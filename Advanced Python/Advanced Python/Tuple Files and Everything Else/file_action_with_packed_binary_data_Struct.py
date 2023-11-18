import struct

with open('data.bin', mode='wb') as file:
    data = struct.pack('>i4sh', 7, b'spam', 8)
    file.write(data)
    file.close()

print(data)
