#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
    print("Usage: vrfy.py <userlist_file> <target_ip>")
    sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
ip = sys.argv[2]
connect = s.connect((ip, 25))

# Receive the banner
banner = s.recv(1024)
print(banner.decode())

# Read usernames from the file
userlist_file = sys.argv[1]
try:
    with open(userlist_file, 'r') as file:
        for line in file:
            user = line.strip().encode()  # Strip newline characters and encode
            if user:
                s.send(b'VRFY ' + user + b'\r\n')
                result = s.recv(1024)
                print(f"VRFY {user.decode()}: {result.decode()}")
except FileNotFoundError:
    print(f"File {userlist_file} not found.")
    sys.exit(1)

# Close the socket
s.close()
