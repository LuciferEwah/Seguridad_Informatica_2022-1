from Crypto.Cipher import DES
from secrets import token_bytes
from flask import Flask, render_template, request
import os

app = Flask(__name__)
g = 421
p = 601
file = open("Laboratorio4\mensajeentrada.txt", "r")
mensaje_entrada = file.readline().lower()
key = token_bytes(8) #(solo 8)
iv = token_bytes(8)	#Vector de inicialización
# Creó un objeto de cifrado DE DES
file = open("Laboratorio4\mensajeentrada.txt", "r")
# Datos necesarios
mensaje_entrada = str(file.readline().lower()).encode()
cipher1 = DES.new(key, DES.MODE_CFB, iv)
msg = cipher1.encrypt(mensaje_entrada)
# Creó un objeto de descifrado 
cipher2 = DES.new(key, DES.MODE_CFB, iv)
file = open("Laboratorio4\mensajeentrada.txt", "w+")
file.write( cipher2.decrypt(msg).decode() + os.linesep)

@app.route('/')
def principal():
    return render_template('principal/index.html',g=g,p=p)

@app.route("/servidor",methods=["GET","POST"])
def servidor():
    a = 234
    A = (g^a)%p
    b = int(request.form.get('dato1'))
    B  = (g^b)%p
    K1 = (A^b)%p
    K2 = (B^a)%p
    file = open("Laboratorio4\mensajerecibido.txt", "r")
    mensaje_recibido = str(file.readline().lower())
    return render_template('cliente/index.html',g=g,p=p,A=A,K1=K1,K2=K2,mensaje=mensaje_recibido)

if __name__ == '__main__':
    app.run(debug=True)
    