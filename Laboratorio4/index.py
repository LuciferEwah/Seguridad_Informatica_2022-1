from Crypto.Cipher import DES, DES3
from secrets import token_bytes
from flask import Flask, render_template, request
import os

app = Flask(__name__)
g = 421
p = 601

keydes = token_bytes(8)	#(solo 8 para des y 3des solo 24
keydes3 = token_bytes(24)	#(solo 8 para des y 3des solo 24
iv = token_bytes(8)	# Vector de inicialización

archivo = open("Laboratorio4\mensajeentrada.txt", "r")
mensaje_entrada = str(archivo.readline().lower()).encode()
archivo.close()

# Creó un objeto de cifrado DE DES
def cifrado_des(texto,key,iv):
    cipher1 = DES.new(key, DES.MODE_CFB, iv)
    mensaje_codificado = cipher1.encrypt(texto)
    # Creó un objeto de descifrado (descifrado cifrado no puede usar la misma clave)
    return mensaje_codificado

def descifrado_des(texto,key,iv):
    cipher2 = DES.new(key, DES.MODE_CFB, iv)
    mensaje_recibido = cipher2.decrypt(texto).decode()
    return str(mensaje_recibido)

def descifrado_des(texto,key,iv):
    cipher2 = DES.new(key, DES.MODE_CFB, iv)
    mensaje_recibido = cipher2.decrypt(texto).decode()
    file = open("Laboratorio4\mensaje_recibido_des.txt", "w+")
    file.write(str(mensaje_recibido))
    file.close()
    return str(mensaje_recibido)

def cifrado_des3(texto,key,iv):
    cipher1 = DES3.new(key, DES3.MODE_CFB, iv)
    mensaje_codificado = cipher1.encrypt(texto)
    # Creó un objeto de descifrado (descifrado cifrado no puede usar la misma clave)
    return mensaje_codificado

def descifrado_des3(texto,key,iv):
    cipher2 = DES3.new(key, DES3.MODE_CFB, iv)
    mensaje_recibido = cipher2.decrypt(texto).decode()
    file = open("Laboratorio4\mensaje_recibido_des3.txt", "w+")
    file.write(str(mensaje_recibido))
    file.close()
    return str(mensaje_recibido)

mensaje_cifrado_des3 = cifrado_des3(mensaje_entrada,keydes3,iv)
mensaje_cifrado_des = cifrado_des(mensaje_entrada,keydes,iv)


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
    mensaje_descifrado_des = descifrado_des(mensaje_cifrado_des,keydes,iv)
    mensaje_descifrado_des3 = descifrado_des3(mensaje_cifrado_des3,keydes3,iv)
    file = open("Laboratorio4\mensaje_recibido_des3.txt", "w+")
    file.write(str(mensaje_cifrado_des3))
    file.close()
    file = open("Laboratorio4\mensaje_recibido_des.txt", "w+")
    file.write(str(mensaje_cifrado_des))
    file.close()
    return render_template('cliente/index.html',g=g,p=p,K1=K1,K2=K2,mensaje1=mensaje_descifrado_des,mensaje2=mensaje_descifrado_des3)

if __name__ == '__main__':
    app.run(debug=True)