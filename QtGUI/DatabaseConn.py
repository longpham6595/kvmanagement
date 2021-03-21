#Database connection

import paramiko
import os
import pymysql
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser

#Connect to Remote Server
k = paramiko.RSAKey.from_private_key_file("D:/TLDH/KVDatabase/id_rsa",password = "kvdatabaselockdown")
        
#Old codes used - Just for rethinking
'''
remoteComp = paramiko.SSHClient()
remoteComp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting...")
remoteComp.connect(hostname = "192.168.2.6", username = "LONG", pkey = k)
print("Connected!")
'''


sql_hostname = 'localhost'
sql_username = 'root'
sql_password = '0377122966longpham!'
sql_main_database = 'kvdatabase'
sql_port = 3306
ssh_host = '192.168.2.6'
ssh_user = 'LONG'
ssh_port = 22
sql_ip = '1.1.1.1.1'

with SSHTunnelForwarder(
     (ssh_host,ssh_port),ssh_username = ssh_user,
      ssh_pkey=k,
      remote_bind_address = (sql_hostname,sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1',user=sql_username,
                         passwd=sql_password,db=sql_main_database,
                         port=tunnel.local_bind_port)
    # Check if database is connected Command - obmit if Connection establish fine at first check!!
    print('Kvdatabase connected!!!')
    cursor = conn.cursor()

    #Test commands establish to database!! Obmit if command establish fine!!
    cursor.execute('SELECT * FROM kvdatabase.dshocsinh;')
    records = cursor.fetchall()
    for row in records: 
        print(row[0],' ',row[1],' ',row[2])

    cursor.close()
    conn.close()
