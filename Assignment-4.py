# program to plot PDF
import numpy as np 
import matplotlib.pyplot as plot

#defining the Cdf
def F(x):
  if(x>1) and (x<6):
    return (x-1)/5;
  else:
    return 0  

    #plotting Cdf 
X = np.linspace(-8,8,100000)

Y = [F(x) for x in X]
plot.xlabel('y')
plot.ylabel('$F(y)$')
plot.plot(X,Y)
plot.grid()
plot.savefig('Assignment4.png' , dpi=125)
plot.show()    