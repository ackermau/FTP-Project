import socket
import os

path = os.getcwd()
buffer_size = 1024
command_ip_s = ""
while (command_ip_s == ""):
    connect = input('Enter Command: ')
    if (connect != ""):    
        if  connect.split()[0].upper() == 'CONNECT':
            command_ip_s = connect.split()[1]
            command_port_s = connect.split()[2]
        else:
            print('Invalid Command: try CONNECT')

command_ip_s = command_ip_s.replace("<", "")
command_ip_s = command_ip_s.replace(">", "")
command_port_s = command_port_s.replace("<", "")
command_port_s = command_port_s.replace(">", "")
# command_ip = bytes(command_ip_s)
command_port = int(command_port_s)

command_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
command_socket.connect((command_ip_s, command_port))

def list():
    command_socket.send(cmd.encode('utf-8'))
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.bind((command_ip_s, command_port - 1))

    data_socket.listen()

    connection_socket, addr = data_socket.accept()

    response = connection_socket.recv(buffer_size).decode('utf-8')
    
    print(response)

    data_socket.close()

def retrieve(f_name):
    command_socket.send(cmd.encode('utf-8'))
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.bind((command_ip_s, command_port - 1))

    data_socket.listen()

    connection_socket, addr = data_socket.accept()
    with open(f_name, "wb") as f:
        while True:
            response = connection_socket.recv(buffer_size)
            if not response:
                break
            f.write(response)

    data_socket.close()

def store(f_name):
    f = open(f_name, 'r')
    data = f.read(buffer_size)
    f_cmd = cmd + " " + data
    command_socket.send(f_cmd.encode('utf-8'))

    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.bind((command_ip_s, command_port - 1))

    data_socket.listen()
    connection_socket, addr = data_socket.accept()
    
    response = connection_socket.recv(buffer_size).decode('utf-8')
    print(response)

    data_socket.close()
    

def quit():
    command_socket.send(cmd.encode('utf-8'))
    command_socket.close()

print('Connected...')
while True: 
    cmd = input('Enter command: ')
    if (cmd.split()[0].upper() == 'LIST'):
        list()
    elif (cmd.split()[0].upper() == 'RETR'):
        cmd = cmd.replace("<", "")
        cmd = cmd.replace(">", "")
        retrieve(cmd.split()[1])
    elif (cmd.split()[0].upper() == 'STOR'):
        cmd = cmd.replace("<", "")
        cmd = cmd.replace(">", "")
        store(cmd.split()[1])
    elif (cmd.split()[0].upper() == 'QUIT'):
        quit()
        break
    else:
        print("Invalid command.")

# def command_loop():
#     cmd = input('Enter command: ')
#     command_socket.send(cmd.encode('utf-8'))

#     response = command_socket.recv(buffer_size).decode('utf-8')
#     print(response)

# data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# data_socket.bind((command_ip_s, command_port - 1))

# data_socket.listen()

# connection_socket, addr = data_socket.accept()

# response = connection_socket.recv(buffer_size).decode('utf-8')
# print(response)

# data_socket.close()
# command_socket.close()

