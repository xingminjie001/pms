#https://blog.csdn.net/github_38294021/article/details/79695426
#coding = utf-8
import common.file_path as ssh_path
import pymssql
from sshtunnel import SSHTunnelForwarder

host_jump = '123.207.159.137'
port_jump = '12222'
user_name_jump = 'xingminjie'
ssh_pk_jump = ssh_path.SSH_PATH
print(ssh_pk_jump)
host_mysql = '192.168.0.17'
port_mysql = '1433'
user_name_mysql = 'test_user'
password_mysql = 't543fDS#5r47'
database = 'HYHotel_test'

with SSHTunnelForwarder(
        (host_jump, int(port_jump)),  # 跳板机的配置
        ssh_pkey=ssh_pk_jump,
        ssh_username=user_name_jump,
        remote_bind_address=(host_mysql, int(port_mysql))) as server:
    conn = pymssql.connect(
        host='127.0.0.1',
        port=server.local_bind_port,
        user=user_name_mysql,
        password=password_mysql,
        database=database)
    cur = conn.cursor()
    cur.execute("show databases")
    print(cur.fetchall())



'''
server = SSHTunnelForwarder(
        (host_jump, int(port_jump)),  # 跳板机的配置
        ssh_pkey=ssh_pk_jump,
        ssh_username=user_name_jump,
        remote_bind_address=(host_mysql, int(port_mysql)))  # 数据库服务器的配置
server.start()
conn = pymssql.connect(host='127.0.0.1', port=1434, user=user_name_mysql, password=password_mysql, database=database)

# do something...
conn.close()
print(22)
server.close()
'''