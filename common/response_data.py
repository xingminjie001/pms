from common.xml_format import XmlFormat
from common.compress import Compress
class Responsedata:
    def __init__(self,response,post_data,logger,case_id):
        self.response = response
        self.post_data = post_data
        self.logger = logger
        self.case_id = case_id
    def handle_data(self):
        post_data = Compress().uncompress_data(self.post_data)
        post_data = XmlFormat().xml_to_json(post_data)
        response_data = self.response.content.decode('utf-8')
        response_data = Compress().uncompress_data(response_data)
        response_data = XmlFormat().xml_to_json(response_data)
        # 日志
        self.logger.info("case_id" + str(self.case_id) + '请求时间为' + str(self.response.elapsed.microseconds))
        self.logger.info("case_id" + str(self.case_id) + "入参" + post_data)
        self.logger.info("case_id" + str(self.case_id) + "出参" + response_data)
        return response_data
