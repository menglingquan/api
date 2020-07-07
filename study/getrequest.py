import requests
base_url = "https://api.ent-dev.kuban.io"
url = base_url+"/managements/v1/location_groups"
header = {
    'ContentType': 'Application/Jason',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjQsInZlcnNpb24iOjEsImV4cCI6MTYyNTE1MDIyNywiaWF0IjoxNTkzNTkzMjc1LCJlbnRlcnByaXNlX2lkIjpudWxsfQ.MYFx132FvEU8la3UDivGF07NC-t48AIPPG7B3_njVjc'

}
data = {
    "page": "1",
    "per_page": "3"
}
a = requests.get(url,params=data,headers=header)
print(a.json())
print(a.elapsed.total_seconds())
print(a.status_code)