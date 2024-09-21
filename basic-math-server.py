#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def rearrange_equation(data):
    if data.startswith('+'): # Checks if data starts with + or -
        data = data[1:] # Removes the + or -
        numbers = data.split(':') # Takes out the ":"
        data = '+'.join(numbers) # Puts + in between
        return data
    elif data.startswith('-'): # See line 9
        data = data[1:]
        numbers = data.split(':')
        data = '-'.join(numbers)
        return data
    else:
        print("error! please try again later ^-^")

def addition_or_subtraction(data):
    if "+" in data:
        print("requested operation is addition")
    elif "-" in data:
        print("requested operation is subtraction")

def extract_arguments(data):
    data = data[1:] # Removes the + or - symbol since client checked position of "+" and "-"
    data_bits = data.split(':')
    numeric_bits = [part for part in data_bits if part.isdigit()]
    arguments = ' '.join(numeric_bits)
    return arguments

def num_of_arguments(data):
    return sum(char.isdigit() for char in data)

def evaluate_expression(equation):
    result = eval(equation)
    result = str(result)
    print("result of operation: " + result)
    return result


print("basic math server starting - listening for connections at IP", HOST, "and port", PORT)
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
            data.decode('utf-8') # to remove the 'b' in front of the print
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            data = data.decode('utf-8')
            addition_or_subtraction(data)
            number = num_of_arguments(data)
            print('request includes ', end = "") # Had weird bugs with printing so I added this, gives number of arguments and arguments
            print(number, end="")
            print(' arguments: ', end = "")
            print(extract_arguments(data))
            
            equation = rearrange_equation(data)
            result = evaluate_expression(equation)
            # print("result of operation: " + result)
            
            full_equation = equation + "=" + result
            print("sending result message " + full_equation)
            data = full_equation
            conn.sendall(data.encode('utf-8'))
            # conn.sendall("I'm not home!".encode('utf-8'))
            print("server is done!")



