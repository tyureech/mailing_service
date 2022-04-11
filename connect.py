import requests
from requests.auth import HTTPBasicAuth
from requests_jwt import JWTAuth
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODA3Njg3ODAsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkFsZWtzZXlUdXJpY2hldiJ9.GXQt5Vsgt-z2v634Q75tAxsMmmebWECUdxV0sEpf10o'


auth = JWTAuth(token)
response = requests.post('https://probe.fbrq.cloud/v1/send/12',
                         # auth=HTTPBasicAuth(0),
                         headers={'Authorization': f'Bearer {token}',
                                  'Content-Type': 'application/json',
                                  'accept': 'application/json'},
                         json={
                             "id": 12,
                             "phone": 9652138071,
                             "text": "Hello World!"
                         },
                         verify=False)
print(response.json())
