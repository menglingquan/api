import hashlib
import os
data = '123' #这里放入要加密的字符串文字。
obj = hashlib.md5()
obj.update(data.encode('utf-8'))
result = obj.hexdigest()
print(result)
print('***获取当前目录***')
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))

print ('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd()))+"\config\data.json")
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print ('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))