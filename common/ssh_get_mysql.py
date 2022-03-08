#https://blog.csdn.net/github_38294021/article/details/79695426
#coding = utf-8
import pymysql
import common.file_path as ssh_path
from sshtunnel import SSHTunnelForwarder

host_jump = '123.207.159.137'
port_jump = '12222'
user_name_jump = 'xingminjie'
ssh_pk_jump = ssh_path.SSH_PATH
print(ssh_pk_jump)
host_mysql = '192.168.32.14'
port_mysql = '3306'
user_name_mysql = 'lc'
password_mysql = 'lc@123456'
database = 'lc_member'
with SSHTunnelForwarder(
        (host_jump, int(port_jump)),  # 跳板机的配置
        ssh_pkey=ssh_pk_jump,
        ssh_username=user_name_jump,
        remote_bind_address=(host_mysql, int(port_mysql))) as server:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=server.local_bind_port,
        user=user_name_mysql,
        passwd=password_mysql,
        db=database)
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
conn = pymssql.connect(host='192.168.32.14', port=3306, user=user_name_mysql, password=password_mysql, database=database)

# do something...
conn.close()
print(22)
server.close()
'''
