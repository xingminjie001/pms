import json
from common.check import JsonCompare
from common import myassert
class CheckDetail:
    def __init__(self,case_id,ignore_key,sheet_name,content):
        self.case_id = case_id
        self.ignore_key = ignore_key
        self.sheet_name = sheet_name
        self.content = json.loads(content)
    def check_detail(self):
        expected_result = myassert.get_log_content(self.ignore_key, self.case_id, self.sheet_name)  # 预期
        actual_result = myassert.del_content(self.ignore_key, self.content)  # 实际
        check1 = JsonCompare(expected_result, actual_result)
        check2 = JsonCompare(actual_result, expected_result)

        if check1.data_compare_result == [] and check2.data_compare_result == []:
            pass
        else:
            raise Exception("接口返回值异常" + str(check1.data_compare_result) + str(check2.data_compare_result))
