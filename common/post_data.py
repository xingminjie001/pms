import json,re,time
from common.xml_format import XmlFormat
from common.compress import Compress
from common.request_update import Update_all
class Postdata:
    def __init__(self,data,associate_id,get_param,set_param,sheet_name):
        self.data = data
        self.associate_id = associate_id
        self.get_param = get_param
        self.set_param = set_param
        self.sheet_name = sheet_name
    def handle_data(self):
        # 判断是否整体压缩
        if self.data.startswith('H4'):
            self.data = Compress().uncompress(self.data)  # 入参解压
        if self.associate_id != "" and self.associate_id != "date":#判断是否需要修改入参
            id_list = self.associate_id.split(',')
            get_param_list = self.get_param.split(',')
            set_param_list = self.set_param.split(',')
            for id, get_param, set_param in zip(id_list, get_param_list, set_param_list):
                if '<'+set_param+'>'in self.data:
                    self.data = XmlFormat().xml_to_json(self.data)
                    self.data = Update_all().update_all(self.sheet_name, id, self.data, get_param, set_param)
                    self.data = XmlFormat().json_to_xml(json.dumps(self.data))  # json转为xml
                else:
                    middlle_xml = re.search(r'H4(.*?)<',self.data).group()
                    if middlle_xml:
                        middle_json = XmlFormat().xml_to_json(Compress().uncompress_data(middlle_xml))
                        datas = Update_all().update_all(self.sheet_name, id, middle_json, get_param,set_param)
                        datas = XmlFormat().json_to_xml(json.dumps(datas))  # json转为xml
                        datas = datas.replace('<?xml version="1.0" encoding="utf-8"?>','')
                        datas = Compress().compress(datas).decode('utf-8')
                        self.data = re.sub(r'H4(.*?)<',datas+'<',self.data)
        elif self.associate_id == "date":  # 判断是否需要修改日期
            self.data = re.sub('1900-01-01', time.strftime("%Y-%m-%d", time.localtime()), self.data)
        return self.data
if __name__ == '__main__':
    content ={'handleDto': {}, 'responseCommonDto': {'resvNo': None, 'errorLevel': '0', 'invokerEndTime': 4938829387425979, 'lans': None, 'message': '000000', 'resultCode': '0', 'sessionKey': None, 'token': '6af80826-eba3-4e45-bb32-78b40541fef4', 'tracerId': None, 'userUid': None}, 'resultData': [{'acctNo': ['F0010160'], 'arrDt': None, 'breakFlg': None, 'dptDt': None, 'errorFlg': '0', 'errorRoomNums': None, 'noShareRoomNums': None, 'resvNo': 'R0010134', 'shareAcctNos': None, 'shareFlg': None, 'shareRoomNums': None, 'shareSeq': 'S0010160'}]}
    print(content.__contains__('acctNo'))