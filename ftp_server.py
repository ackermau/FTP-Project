import os
import socket
import threading

def cmd_handler(connection_socket):
    while True:
        m = connection_socket.recv(buffer_size).decode('utf-8')
        cmd = m.split()[0]
        if (cmd.upper() == 'LIST'):
           list()
        elif (cmd.upper() == 'RETR'):
            file_name = m.split()[1]
            retrieve(file_name)
        elif (cmd.upper() == 'STOR'):
            file_name = m.split()[1]
            store(file_name, m, cmd)
        elif (cmd.upper() == 'QUIT'):
            quit()
            break

def list():
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((command_ip, command_port - 1))
    try:
        dir_list = os.listdir(os.getcwd())
        list = '\n'.join(dir_list)
        data_socket.send(list.encode('utf-8'))
        data_socket.close()
    except:
        print('failed creating list')
        data_socket.close()

def retrieve(f_name):
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((command_ip, command_port - 1))
    try:
        f = open(f_name, 'r')
        data = f.read(buffer_size)
        data_socket.send(data.encode('utf-8'))
        data_socket.close()
    except:
        print('failed sending file')
        data_socket.close()

def store(f_name, m, cmd):
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((command_ip, command_port - 1))
    with open(f_name, "w", encoding='utf-8') as f:
        data = m
        data = data.replace(cmd, "")
        data = data.replace(f_name, "")
        f.write(data)
    if (data != ""):   
        data_socket.send('file stored'.encode('utf-8'))
        data_socket.close()
    else:
        print('failed storing file')
        data_socket.close()

def quit():
    print("connection terminated.")
    # command_socket.close()
    pass

command_ip = '216.171.56.60'
command_port = 7857 
buffer_size = 1024

command_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
command_socket.bind((command_ip, command_port))

command_socket.listen()

while True:
    connection_socket, addr = command_socket.accept()
    threading.Thread(target=cmd_handler, args=(connection_socket,)).start()
    