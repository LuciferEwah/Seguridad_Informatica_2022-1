from Crypto.Cipher import DES, DES3, AES
from secrets import token_bytes
from flask import Flask, render_template, request
import os

app = Flask(__name__)
g = 421
p = 601

keydes = token_bytes(8)	#(solo 8 para des y 3des solo 24
keydes3 = token_bytes(24)	#(solo 8 para des y 3des solo 24
keyAES = token_bytes(16) 
iv = token_bytes(8)	# Vector de inicialización

archivo = open("Laboratorio5\mensajeentrada.txt", "r")
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
    return str(mensaje_recibido)

def cifrado_des3(texto,key,iv):
    cipher1 = DES3.new(key, DES3.MODE_CFB, iv)
    mensaje_codificado = cipher1.encrypt(texto)
    # Creó un objeto de descifrado (descifrado cifrado no puede usar la misma clave)
    return mensaje_codificado

def cifrado_AES(mensaje):
    cipher = AES.new(keyAES, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(mensaje) #toma mensajes como bytes
    return nonce, ciphertext, tag

def descifrado_AES(nonce, ciphertext, tag):
    cipher = AES.new(keyAES, AES.MODE_EAX, nonce=nonce)
    texto = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return texto
    except:
        return "mensaje alterado"

def descifrado_des3(texto,key,iv):
    cipher2 = DES3.new(key, DES3.MODE_CFB, iv)
    mensaje_recibido = cipher2.decrypt(texto).decode()
    return str(mensaje_recibido)

mensaje_cifrado_des3_AES = cifrado_des3(mensaje_entrada,keydes3,iv)
nonce, mensaje_cifrado_des3_AES, tag = cifrado_AES(mensaje_cifrado_des3_AES)

mensaje_cifrado_des = cifrado_des(mensaje_entrada,keydes,iv)


@app.route('/')
def principal():
    return render_template('principal/index.html',g=g,p=p)

@app.route("/servidor",methods=["GET","POST"])
def servidor():
    a = 234 #llave privada del sistema
    A = (g^a)%p #llave publica del sistema
    b = int(request.form.get('dato1'))#llave privada del usuario
    B  = (g^b)%p #llave publica del usuario
    #shared secret key
    K1 = (A^b)%p
    K2 = (B^a)%p
    mensaje_descifrado_des = descifrado_des(mensaje_cifrado_des,keydes,iv)
    mensaje_descifrado_des3_AES = descifrado_AES(nonce, mensaje_cifrado_des3_AES, tag)
    mensaje_descifrado_des3_AES = descifrado_des3(mensaje_descifrado_des3_AES,keydes3,iv)

    file = open("Laboratorio5\mensaje_cifrado_des3_AES.txt", "w+")
    file.write(str(mensaje_cifrado_des3_AES))
    file.close()
    file = open("Laboratorio5\mensaje_cifrado_des.txt", "w+")
    file.write(str(mensaje_cifrado_des))
    file.close()
    return render_template('cliente/index.html',
    g=g,p=p,K1=K1,K2=K2,A=A,B=B,
    mensaje1=mensaje_descifrado_des,
    mensaje2=mensaje_descifrado_des3_AES,
    codificadoDes=mensaje_cifrado_des,
    codificado3DesAES=mensaje_cifrado_des3_AES)

if __name__ == '__main__':
    app.run(debug=True)