# -*- coding: utf-8 -*-
import requests
from common.readconfig import ReadConfig



config = ReadConfig()

class Login:
    def __init__(self,sheet_name):
        self.timeout = config.get_config_value('apiDomain', 'timeout')
        if '销售点' in sheet_name:
            self.interface = '/touchposwebservice/TouchposWebService.asmx'
        else:
            self.interface = '/CshisNetWS/LoginService.asmx'

        self.url = config.get_config_value('apiDomain', 'domain') + self.interface
        self.sessionkey = None

        self.data=config.get_config_section_dict('LoginData')
        if '集团' in sheet_name:
            self.xml_data=self.data['cpcs_xml']
        elif '销售点' in sheet_name:
            self.xml_data=self.data['pos_xml']
        else:
            self.xml_data = self.data['cpcs01_xml']
        self.headers = config.get_config_section_dict('HEADERS')

    def get_cookies(self):
        self.response = requests.post(self.url,headers = self.headers,data = self.xml_data,timeout = float(self.timeout))
        try:
            self.cookies = self.response.cookies['ASP.NET_SessionId']
            return self.cookies
        except:
            pass
if __name__ == '__main__':
    pass
    #cookies = str(Login('销售点').get_cookies())
    #print('cookies:'+cookies)