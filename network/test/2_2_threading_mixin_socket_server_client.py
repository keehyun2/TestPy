import os
import socket
import threading
import socketserver

SERVER_HOST = 'dm1587858100882.clserver.co.kr'
SERVER_PORT = 24803
BUF_SIZE = 1024

def client(ip, port, message):
    ''' A client to test threading mixin server '''
    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message.encode())
        response = sock.recv(BUF_SIZE)
        print('Client received 1차 응답: %s' % response.decode())
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.connect((ip, port))
        # sock.sendall(response.decode())
        # response = sock.recv(BUF_SIZE)
        # print('Client received 2차 응답: %s' % response.decode())
    finally:
        sock.close()


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    ''' An example of threaded TCP request handler '''
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = '%s: %s' % (cur_thread.name, data.decode())
        self.request.sendall(response.encode())


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    ''' Nothing to add here, inherited everything necessary from parents '''
    pass

if __name__ == "__main__":
    # run server
    # server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    # ip, port = server.server_address # retrieve ip address
    # start a thread with the server -- one thread per request
    # server_thread = threading.Thread(target=server.serve_forever)
    # # Exit the server thread when the main thread exits
    # server_thread.daemon = False
    # server_thread.start()
    # print('Server loop running on thread: %s' % server_thread.name)
    # run clients
    client(SERVER_HOST, SERVER_PORT, "안녕하세요.")

    # client(SERVER_HOST, SERVER_PORT, "uhghsghjgasd")
    # client(SERVER_HOST, SERVER_PORT, "asdhjhjkzxc")
    # server cleanup
    # server.shutdown()
