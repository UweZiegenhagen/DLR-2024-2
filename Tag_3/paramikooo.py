import os
import paramiko
 
# Replace these variables with your specific values
host = '192.168.0.22'
port = 22
username = '<user>'
private_key_path = 'keyfile'
remote_directory_path = '/home/uwe/uploadtest'
local_directory_path = 'E:/uploadtest'
 
 
# Establish an SSH transport session
private_key = paramiko.RSAKey(filename=private_key_path)
transport = paramiko.Transport((host, port))
transport.connect(username=username, pkey=private_key)
 
# Create an SFTP client
sftp = paramiko.SFTPClient.from_transport(transport)
 
try:
    # Iterate through local files in the specified folder
    for local_file in os.listdir(local_directory_path):
        local_file_path = os.path.join(local_directory_path, local_file)
 
        # Check if the file is a CSV file
        if os.path.isfile(local_file_path): # and local_file.lower().endswith('.csv'):
            remote_file_path = os.path.join(remote_directory_path, local_file)
 
            # Upload the CSV file
            sftp.put(local_file_path, remote_file_path)
            print(f"Uploaded: {local_file} to {remote_file_path}")
 
finally:
    # Close the SFTP session and SSH transport
    sftp.close()
    transport.close()