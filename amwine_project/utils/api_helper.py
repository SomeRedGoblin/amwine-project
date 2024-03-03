import json

import allure
import requests
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions


def do_request(method: str, base_url: str, url: str = None, **kwargs) -> requests:
    current_url = base_url + url
    with allure.step(f'{method.upper()} {base_url}{url}'):
        with sessions.Session() as session:
            resp = session.request(method=method, url=current_url, **kwargs)
            if resp.headers['Content-Type'] == 'text/html; charset=UTF-8':
                # allure.attach(body=resp.text.encode('utf8'), name='html_response',
                #               attachment_type=AttachmentType.HTML, extension='html')
                return resp
            message = to_curl(resp.request)
            allure.attach(body=message.encode('utf8'), name='Curl',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            if resp.text == '':
                allure.attach(body=resp.text.encode('utf8'), name='empty_response',
                              attachment_type=AttachmentType.JSON, extension='json')
                return resp
            allure.attach(body=json.dumps(resp.json(), indent=4).encode('utf8'), name='response',
                          attachment_type=AttachmentType.JSON, extension='json')
    return resp


def headers() -> dict:
    return {'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/121.0.0.0 Safari/537.36'
            }
