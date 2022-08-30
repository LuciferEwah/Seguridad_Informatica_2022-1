import requests
headers = {
    'Content-Type': 'text/plain',
}
data = '{"msg":"qltauhlufkxpmctclhvyrouesixyfpjpcsjhsxela(holaprofenosecomosubirmensajesasuservidor)"}'
response = requests.post('http://lab1.seguridad.xn--ensea-rta.cl/SendMsg', headers=headers, data=data)