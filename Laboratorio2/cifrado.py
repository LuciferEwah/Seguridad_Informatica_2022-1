from funciones import *
import os
import hashlib


def algoritmo_cifrado(mensaje):
    mensaje = mensaje.replace(' ', '').lower()	# Se guarda el mensaje en miniscula y sin espacios #
    mensaje = rot_cifrado(mensaje,20)
    mensaje_vigenere = vigenere(mensaje,'hellomoto','cifrado')
    cifrado_completo = vigenere(mensaje_vigenere,'monomarcelo','cifrado')
    return cifrado_completo

if __name__ == '__main__':
    file = open("mensajedeentrada.txt", "r")
    mensajeDeEntrada = file.readline().replace(' ', '').lower()
    hash = hashlib.md5(mensajeDeEntrada.encode('utf-8')).hexdigest() #hash de mensaje de entrada
    file.close()
    MensajeCodificado = algoritmo_cifrado(mensajeDeEntrada)
    print(hash)
    file = open("mensajeseguro.txt", "w+")
    file.write(MensajeCodificado + '\n' + hash)
    



    