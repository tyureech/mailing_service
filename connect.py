import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODA3Njg3ODAsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkFsZWtzZXlUdXJpY2hldiJ9.GXQt5Vsgt-z2v634Q75tAxsMmmebWECUdxV0sEpf10o'
response = requests.post('https://probe.fbrq.cloud/v1/send/1',
                         headers={'Authorization': 'token {}'.format(token) +token},
                         json={
                             "id": 12,
                             "phone": +79872139061,
                             "text": "Hello World!"
                         },
                         verify=False)
print(response)
