import random

def verifica_primo(n):
	c=0
	x=2
	if n>=2:
		while x<=n/2:
			if n%x==0:
				c=c+1
				x=x+1
			else:
				x=x+1
		if c==0:
			return True
		else:
			return False
	else:
		return False

def genera_primos(n):
	lp=[]
	x=2
	while n!=0:
		if verifica_primo(x)==True:
			lp.append(x)
			x=x+1
			n=n-1
		else:
			x=x+1
	return lp


def pyq():
	lista_primos=genera_primos(100)
	p= int(random.choice(lista_primos))
	q= int(random.choice(lista_primos))
	lpq=[p,q]
	return lpq
	
def calculae(ø):
	e=2
	le=[]
	while e>1 and e<ø :
		if mcd(e,ø)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1
	e= int(random.choice(le))
	return e

def mcd(e,ø):
	m=ø%e
	while m!=0:
		ø=e
		e=m
		m=ø%e
	return e

def congruente(e,ø):
	k=1
	m=(1+(k)*(ø))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(ø))%(e)
	d=int((1+(k)*(ø))/(e))
	return d

def cifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split(" ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=cifrarpalabra(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc

def cifrarpalabra(m,k):
	lpc=[]
	lp=[]
	n,e=k
	cpc=""
	for i in m:
		x=buscarpos(i)
		lp.append(x)
	for j in lp:
		c=(j**e)%n
		lpc.append(c)
	for k in lpc:
		cpc=cpc+str(k)+" "
	return cpc	

def buscarpos(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==i:
			return c
		else:
			c=c+1	

def descifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split("  ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=descifrarnumero(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc

def descifrarnumero(m,k):
	lnc=[]
	ln=[]
	n,d=k
	cnc=""
	men=m.split(" ")
	for i in men:
		x=int(i)
		ln.append(x)
	for j in ln:
		m=(j**d)%n
		lnc.append(m)
	for k in lnc:
		l=buscarlet(k)
		cnc=cnc+str(l)
	return cnc

def buscarlet(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==c:
			return i
		else:
			c=c+1	


p,q = pyq()
n=p*q
ø=(p-1)*(q-1)
e=calculae(ø)
d=congruente(e,ø)

key_public=[n,e]
key_private=[n,d]


archivo = open("mensajeentrada.txt", "r")
mensaje_entrada = str(archivo.readline().upper())
archivo.close()

mensaje= mensaje_entrada
mensaje_cifrado=cifrarmensaje(mensaje,key_public)


mensaje_cifrado=str(mensaje_cifrado.strip())
mensaje_descifrado=descifrarmensaje(mensaje_cifrado,key_private)
