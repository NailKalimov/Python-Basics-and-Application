"""https://httpbin.org/legacy"""

import requests

# params = {'arg1': "value1", 'arg2': "value2"}
# r = requests.get("https://httpbin.org/get", params)
# print(r.url, r.status_code)
# print(r.json())
#
# r = requests.post("http://httpbin.org/post", params)
# print(r.url, r.status_code)
# print(r.text)
#
# response = requests.options('https://httpbin.org/redirect-to?url=foo')
# print(response.status_code)
# print(response.headers)
# print(response.headers['Allow'])

response = requests.get('https://httpbin.org/redirect-to', data={'url': 'http://example.com/'})
print(response.status_code)
print(response.content)





# github_url = "https://api.github.com/user/repos"
# data = json.dumps({'name': 'test', 'description': 'some test repo'})
# r = requests.post(github_url, data, auth=('user', '*****'))
#
# print(r.json)
