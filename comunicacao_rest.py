import requests

# a = requests.get('https://gui25.github.io/lab/')
# a = requests.get('https://www.google.com')
a = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
if 'json' in a.headers['Content-Type']:
    print('Sou um JSON\n\n')
    print(a.json())
else:
    print('Sou qualquer outra coisa\n\n')
    print(a.text)
# requests.post('https://www.google.com.br')
