import socket
import json

class Debugger():
  @classmethod
  def listen(cls, addr = None, port = None):
    # Settings
    addr = addr if addr else "127.0.0.1"
    port = port if port else 5055
    addr = (addr, port)
    # Start server
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Starting Debugger on %s port %s' % addr)
    try:
      sock.bind(addr)
      while True:
        data, address = sock.recvfrom(4096)
        if data:
          data=data if type(data) is str else data.decode('utf-8')
          print("[%s] %s\n"%(address[0], data))
    except KeyboardInterrupt:
      pass
    finally:
      sock.close()

  @classmethod
  def send(cls, message, addr = None, port = None):
    # Settings
    addr = addr if addr else "127.0.0.1"
    port = port if port else 5055
    addr = (addr, port)
    # Send message
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
      if type(message) is not str: message=repr(message)
      message = message.encode('utf-8')
      try:    message = json.loads(message)
      except: pass
      sock.sendto(message, addr)
    finally:
      sock.close()
    
