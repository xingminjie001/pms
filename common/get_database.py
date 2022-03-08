# -*- coding: utf-8 -*-
from common.readconfig import ReadConfig
import pymssql
from common.login import Login

readconfig=ReadConfig()


class Database():
    def __init__(self):

        self.sqlserver = readconfig.get_config_section_dict('sqlserver')
        self.backup = readconfig.get_config_section_dict('backup')
        self.restore = readconfig.get_config_section_dict('restore')




    def huanyuan(self,sheet_name):  # 数据库还原
        con = pymssql.connect(self.sqlserver['ip'], self.sqlserver['username'], self.sqlserver['password'],
                              self.sqlserver['database'], autocommit=True)
        cur = con.cursor()
        cur.execute(self.restore['sql'])
        con.commit()
        cur.close()
        con.close()
        cookie = Login(sheet_name).get_cookies()
        if cookie == None:
            cookie = Login(sheet_name).get_cookies()



    def beifen(self):  #数据库备份
        con = pymssql.connect(self.sqlserver['ip'], self.sqlserver['username'], self.sqlserver['password'],
                              self.sqlserver['database'], autocommit=True)
        cur = con.cursor()
        cur.execute(self.backup['sql'])
        con.commit()
        cur.close()
        con.close()


if __name__ == '__main__':
    Database().huanyuan('')


