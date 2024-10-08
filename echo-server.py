#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024) # 1024 => number of bytes
            if not data:
                break
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            print(f"echoing '{data!r}' back to client")
            conn.sendall(data)
            # conn.sendall("I'm not home!".encode('utf-8'))

print("server is done!")
