import numpy as np


def write_matrix_binary(filename, A, x=None, y=None):
  if x is None:
    x = np.linspace(0, 1, A.shape[1])
  if y is None:
    y = np.linspace(0, 1, A.shape[0])
  if filename is None:
    filename='test.dat'
  M = np.zeros((A.shape[0]+1, A.shape[1]+1))
  M[0] = len(x)
  M[0, 1:] = x
  M[1:, 0] = y
  M[1:, 1:] = A
  with open(filename, 'wb') as file:
    M.astype('float32').tofile(file)


if __name__ == "__main__":
  n, m=50,50
  A=np.random.random((n,m))
  print(A.shape)
  x=np.linspace(0, 20, m)
  y=np.linspace(0, 1, n)
  write_matrix_binary('test.dat', A)
