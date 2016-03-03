import socket
import os
import time
import sys


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 2222))
s.listen(10)
conn, addr = s.accept()

pid=os.fork()
if pid!=0:
	time.sleep(10)
	sys.exit(0)

while True:
	data = conn.recv(1024)
	if not data:
		break
		if data == "Close" or data == "close": conn.close()
		conn.send(data)

conn.close()
