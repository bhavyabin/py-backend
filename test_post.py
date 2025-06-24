import requests

url = 'https://in.docs.wps.com/module/common/preview/?sid=sIKH83rZR8b6hwQY/l/sIKH83rZR8b6hwQY?readonly&amp;disablePlugins'
headers = {
    "access-control-allow-origin": "https://in.docs.wps.com"
}

x = requests.get(url)

print(x.text)