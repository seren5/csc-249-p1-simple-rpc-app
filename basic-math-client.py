#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def run_client():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(s):
                break

def talk_to_server(sock):
    
    
    exit_loop = False
    while exit_loop == False:
        msg = input("What (addition/subtraction) equation would you like solved? (Please enter your equation in the following format: +1:3:5 or -1:3:5. The order of the numbers matter.)")
        if msg == "quit":
            print("client quitting at operator request")
            exit(0)
        elif msg == "":
            print("You have not specified a value, please try again.")
        elif msg.startswith("+") or msg.startswith("-"):
            if ":" in msg and "0" in msg or "1" in msg or "2" in msg or "3" in msg or "4" in msg or "5" in msg or "6" in msg or "7" in msg or "8" in msg or "9" in msg:
                break
            else:
                print("Please format your equation in the following format:+1:3:5 or -1:3:5")
        else:
            print("You have not formatted your equation properly.")



    sock.sendall(msg.encode('utf-8'))
    print("message sent, waiting for reply")
    
    answer = sock.recv(1024)
    
    if not answer:
        return False
    else:
        print(f"Received response: '{answer!r}' from server -> [{len(answer)} bytes]")
        return answer



    
    
    
    
if __name__ == "__main__":
    run_client()
    print("test client is done, exiting...")   
    
    



    
    # if msg == 'quit':
    #     print("client quitting at operator request")
    #     return False
    # print(f"sending message '{msg}' to server")
    # sock.sendall(msg.encode('utf-8'))
    # print("message sent, waiting for reply")
    # reply = sock.recv(1024)
    # if not reply:
    #     return False
    # else:
    #     print(f"received reply '{reply}' from server")
    #     return reply




# print(f"Received response: '{data!r}' [{len(data)} bytes]")
# print("client is done!") 