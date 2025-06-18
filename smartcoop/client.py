import requests

class SmartCoopClient:
    def __init__(self, client_secret):
        self.client_secret = client_secret
        self.base_url = 'https://x107.omlet.co.uk/api/v1'

    def _get_headers(self):
        return {
            'Authorization': f'Bearer {self.client_secret}',
            'Content-Type': 'application/json'
        }

    def get(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, json=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.post(url, headers=headers, json=json)
        response.raise_for_status()
        if response.status_code != 204:
            return response.json()

    def patch(self, endpoint, json=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.patch(url, headers=headers, json=json)
        response.raise_for_status()


    def delete(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
