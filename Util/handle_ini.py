import os
import configparser
class HandleInit:
    def load_ini(self):
        base_path = os.path.abspath(os.path.dirname(os.getcwd()))
        file_path = base_path + "\Config\server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf
    def get_value(self,key,section=None):
        if section == None:
            section = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(section,key)
        except Exception:
            print('别乱填')
            data = None
        return data
get_ini = HandleInit()
if __name__ == '__main__':
    get_ini = HandleInit()
    a = get_ini.get_value('username')
    print(a)
    print(len(a))