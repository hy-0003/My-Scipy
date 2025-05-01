from LSMethod import LSmethod
import numpy as np


x = [1.0, 1.25, 1.50, 1.75, 2.00]
y = [np.log(5.10),np.log(5.79),np.log(6.53),np.log(7.45),np.log(8.48)]
n = 2

p = LSmethod(x, y, n).get_f()
LSmethod(x,y,n).print_f(num=3)

