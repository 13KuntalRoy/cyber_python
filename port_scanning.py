import socket
print("hhghjv")

s = socket.socket()

result = s.connect_ex(("www.google.com", 8090))

if(result == 0):
  print('Port is open')
else:
  print('Port is closed')