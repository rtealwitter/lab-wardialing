"""Run the student's scan against a local simulation, without network traffic."""
from pathlib import Path
import runpy
from unittest.mock import patch
from urllib.parse import urlsplit
import requests

RESPONDING = {'175.45.176.5', '175.45.179.250'}
visited = set()

def simulated_request(session, method, url, **kwargs):
    address = urlsplit(url).hostname
    visited.add(address)
    if address not in RESPONDING:
        raise requests.ConnectionError('Simulated address has no web server')
    response = requests.Response()
    response.status_code = 200
    return response

if __name__ == '__main__':
    with patch('requests.sessions.Session.request', simulated_request):
        runpy.run_path(str(Path(__file__).with_name('wardial.py')), run_name='__main__')
    print(f'Simulated requests: {len(visited)}; expected 1024 distinct addresses.')
    print('Expected detected servers:', sorted(RESPONDING))
