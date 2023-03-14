# Data-Management-Application

Downloading a file from remote machine:
ftp_client=ssh_win.open_sftp() 
ftp_client.get(‘remotefileth’,’localfilepath’) 
ftp_client.close()


Uploading file from local to remote machine:
ftp_client=ssh_win.open_sftp() 
ftp_client.put(‘localfilepath’,remotefilepath’) 
ftp_client.close()

Python and SQL server connection:
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM table_name')

for i in cursor:
    print(i)
