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
  
        # añadir todos los elementos restantes
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

class adc:
  def __init__(self,data,index):
    #para los metodos de mergesort, es necesario tambien pasarles la dimension
    #en la que estan trabajando actualmente para evitar hacer copias
    #inicio/final/dimension actual/dimensiones totales
    #breakpoint()
    self.data = data
    np.genfromtxt(file,dtype=float,delimiter=",")
    self.indexes = indexes
    print(self.data)
    print(self.indexes)

  def solve(data, e):
    #encuentra la mejor division 
    j,r,z = mejor_division(data)
    #si el decremento de impureza es lo suficientemente pequenyo
    if z > e:
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
    tl = self.solve(yl,e)
    tr = self.solve(yr,e)
    return Node(0,j,r,tl,tr)

  def mejor_division(self,data):
    j = r = None
    muestras,D = data.shape
    #me voy a disfrazar en halloween de esta linea
    split = int(self.data[0,self.index[0,len(self.index[0])//2]])
    for d in range(D-1):
      part_inferior = 1
      part_superior =  1

  def clase_dominante(data):
    c = Counter(data[:,-1])
    res,_ = c.most_common(1)
    return res

if __name__ == "__main__":
  breakpoint()
  data = np.genfromtxt(sys.argv[1],dtype=float,delimiter=",")
  #obtenemos la forma de las muestras
  muestras,D = data.shape
  #tenemos que ordenar las muestras por cada una de las dimensiones
  indexes = np.tile(np.arange(muestras),(D-1,1))
  for d in range(D-1):
    mergeSort(data[:,d],indexes[d])
  print(indexes)
  #e = input('Introduce decremento de impureza minimo: ')
  #sol = adc(np.genfromtxt(sys.argv[1],dtype=float,delimiter=","),indexes)
  



  
