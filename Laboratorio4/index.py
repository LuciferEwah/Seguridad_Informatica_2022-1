from Crypto.Cipher import DES
from secrets import token_bytes
from flask import Flask, render_template, request
import os

app = Flask(__name__)
g = 421
p = 601
key = token_bytes(8)	#(solo 8)
iv = token_bytes(8)	# Vector de inicialización

# Creó un objeto de cifrado DE DES

file = open("Laboratorio4\mensajeentrada.txt", "r")
# Datos necesarios
mensaje_entrada = str(file.readline().lower()).encode()
file.close()
print(mensaje_entrada)
cipher1 = DES.new(key, DES.MODE_CFB, iv)

mensaje_codificado = cipher1.encrypt(mensaje_entrada)
print(mensaje_codificado)

file = open("Laboratorio4\Mensaje_Codificado.txt", "w+")
file.write(str(mensaje_codificado))
file.close()

# Creó un objeto de descifrado (descifrado cifrado no puede usar la misma clave)
cipher2 = DES.new(key, DES.MODE_CFB, iv)
mensaje_recibido = cipher2.decrypt(mensaje_codificado).decode()
print(mensaje_recibido)
file = open("Laboratorio4\mensajerecibido.txt", "w+")
file.write(mensaje_recibido)
file.close()

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
    