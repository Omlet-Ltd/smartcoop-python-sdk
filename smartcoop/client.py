import logging

import requests


logger = logging.getLogger("smartcoop.client")


class SmartCoopClient:
    def __init__(self, client_secret):
        self.client_secret = client_secret
        self.base_url = 'https://x107.omlet.co.uk/api/v1'

    def _get_headers(self):
        # Do not log the Authorization header to avoid leaking secrets.
        return {
            'Authorization': f'Bearer {self.client_secret}',
            'Content-Type': 'application/json'
        }

    def get(self, endpoint, params=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        logger.debug("GET %s params=%s", url, params)
        response = requests.get(url, headers=headers, params=params)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            logger.error(
                "GET %s failed: status=%s, body=%s",
                url,
                response.status_code,
                response.text,
            )
            raise
        return response.json()

    def post(self, endpoint, json=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        logger.debug("POST %s payload=%s", url, json)
        response = requests.post(url, headers=headers, json=json)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            logger.error(
                "POST %s failed: status=%s, body=%s, payload=%s",
                url,
                response.status_code,
                response.text,
                json,
            )
            raise
        if response.status_code != 204:
            return response.json()

    def patch(self, endpoint, json=None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        logger.debug("PATCH %s payload=%s", url, json)
        response = requests.patch(url, headers=headers, json=json)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            logger.error(
                "PATCH %s failed: status=%s, body=%s, payload=%s",
                url,
                response.status_code,
                response.text,
                json,
            )
            raise

    def delete(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()
        logger.debug("DELETE %s", url)
        response = requests.delete(url, headers=headers)
        try:
            response.raise_for_status()
        except requests.HTTPError:
            logger.error(
                "DELETE %s failed: status=%s, body=%s",
                url,
                response.status_code,
                response.text,
            )
            raise
