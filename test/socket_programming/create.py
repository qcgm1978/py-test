
import unittest,socket
class TDD_CREATE(unittest.TestCase):
    def test_create(self):
        # create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # now connect to the web server on port 80 - the normal http port
        s.connect(("www.python.org", 80))        
    def test_web_server(self):
        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # bind the socket to a public host, and a well-known port
        serversocket.bind((socket.gethostname(), 80))
# become a server socket
        serversocket.listen(5)
        while True:
            pass
# accept connections from outside
#             (clientsocket, address) = serversocket.accept()
# # now do something with the clientsocket
# # in this case, we'll pretend this is a threaded server
#             ct = client_thread(clientsocket)
#             ct.run()
    def test_not_end(self):
        class MySocket:
            """
            demonstration class only
            - coded for clarity, not efficiency 
            """
            def __init__(self, sock=None):
                if sock is None:
                    self.sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
                else:
                    self.sock = sock
            def connect(self, host, port): self.sock.connect((host, port))
            def mysend(self, msg):
                totalsent = 0
                while totalsent < MSGLEN:
                    sent = self.sock.send(msg[totalsent:])
                    if sent == 0:
                        raise RuntimeError("socket connection broken")
                    totalsent = totalsent + sent
            def myreceive(self):
                chunks = []
                bytes_recd = 0
                while bytes_recd < MSGLEN:
                    chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
                    if chunk == b'':
                        raise RuntimeError("socket connection broken")
                    chunks.append(chunk)
                    bytes_recd = bytes_recd + len(chunk)
                return b''.join(chunks)
if __name__ == '__main__':
    unittest.main()

                