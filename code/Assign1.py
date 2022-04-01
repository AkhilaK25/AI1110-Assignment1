import matplotlib.pyplot as plt
import numpy as np

def f(n):
  #function to check whether it is a factor of the polynomial or not
  k=(2*n*n*n)+(3*n*n)-(9*n)-10
  
  if k == 0:
    if k<0:
      print("x +",-1*n," is a factor of the polynomial")
    else:
      print("x -",n," is a factor of the polynomial")
  
  else:
    if k<0:
      print("x +",-1*n," is not a factor of the polynomial")
    else:
      print("x -",n," is not a factor of the polynomial")
  return 0
x=input("enter the number: ")
f(float(x))

x = np.linspace(-4,4,100)
y = 2*x**3+3*x**2-9*x-10

plt.plot(x, y, 'b', label = "y=2x^3+3x^2-9x-10")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.legend(loc = "upper left")
plt.title('Graph of the polynomial y=2x^3+3x^2-9x-10')
plt.show()
