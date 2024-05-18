"""gputil"""
import numpy as np


def write_matrix_binary(filename, matrix, x=None, y=None):
  if x is None:
    x = np.linspace(0, 1, matrix.shape[1])
  if y is None:
    y = np.linspace(0, 1, matrix.shape[0])
  gnuplot_matrix = np.zeros((matrix.shape[0] + 1, matrix.shape[1] + 1))
  gnuplot_matrix[0] = len(x)
  gnuplot_matrix[0, 1:] = x
  gnuplot_matrix[1:, 0] = y
  gnuplot_matrix[1:, 1:] = matrix
  with open(filename, 'wb') as file:
    gnuplot_matrix.astype('float32').tofile(file)


if __name__ == '__main__':
  n, m = 50, 80
  test_matrix = np.random.random((n, m))
  print(test_matrix.shape)
  write_matrix_binary('test.dat', test_matrix)
