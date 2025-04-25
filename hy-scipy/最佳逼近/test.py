import numpy as np
from Remes import Remes


def f(x):
    return np.sin(np.pi * x**2)


slover = Remes(f,0,1,3,max_iter=1)
p_coeffs = slover.solve()
print(p_coeffs)

slover.show_ploy()
slover.save_plot()
