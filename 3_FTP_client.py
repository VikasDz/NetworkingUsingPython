from ftplib import FTP

host = "your Host Name"
user = "your Username"
password = "your Password"

with FTP(host) as ftp:

    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

# For Downloading Your Data
    with open('text.txt', 'wb') as f:
        ftp.retrbinary('RETR ' + 'mytext.txt', f.write, 1024)

# For Uploading Your Data From Local to Sever 
    with open('YourFile.txt' , 'rb') as f:
        ftp.storbinary('STOR ' + 'uplaod.txt', f)


# For Uploading Your Data From Local To Sever In Specific Dic...
    ftp.cwd("YourServerDic")
    with open('YourFile.txt' , 'wb') as f:
        ftp.retrbinary('RETR ' + 'mytext.txt', f.write, 1024)



    ftp.quit()

