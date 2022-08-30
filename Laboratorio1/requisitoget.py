import requests
headers = {
    'Content-Type': 'text/plain',
}
response = requests.get('http://lab1.seguridad.xn--ensea-rta.cl/GetMsg', headers=headers)