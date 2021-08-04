import numpy as np
import os

#uncomment this line of code if you get an error
#os.system('pip install galois')
import galois


def CreateField(order, char):
  GF = galois.GF(order)
  
  if char and GF.characteristic != char:
    raise Exception("Characteristic does not match order of field. Expected: " + str(GF.characteristic) + ", received: "  +str(char))

  GF.int_map = {}
  x = GF.primitive_element
  n = 1
  while n != 0:
    GF.int_map[int(x)] = n+1
    x = np.multiply(x, GF.primitive_element)
    n = (n+1)%order
  GF.int_map[0] = 0
  GF.int_map[1] = 1

  GF.ToOrdering = lambda x : GF.int_map[int(x)]

  return GF

def CreatePolynomial(GF, coeffs):
  return galois.Poly(coeffs, GF)

def GetDegree(poly):
  poly.degree

def Hat(GF, N):
  return GF.order**N

def _next(GF, coeffs):
  order = GF.order
  for i in range(len(coeffs)):
    if coeffs[i] == order - 1:
      coeffs[i] = 0
    else:
      coeffs[i] += 1
      break
  else:
    return False

  return True

def Iter(GF, N):
  coeffs = [0 for i in range(N+1)]
  yield CreatePolynomial(GF, coeffs)
  while _next(GF, coeffs):
    yield CreatePolynomial(GF, coeffs)

def PolyToInt(GF, poly):
  ret = 0
  print (poly)
  for coeff in list(poly.coeffs):
    ret *= GF.order
    ret += GF.ToOrdering(coeff)

  return ret

def IntToPoly(GF, n):
  print("int to poly is still work in progress")

if __name__ == "__main__":
  GF = CreateField(4, 2)

  arr = []
  for c in Iter(GF, 3):
    arr.append(c)

  print(PolyToInt(GF, arr[10]))