from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from flask import Flask, render_template
import os
import rsa

app = Flask(__name__)


p,q = rsa.pyq()
n=p*q
ø=(p-1)*(q-1)
e=rsa.calculae(ø)
d=rsa.congruente(e,ø)

key_public=[n,e]
key_private=[n,d]


archivo = open("Laboratorio6\mensajeentrada.txt", "r")
mensaje_entrada = str(archivo.readline().upper())
archivo.close()

mensaje= mensaje_entrada
mensaje_cifrado=rsa.cifrarmensaje(mensaje,key_public)
mensaje_cifrado=str(mensaje_cifrado.strip())
mensaje_descifrado=rsa.descifrarmensaje(mensaje_cifrado,key_private)

@app.route('/',methods=["GET","POST"])
def principal():
    key_public=[n,e]
    key_private=[n,d]
    
    file = open("Laboratorio6\mensaje_recibido_rsa.txt", "w+")
    file.write(str(mensaje_descifrado))
    file.close()


    return render_template('index.html',
    key_public=key_public,
    key_private=key_private,
    mensaje_encriptado_cliente=str(rsa.cifrarmensaje(mensaje,key_public)),
    mensajerecibido = str(mensaje_descifrado))

if __name__ == '__main__':
    app.run(debug=True)