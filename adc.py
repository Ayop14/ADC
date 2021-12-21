import numpy as np
import csv
import sys
from collections import Counter


class Node:
  def __init__(self,clase,D,r,izq,der):
    self.clase = clase
    self.D = D
    self.r = r
    self.izq = izq
    self.der = der

def mergeSort(arr,indexes):
    if len(arr) > 1:
        #breakpoint()
         # encontramos la mitad de la lista
        mid = len(arr)//2
        # Dividimos la lista en dos mitades
        L = arr[:mid].copy();Li = indexes[:mid].copy()
        R = arr[mid:].copy();Ri = indexes[mid:].copy()
        # ordenamos ambas mitades
        mergeSort(L,Li)
        mergeSort(R,Ri)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                indexes[k] = Li[i]
                i += 1
            else:
                arr[k] = R[j]
                indexes[k] = Ri[j]
                j += 1
            k += 1
  
        # anyadir todos los elementos restantes
        while i < len(L):
            arr[k] = L[i]
            indexes[k] = Li[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            indexes[k] = Ri[j]
            j += 1
            k += 1

def adc(data, indexes,e):
  #encuentra la mejor division 
  j,r,z = mejor_division(data,indexes)
  #si el decremento de impureza es lo suficientemente pequenyo
  if z < e:
    #entonces buscamos la clase dominante
    c = clase_dominante(data)
    #lo declaramos como un nodo lo suficientemente puro
    return Node(c,None,None,None,None)
  else:
    yl = yr = np.array([])
    for muestra in data:
      if muestra[j] <= r:
        yl = yl.concatenate(muestra)
      else:
        yr = yr.concatenate(muestra)
  tl = adc()
  tr = adc()
  return Node(0,j,r,tl,tr)

def mejor_division(data,indexes):
  j = r = z = None
  muestras,D = data.shape
  #hallamos el indice intermedio
  indice = len(indexes[0])//2
  #recorremos cada una de las dimensiones
  for d in range(D-1):
    #calculamos el umbral como la media del intermedio y el anterior
    #len([1,2]) = 2 ->//2 = 1 -> si lo hicieramos con el siguiente daria error,
    #y si el array es de longitud par entonces no estariamos calculando el intermedio
    #len([1,2,3,4]) = 4//2=2 arr[2] -> 3a posicion-> pos-1 operamos con 2 y 3 
    raux = (indexes[d,indice] + indexes[d,indice-1])/2
    jaux = d
    zaux = decremento_impureza(data,indexes,jaux)
    if(j is None or zaux > z):
      j,r,z = jaux,raux,zaux
  return (j,r,z)

#evaluamos la calidad de la particion usando la entropia como medida
def decremento_impureza(data,indexes,j):
  indice = len(indexes[j])//2
  entr = entropia(data)
  #esto de poder indexar listas CON LISTAS me parece increible
  entrL = entropia(data[indexes[j,:indice]])
  entrR = entropia(data[[indexes[j,indice:]])
  return (entr - entrL*len(indexes[j,:indice]) - enterR*len([indexes[j,indice:]))

def entropia(data):
  #para cada una de las clases
  C = np.unique(data[:,-1],return_counts = True)
  N,_ = data.shape
  suma = 0
  #calculamos el sumatorio de la entropia
  #c = clase, Nc = n elementos de esa clase, N = n elementos total
  for c,Nc in C:
    suma += (Nc/N * np.log2(Nc/N))
  #al devolverlo, lo tenemos que volver positivo:
  return (-suma)


def clase_dominante(data):
  c = Counter(data[:,-1])
  res,_ = c.most_common(1)
  return res

if __name__ == "__main__":
  data = np.genfromtxt(sys.argv[1],dtype=float,delimiter=",")
  #obtenemos la forma de las muestras
  muestras,D = data.shape
  #tenemos que ordenar las muestras por cada una de las dimensiones
  indexes = np.tile(np.arange(muestras),(D-1,1))
  for d in range(D-1):
    mergeSort(data[:,d],indexes[d])
  e = input('Introduce decremento de impureza minimo: ')
  sol = adc(np.genfromtxt(sys.argv[1],dtype=float,delimiter=","),indexes,e)
  



  
