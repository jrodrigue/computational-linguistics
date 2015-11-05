import collections
import operator
import os

#declaraciones
cadena="EL/DT perro/N come/V carne/N de/P la/DT carniceria/N y/C de/P la/DT nevera/N y/C canta/V el/DT la/N la/N la/N ./Fp";
cadena = cadena.lower()
cadena_separada = cadena.split() #separo la cadena por los espacios
diccionario ={}
clases=[]
tuplaClaves = {}
datos =[]
paralabras = []
tuplaPalabras={}
n=0
vc=0
clases=[]
tuplaClaves = {}
posiciones=[]
palConteo={}
conCate={}
lcad=[x.split('/') for x in cadena.split()]
diccionario = (dict(lcad))
lista_diccionario = diccionario.items()
# print("##################")
arrayPalabras=[]
arrayClasePalabras=[]
for v,c in lcad: #vector de clases de las palabras
	# tuplaPalabras[v]=c
	arrayPalabras.append(v)
	arrayClasePalabras.append(c)
# print("##################")
nobj=len(lcad)
for i, c in lcad:
	datos.append(c)
diccionarioR= collections.Counter(datos)
listaDicc = sorted(list(diccionarioR.items()))
print("################# DICCIONARIO DE CATEGORIA ################")
for p,k in listaDicc:
	print (p, k)
print("################# DICCIONARIO CON FRECUENCIA ##############")
# dicP={}
# for v,c in lcad: #vector de clases de las palabras
# 	dicP[v]=1+dicP.get(v,0)
d={}
dic2={}

for c,v in lcad:
	dic2[c]=1+dic2.get(c,0)
	dc={}
	for clave,valor in lcad:
		if clave==c:
			dc[valor]=1+dc.get(valor,0)
		d[c]=dic2[c],dc
	del dc
for p in d:
	print (p, ": ", d[p])	

print("################# FRECUENCIA DE BIGRAMAS ##################")
# v -> valor - c -> clave
for v,c in lcad: #vector de clases de las palabras
	clases.append(c)
tam=len(clases)+1
auxiliar=""
for i in range(tam):
	if i==0:
		auxiliar = '<s>',clases[i]
	elif i==tam-1:
		auxiliar = clases[i-1],'</s>'
	else:
		auxiliar = clases[i-1],clases[i]
	tuplaClaves[i]=(auxiliar)
dicConteo={}
for k in range(len(tuplaClaves)):
	dicConteo[tuplaClaves[k]]=1+dicConteo.get(tuplaClaves[k],0)

for clave in dicConteo:
	print (clave, ": ", dicConteo[clave])
# print("###########################################################")# print(lcad)
print("###################### PROBABILIDADES LÉXICAS #############")

def calProb(palabra):
	repeticiones=0
	for i in range(0,len(arrayPalabras)):
		if arrayPalabras[i]==palabra:
			repeticiones=repeticiones +1
			posiciones.append(i)
	if repeticiones>0:
		li=d[palabra][1].items()
	print("############# Resultados de la Busqueda para la Palabra (",palabra,") #####################")
	print(" ")
	print("La palabra ",palabra," Se consiguio ", repeticiones, " Veces")
	print(" ")
	for b,n in li:
		print("P(",b.upper(),"|",palabra,") = ",n/d[palabra][0])
	for b,n in li:
		print(n/repeticiones)
	
	print(d[palabra][0]/n)
		#print("P(",palabra,"|",b.upper(),") = ",n/repeticiones)
palabra = input("Ingrese una palabra : ")
if palabra!="":
	calProb(palabra)
	print(" ")
if palabra=="":
	print("Cadena Vacia no Perimitida")
