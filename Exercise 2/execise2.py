# Telnet to the server


import telnetlib

try:
    conn = telnetlib.Telnet("google.com", "80")
    response = 'Success'
except:
    response = 'Failed'
finally:
    print(response)
print(conn.fileno())




# SSH to server

from paramiko import SSHClient

client = SSHClient()

client.connect('example.com', username='user', password='secret')
client.close()




# Check Disk Usage

import shutil
  
# Path
path = "C:\Users\Rohan"
  
# Get the disk usage statistics
# about the given path
stat = shutil.disk_usage(path)
  
# Print disk usage statistics
print("Disk usage statistics:")
print(stat)


# Get List of Files in Python

import os
 
# Get the list of all files and directories
path = "C:\Users\Rohan"

dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)


# Inode number of files

import os
  
  
# Directory to be scanned
path = "C:\Users\Rohan"
  
# Using os.scandir() method
# scan the specified directory
# and yield os.DirEntry object
# for each file and sub-directory
  
print("Directory entry name and their inode number") 
with os.scandir(path) as itr:
    for entry in itr :
        # Exclude the entry name
        # starting with '.'  
        if not entry.name.startswith('.') :
            # print entry name
            # and entry's inode() number 
            print(entry.name, " :", entry.inode())
			
			
			

# Copy files to the remote server using FTP


import ftplib
session = ftplib.FTP('server.address.com', 'USERNAME', 'PASSWORD')
file = open('arsenal.jpg', 'rb') #file to send
session.storbinary('STOR arsenal.jpg', file) #send the file
file.close() #close file & ftp
session.quit()


# File transfer over SSH


import OS
import paramiko

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~"), ".ssh", "known_hosts")))
ssh.connect(server, username=username, password=password)
sttp = ssh.open_sftp()
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()

