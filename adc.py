import numpy as np

class Node:
  def __init__(self,clase,D,r,izq,der):
    self.clase = clase
    self.D = D
    self.r = r
    self.izq = izq
    self.der = der

def adc(data, e):
  #encuentra la mejor division 
  j,r,z =mejor_division(data)
  #si el decremento de impureza es muy pequeño
  if z > e:
    c = clase_dominante(data)
    return Node(c,None,None,None,None)
  else:
    yl = yr = []
    for 
  
  
  
  
if __name__ == "__main__":
  main()
