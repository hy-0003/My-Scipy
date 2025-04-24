import numpy as np
from numpy import poly1d
import matplotlib.pyplot as plt



class Interpolate:
    def __init__(self, x, y, fxx=None):
        self.x = np.array(x)
        self.y = np.array(y)
        self.fxx = np.array(fxx) if fxx is not None else None


class show():
    def __init__(self, p):
        self.p = p
    
    def show_poly(self, p, num=2):
        p = self.p
        coeffs = p.coeffs
        terms = []
        degree = len(coeffs) - 1
        for i, coeff in enumerate(coeffs):
            power = degree - i
            if coeff == 0:
                continue
        # 处理系数符号
            sign = '-' if coeff < 0 else '+' if terms else ''
            abs_coeff = abs(coeff)
            abs_coeff = f"{abs_coeff:.{num}f}"

            if power == 0:
                terms.append(f"{sign}{abs_coeff}")
            elif power == 1:
                if abs_coeff == 1:
                    terms.append(f"{sign}x")
                else:
                    terms.append(f"{sign}{abs_coeff}x")
            else:
                if abs_coeff == 1:
                    terms.append(f"{sign}x^{power}")
                else:
                    terms.append(f"{sign}{abs_coeff}x^{power}")
    
        result = ''.join(terms)

        if result.startswith('+'):
            result = result[1:]

        print(result)


    def save_plot(self, x, y, save_path='./interpolation.png'):
        plot_x = np.linspace(min(x)-0.1*min(x), max(x)+0.1*max(x), 1000)
        plot_y = self.p(plot_x)
        plt.plot(plot_x, plot_y, label='Interpolation')
        plt.scatter(x, y, label='Data Points', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
        plt.savefig(save_path)
        plt.close()


    def show_plot(self, x, y):
        plot_x = np.linspace(min(x)-0.1*min(x), max(x)+0.1*max(x), 1000)
        plot_y = self.p(plot_x)
        plt.plot(plot_x, plot_y, label='Interpolation')
        plt.scatter(x, y, label='Data Points', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
        plt.show()



class Lagrange_Interpolation(Interpolate):
    def __call__(self, x):
        x = np.array(x)
        y = np.zeros_like(x)
        for i in range(len(x)):
            y[i] = self.lagrange_basis(self.x, self.y)(x[i])
        return y
    
    def lagrange_basis(self, x, y):
        M = len(x)
        p = poly1d(0.0)
        for j in range(M):
            pt = poly1d(y[j])
            for k in range(M):
                if k == j:
                    continue
                fac = x[j]-x[k]
                pt *= poly1d([1.0, -x[k]])/fac
            p += pt
        return p


    def show_poly(self,num=2):
        l_show = show(self.lagrange_basis(self.x, self.y))
        l_show.show_poly(self, num=num)


    def save_plot(self,save_path='./lagrange_interpolation.png'):
        l_show = show(self.lagrange_basis(self.x, self.y))
        l_show.save_plot(self.x, self.y, save_path=save_path)


    def show_plot(self):
        l_show = show(self.lagrange_basis(self.x, self.y))
        l_show.show_plot(self.x, self.y)



    
class Neville_Interpolation(Interpolate):
    def __call__(self, x):
        x = np.array(x)
        y = np.zeros_like(x)
        for i in range(len(x)):
            y[i] = self.neville_basis(self.x, self.y)(x[i])
        return y

    def neville_basis(self, x, y):
        M = len(x)
        p = poly1d([1.0,0.0])
        def f(a, b, p=p):
            if a == b:
                p_0 = poly1d(y[a])
                return p_0
            else:
                left_term = ( poly1d([x[b]]) - p) * f(a, b-1, p)
                right_term = (p - poly1d([x[a]]) ) * f(a+1, b, p)
                denominator = x[b] - x[a]
                return ( left_term + right_term ) / denominator
            
        return f(0,M-1,p)
    

    def show_poly(self,num=2):
        n_show = show(self.neville_basis(self.x, self.y))
        n_show.show_poly(self, num=num)


    def save_plot(self,save_path='./neville_interpolation.png'):
        n_show = show(self.neville_basis(self.x, self.y))
        n_show.save_plot(self.x, self.y, save_path=save_path)


    def show_plot(self):
        n_show = show(self.neville_basis(self.x, self.y))
        n_show.show_plot(self.x, self.y)




class Newton_Interpolation(Interpolate):
    def __call__(self, x):
        x = np.array(x)
        y = np.zeros_like(x)
        for i in range(len(x)):
            y[i] = self.newton_basis(self.x, self.y)(x[i])
        return y
    
    def newton_basis(self, x, y):
        M = len(x)
        p_x = poly1d([1.0,0.0])
        p = poly1d([y[0]])
        def f(x,y,i,j):
            if i==j:
                return poly1d([y[i]])
            else:
                return (f(x,y,i+1,j)-f(x,y,i,j-1))/(x[j]-x[i])
        
        for j in range(1,M):
            p_1 = poly1d(1.0)
            for i in range(j):
                p_1 = p_1 * (p_x-poly1d( [x[i]] ) )
            p = p + p_1 * f(x,y,0,j)

        return p

    def show_poly(self,num=2):
        n_show = show(self.newton_basis(self.x, self.y))
        n_show.show_poly(self, num=num)


    def save_plot(self,save_path='./newton_interpolation.png'):
        n_show = show(self.newton_basis(self.x, self.y))
        n_show.save_plot(self.x, self.y, save_path=save_path)


    def show_plot(self):
        n_show = show(self.newton_basis(self.x, self.y))
        n_show.show_plot(self.x, self.y)



class Hermite_Interpolation(Interpolate):
    def __call__(self, x):
        x = np.array(x)
        y = np.zeros_like(x)
        for i in range(len(x)):
            y[i] = self.hermite_basis(self.x, self.y, self.fxx)(x[i])
        return y
    
    def hermite_basis(self, x, fx, fxx):
        M = len(x)
        p = poly1d([1.0,0.0])
        def lx(x,i):
            sum = 1
            for j in range(M):
                if j != i:
                    sum = sum * (x[i]-x[j])
            return sum
        def ls(p,x,i):
            sum = poly1d(1.0)
            for j in range(M):
                if j != i:
                     sum = sum * ( p-poly1d([x[j]]) )
            return sum
        def l(p,x,i):
            return ls(p,x,i)/lx(x,i)

        def a(p,x,i):
            sum = 0
            for j in range(M):
                if j == i:
                   sum =sum
                if j != i:
                   sum = sum + 1/(x[i]-x[j])
            return (1-2*(p-poly1d([x[i]]))*sum)*l(p,x,i)*l(p,x,i)
        def b(p,x,i):
             return (p-poly1d([x[i]]))*l(p,x,i)*l(p,x,i)
        
        sum = poly1d(0.0)
        for i in range(M):
            sum =sum + a(p,x,i)*fx[i] + b(p,x,i)*fxx[i]
        return sum
    

    def show_poly(self,num=2):
        n_show = show(self.hermite_basis(self.x, self.y, self.fxx))
        n_show.show_poly(self, num=num)


    def save_plot(self,save_path='./hermite_interpolation.png'):
        n_show = show(self.hermite_basis(self.x, self.y, self.fxx))
        n_show.save_plot(self.x, self.y, save_path=save_path)


    def show_plot(self):
        n_show = show(self.hermite_basis(self.x, self.y, self.fxx))
        n_show.show_plot(self.x, self.y)