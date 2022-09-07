from funciones import *

def algoritmo_descifrado(mensaje):
    MensajeModificado = vigenere(mensaje,'monomarcelo','descifrado')
    mensaje_vigenere = vigenere(MensajeModificado,'hellomoto','descifrado')
    descifrado_completo = rot_descifrado(mensaje_vigenere,20)
    return descifrado_completo

if __name__ == '__main__':
    archivo = open("mensajeseguro.txt",'r')
    archivo_leido = archivo.readlines()
    archivo.close()
    mensaje = archivo_leido[0].replace('\n',"")
    hash_cifrado = archivo_leido[1]
    MensajeCodificado = algoritmo_descifrado(mensaje)
    hash_decifrado = hashlib.md5(MensajeCodificado.encode('utf-8')).hexdigest()

    if hash_cifrado == hash_decifrado: 
        print('El mensaje no fue adulterado')
    else: 
        print('El mensaje fue adulterado, PELIGRO!')




    

