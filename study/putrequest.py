import requests
import json
base_url = "https://api.ent-dev.kuban.io"
url = base_url+"/managements/v1/user_books/337"
header = {
    'ContentType': 'Application/Jason',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjQsInZlcnNpb24iOjEsImV4cCI6MTYyNTE1MDIyNywiaWF0IjoxNTkzNTkzMjc1LCJlbnRlcnByaXNlX2lkIjpudWxsfQ.MYFx132FvEU8la3UDivGF07NC-t48AIPPG7B3_njVjc'

}
data = {
    "name": "孙da童",
    "phone_num": "16724453423",
    "email": "menglingquan@kuban.io",
    "company": "企业电竞",
    "notes": "企业电竞"
}
a = requests.put(url,params=data,headers=header)
print(a.json())


