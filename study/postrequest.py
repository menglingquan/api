import requests
base_url = "https://api.ent-dev.kuban.io"
url = base_url+"/managements/v1/sessions"
header = {
    'ContentType': 'Application/Jason',

}
data = {
    "space_id": "4",
    "phone_num": "18845647728",
    "login_sms_code": "123456"
}
a = requests.post(url,data=data,headers=header)
print(a.json())