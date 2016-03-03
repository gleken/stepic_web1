import os
import sys
import socket

acceptor = socket.socket()
acceptor.bind(('0.0.0.0', 2222))
acceptor.listen(10)

for i in range(10):
  pid = os.fork()
  if pid == 0:
    childpid = os.getpid()
    print "Child %s listening on localhost:4242" % childpid
    try:
      while 1:
       
        conn, addr = acceptor.accept()
        data=conn.recv(1024)
        if not data:break
          if data == "close" or data == "Close"" conn.close()
          conn.send(data)
          
          conn.close()
         
    except KeyboardInterrupt: sys.exit()


try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    print "\nbailing"
    sys.exit()
