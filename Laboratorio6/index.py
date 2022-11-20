from flask import Flask, render_template
import rsa, gamal, random

app = Flask(__name__)

####rsa
p,q = rsa.pyq()
n=p*q
ø=(p-1)*(q-1)
e=rsa.calculae(ø)
d=rsa.congruente(e,ø)

key_public=[n,e]
key_private=[n,d]


archivo = open("mensajeentrada.txt", "r")
mensaje_entrada = str(archivo.readline().upper())
archivo.close()

mensaje= mensaje_entrada
mensaje_cifrado=rsa.cifrarmensaje(mensaje,key_public)
mensaje_cifrado=str(mensaje_cifrado.strip())
mensaje_descifrado=rsa.descifrarmensaje(mensaje_cifrado,key_private)

####gamal
q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=gamal.gen_key(q)
h=gamal.power(g,key,q)

ct,p=gamal.encryption(mensaje,q,h,g)
pt=gamal.decryption(ct,p,key,q)
d_msg=''.join(pt)

  


@app.route('/',methods=["GET","POST"])
def principal():
    key_public=[n,e]
    key_private=[n,d]
    
    file = open("mensaje_recibido_rsa.txt", "w+")
    file.write(str(mensaje_descifrado))
    file.close()

    file2 = open("mensaje_recibido_gamal.txt", "w+")
    file2.write(str(d_msg))
    file2.close()

    return render_template('index.html',
    key_public=key_public,
    key_private=key_private,
    mensaje_encriptado_cliente=str(rsa.cifrarmensaje(mensaje,key_public)),
    mensajerecibido = str(mensaje_descifrado),

    mensaje_encriptado_gamal= ct,
    mensajerecibidoGamal = str(d_msg))

if __name__ == '__main__':
    app.run(debug=True)