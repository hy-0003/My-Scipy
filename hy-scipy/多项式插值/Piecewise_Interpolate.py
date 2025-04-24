import numpy as np
from numpy import poly1d
import matplotlib.pyplot as plt



class Piecewise_Interpolation:
    def __init__(self, x, y, fxx=None):
        self.x = np.array(x)
        self.y = np.array(y)
        self.fxx = np.array(fxx) if fxx is not None else None


    def div_f(x,fx,fxx,P):
        M = len(x)
        Piecewise_polynomials = []
        for i in range(M-1):
            sub_x = [x[i],x[i+1]]
            sub_fx = [fx[i],fx[i+1]]
            sub_fxx = [fxx[i],fxx[i+1]]
            Piecewise_polynomials.append(P(sub_x,sub_fx,sub_fxx))

        def piecewise_poly_func(input_x):
            if isinstance(input_x, np.ndarray):
                result = np.zeros_like(input_x, dtype=float)
                for j, val in enumerate(input_x):
                    for i in range(M - 1):
                        if val >= x[i] and val <= x[i + 1]:
                            result[j] = Piecewise_polynomials[i](val)
                            break
                return result
            else:
                for i in range(M - 1):
                    if input_x >= x[i] and input_x <= x[i + 1]:
                        return Piecewise_polynomials[i](input_x)

        return piecewise_poly_func        
    

    def div_f_P(x,fx,fxx,P):
        M = len(x)
        Piecewise_polynomials = []
        for i in range(M-1):
            sub_x = [x[i],x[i+1]]
            sub_fx = [fx[i],fx[i+1]]
            sub_fxx = [fxx[i],fxx[i+1]]
            Piecewise_polynomials.append(P(sub_x,sub_fx,sub_fxx))

        return Piecewise_polynomials


    def show_poly(*args, num=2):
        if len(args) == 4:
            x, fx, fxx, P = args
            P = Piecewise_Interpolation.div_f_P(x, fx, fxx, P)
        elif len(args) == 1:
            P = args[0]
        else:
            raise ValueError("参数数量不正确，请传入 1 个或 4 个参数")
    
        plot = Piecewise_show(P)
        plot.show_piecewise_poly(num)


    def show_plot(x, fx, fxx, P):
        p = Piecewise_Interpolation.div_f(x, fx, fxx, P)
        Piecewise_show.show_plot(x, fx, fxx, p)


    def save_plot(x, fx, fxx, P, save_path='./piecewise_interpolation.png'):
        p = Piecewise_Interpolation.div_f(x, fx, fxx, P)
        Piecewise_show.save_plot(x, fx, fxx, p, save_path)



class Piecewise_show():
    def __init__(self, P):
        self.P = P
    

    def show_piecewise_poly(self, num=2):
        P = self.P
        def show_poly(p, num=2):
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

            return result

        for p in P:
            print(show_poly(p,num))




    def save_plot(self, x, fx, P, save_path='./piecewise_interpolation.png'):
        plot_x = np.linspace(min(x)-0.1*min(x), max(x)+0.1*max(x), 1000)
        plot_y = P(plot_x)
        plt.plot(plot_x, plot_y, label='Interpolation')
        plt.scatter(x, fx, label='Data Points', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
        plt.savefig(save_path)
        plt.close()


    def show_plot(self, x, fx, fxx):
        plot_x = np.linspace(min(x)-0.1*min(x), max(x)+0.1*max(x), 1000)
        p = self.P
        plot_y = p(plot_x)
        plt.plot(plot_x, plot_y, label='Interpolation')
        plt.scatter(x, fx, label='Data Points', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
        plt.show()