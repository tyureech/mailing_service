import requests
from django.conf import settings


class Connections:
    def __init__(self):
        self.token = settings.TOKEN

    def send(self, id, phone, text):
        try:
            response = requests.post(f'https://probe.fbrq.cloud/v1/send/{id}',
                                     headers={'Authorization': f'Bearer {self.token}',
                                              'Content-Type': 'application/json',
                                              'accept': 'application/json'},
                                     json={
                                         "id": id,
                                         "phone": phone.as_e164,
                                         "text": text
                                     },
                                     verify=False,
                                     timeout=10)
            return response
        except Exception as e:
            print(e)
            return -10
