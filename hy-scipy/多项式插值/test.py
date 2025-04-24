from Interpolate import Lagrange_Interpolation,Neville_Interpolation,Newton_Interpolation,Hermite_Interpolation
from Piecewise_Interpolate import Piecewise_Interpolation,Piecewise_show
import numpy as np

# 定义测试数据
X_test = [3.2, 9, 16]
y_test = [12, 23, 3]

# 初始化模型
Lagrangemodel = Lagrange_Interpolation(X_test,y_test)

x = [0.0,12,20]
# 进行预测
y_pred = Lagrangemodel(x)
# 输出预测结果
print(y_pred)


Lagrange_Interpolation(X_test,y_test).show_poly()
Lagrangemodel.save_plot()


Nevillemodel = Neville_Interpolation(X_test,y_test)
Ny = Nevillemodel(x)
print(Ny)

Nevillemodel.show_poly()
Nevillemodel.save_plot()


Newtonmodel = Newton_Interpolation(X_test,y_test)
Ny = Newtonmodel(x)
print(Ny)
Newtonmodel.show_poly()
Newtonmodel.save_plot()



x_test = [0,1,2,3]
fx = [1,7,4,2]
fxx = [2,4,4,4]

Hermitemodel = Hermite_Interpolation(x_test,fx,fxx)
Hy = Hermitemodel(x)
print(Hy)
Hermitemodel.show_poly()
Hermitemodel.save_plot()
