import socket

class Client:
    def __init__(self, host, port, filename):
        self.CHUNK_SIZE = 8 * 128
        self.s = socket.socket()
        self.s.connect((host, port))
        self.s.send(b"Hello server!")
        self.f = open(filename,'rb')
        self.data = self.f.read(self.CHUNK_SIZE)
        self.i = 1
        while (self.data):
            self.s.send(self.data)
            self.data = self.f.read(self.CHUNK_SIZE)
            print(self.i)
            self.i = self.i + 1

        self.f.close()
        print('Done sending')
        self.s.send(b'Thank you for connecting')
        self.s.close()

Client("145.37.148.183", 80, "mail.pdf")