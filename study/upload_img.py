import json
import requests
import hashlib
token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjQsInZlcnNpb24iOjEsImV4cCI6MTYy' \
       'NTE1MDIyNywiaWF0IjoxNTkzNTkzMjc1LCJlbnRlcnByaXNlX2lkIjpudWxsfQ.MYFx132FvEU8la3UDivGF07NC-t48AIPPG7B3_njVjc' #这里放入要加密的字符串文字。
obj = hashlib.md5()
obj.update(token.encode('utf-8'))
token_hlb = obj.hexdigest()

base_url = "https://api.ent-dev.kuban.io"
url = base_url+"/managements/v1/meeting_rooms/169"
header = {
    'ContentType': 'Application/Jason',
    'Authorization': token

}
print(header)
print(type(header))
room_info = {
    "name": "房间111",
    "area_type": "huddle_room",
    "floor_info_id": 224,
    "capacity": 11,
    "oav_enable":"false",
    "state": "free",
    "size": 50,
    "id": 169,
    "images": ["https://media-dev-ssl.kuban.io/static/ent-web/1593670833828123123.jpg",]
}
a = requests.put(url,params=room_info,headers=header)
print(a.status_code)