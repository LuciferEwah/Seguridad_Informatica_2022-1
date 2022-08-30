import string
diccionario = string.ascii_lowercase
def rot5(mensaje):
    aux = ''
    for i in mensaje:
        aux = aux + diccionario[(diccionario.find(i) + 5 ) % len(diccionario)]
    return aux

def rot18(mensaje):
    aux = ''
    for i in mensaje:
        aux = aux + diccionario[(diccionario.find(i) + 18 ) % len(diccionario)]
    return aux

def rot_18(mensaje):
    aux = ''
    for i in mensaje:
        aux = aux + diccionario[(diccionario.find(i) - 18 ) % len(diccionario)]
    return aux

def rot_5(mensaje):
    aux = ''
    for i in mensaje:
        aux = aux + diccionario[(diccionario.find(i) - 5 ) % len(diccionario)]
    return aux

def vigenere(mensaje,clave_original,modo):
    clave = ''
    cifrado = ''
    descifrado = ''

    if len(mensaje)>len(clave_original):	# Si la logitud del mensaje es mayor que la de la clave... #
        for i in range(int(len(mensaje)/len(clave_original))):		## Se alarga la clave, duplicándola y		 ##
            clave += clave_original									## concatenándosela a sí misma, hasta que su ##
        clave += clave_original[:len(mensaje)%len(clave_original)]	## longitud sea la misma que la del mensaje  ##

    elif len(mensaje)<len(clave_original):	# Si la longitud del mensaje es menor que la de la clave...
        clave = clave_original[:len(mensaje)]	# Se trunca la clave para que tenga la misma longitud que el mensaje #

    elif len(mensaje)==len(clave_original):	# Si la longitud del mensaje es igual que la de la clave... #
        clave = clave_original	# Se guarda la clave tal cual se encuentra en 'clave_original' #

    else:
        print ('Ha ocurrido un error inesperado. Terminando ejecución...')
    if modo == 'cifrado':
        for i in range(len(mensaje)):
            x = diccionario.find(mensaje[i])	# Se guarda la posición del caracter del mensaje en el abecedario
            y = diccionario.find(clave[i])	# Se guarda la posición del caracter de la clave en el abecedario
            suma = x+y	# Se calcula la suma de ambas posiciones
            modulo = suma%len(diccionario)	# Se calcula el módulo de la suma respecto a la longitud del abecedario
            cifrado += diccionario[modulo]	# Se concatena el caracter cifrado con 'cifrado'
        return cifrado
    elif modo == 'descifrado':
        for i in range(len(mensaje)):
            x = diccionario.find(mensaje[i])	# Se guarda la posición del caracter del mensaje cifrado en el abecedario
            y = diccionario.find(clave[i])	# Se guarda la posición del caracter de la clave en el abecedario
            resta = x-y	# Se calcula la resta de ambas posiciones
            modulo = resta%len(diccionario)	# Se calcula el módulo de la resta respecto a la longitud del abecedario
            descifrado += diccionario[modulo]	# Se concatena el caracter descifrado con 'descifrado'
        return descifrado
    else:
        pass
    
def algoritmo_cifrado():
    mensaje = str(input("Introduzca el mensaje a cifrar:"))
    mensaje = mensaje.replace(' ', '').lower()	# Se guarda el mensaje en miniscula y sin espacios #
    clave_original = str(input("Introduzca la palabra clave: "))
    clave_original = clave_original.replace(' ', '').lower()	# Se guarda la clave en mayúsculas y sin espacios #
    modo = 'cifrado'
    mensaje_rot5 = rot5(mensaje)
    mensaje_vigenere = vigenere(mensaje_rot5,clave_original,modo)
    cifrado_completo = rot18(mensaje_vigenere)
    
    print('El mensaje cifrado es el siguiente: ')
    return cifrado_completo

def algoritmo_descifrado():
    mensaje = str(input("Introduzca el mensaje a descifrado:"))
    mensaje = mensaje.replace(' ', '').lower()	# Se guarda el mensaje en miniscula y sin espacios #
    clave_original = str(input("Introduzca la palabra clave: "))
    clave_original = clave_original.replace(' ', '').lower()	# Se guarda la clave en mayúsculas y sin espacios #
    modo = 'descifrado'
    mensaje_rot_18 = rot_18(mensaje)
    mensaje_vigenere = vigenere(mensaje_rot_18,clave_original,modo)
    descifrado_completo = rot_5(mensaje_vigenere)
    print('El mensaje descifrado es el siguiente: ')
    return descifrado_completo

if __name__ == '__main__':
    print(algoritmo_cifrado())
    print(algoritmo_descifrado())