import os
import unittest
from Util.handle_excel import excel_data
from Base.base_request import request_base
from Util.handle_ini import get_ini
class RunMian:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows-1):
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[5]
                url = data[4]
                data1 = data[6]
                res = request_base.run_main(method,url,data1)
                print(method)
                print(url)
                print(data1)
                print(res)
if __name__ == '__main__':
    run = RunMian()
    run.run_case()