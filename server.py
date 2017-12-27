import socket
import datetime

HOST, PORT = '0.0.0.0', 3000

def run():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print(f'Serving at http://{HOST}:{PORT}')
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024).decode()
        http_action = request.split('\n')[0]
        request_time = datetime.datetime.now().ctime()

        print(f'{client_address[0]} - {request_time} - {http_action}')
        http_response = f"""\
HTTP/1.1 200 OK

{request}
"""
        client_connection.sendall(http_response.encode())
        client_connection.close()

if __name__ == '__main__':
    run()
