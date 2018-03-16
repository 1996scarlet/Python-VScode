import socket
ip_port = ('172.20.61.99',12345)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
while True:
    inp = input('数据：').strip()
    if inp == 'exit':
        break
    sk.sendto(bytes(inp,encoding = "utf-8"),ip_port)

sk.close()