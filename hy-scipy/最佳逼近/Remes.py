import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from numpy import poly1d
"""
[a, b]对f求n次最佳一致逼近多项式。
max_iter: 最大迭代次数

返回:
最佳逼近多项式的系数
"""


class Remes:
    def __init__(self, f, a, b, n, max_iter=10, mu=1e-5, num_points=10000, epsilon=1e-5):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.mu = mu
        self.mun_points = num_points
        self.max_iter = max_iter
        self.epsilon = epsilon

    
    def __call__(self):
        f = self.f
        a = self.a
        b = self.b
        n = self.n
        max_iter = self.max_iter
        epsilon = self.epsilon
        mu = self.mu
        num_points = self.mun_points

        return f,a,b,n,max_iter,mu,num_points,epsilon
    

    def solve(self, initial_guess = None):
        f,a,b,n,max_iter,mu,num_points,epsilon = self.__call__()

        initial_guess = np.zeros(self.n + 2)
        initial_guess[-1] = mu
        x = np.linspace(a, b, n + 2)
        for _ in range(max_iter):
            x.sort()
            signs = (-1) ** np.arange(n + 2)
        
            def equations(vars):
                p_coeffs = vars[:-1]
                mu = vars[-1]
                A = np.vander(x, n + 1, increasing=True)
                residuals = f(x) - A @ p_coeffs - signs * mu
                return residuals


            result = fsolve(equations, initial_guess)
            p_coeffs = result[:-1]
            mu = result[-1]
            initial_guess = result.copy()

            p = np.poly1d(p_coeffs[::-1])

            # 寻找新的极值点
            x_fine = np.linspace(a, b, num_points)
            errors = np.abs(f(x_fine) - p(x_fine))
            max_error_index = np.argmax(errors)
            new_point = x_fine[max_error_index]

        
            if np.abs(errors[max_error_index] - np.abs(mu)) < epsilon:
                break

            # 更新交错点
            if new_point not in x:
                def alternating_condition_violation(index):
                    if index == 0:
                        return np.abs((f(x[index]) - p(x[index])) + (f(x[index + 1]) - p(x[index + 1])))
                    elif index == n + 1:
                        return np.abs((f(x[index]) - p(x[index])) + (f(x[index - 1]) - p(x[index - 1])))
                    else:
                        return np.abs((f(x[index]) - p(x[index])) + (f(x[index + 1]) - p(x[index + 1])) +
                                  (f(x[index]) - p(x[index])) + (f(x[index - 1]) - p(x[index - 1])))

                violations = [alternating_condition_violation(i) for i in range(n + 2)]
                replace_index = np.argmax(violations)
                x[replace_index] = new_point

        return p_coeffs[::-1]


    def show_ploy(self, num=2):
        p_coeffs = self.solve()
        p_show = show(p_coeffs)
        p_show.show_poly(num=num)


    def show_plot(self):
        f,a,b,n,max_iter,mu,num_points,epsilon = self.__call__()
        p_coeffs = self.solve()
        p_show = show(p_coeffs)
        p_show.show_plot(a,b,f)


    def save_plot(self, save_path='./Remes_interpolation.png'):
        f,a,b,n,max_iter,mu,num_points,epsilon = self.__call__()
        p_coeffs = self.solve()
        p_show = show(p_coeffs)
        p_show.save_plot(a,b,f, save_path=save_path)



class show():
    def __init__(self, coeffs):
        self.coeffs = coeffs
    
    def show_poly(self, num=2):
        coeffs = self.coeffs
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


    def save_plot(self, a, b, f, save_path='./Remes_interpolation.png'):
        p = poly1d(self.coeffs)
        plot_x = np.linspace(a-0.1*a, b+0.1*b, 1000)
        plot_y = p(plot_x)
        plot_f = f(plot_x)
        plt.plot(plot_x, plot_y, label='Remes_Interpolation')
        plt.plot(plot_x, plot_f, label='f(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
        plt.savefig(save_path)
        plt.close()


    def show_plot(self, a, b, f):
        p = poly1d(self.coeffs)
        plot_x = np.linspace(a-0.1*a, b+0.1*b, 1000)
        plot_y = p(plot_x)
        plot_f = f(plot_x)
        plt.plot(plot_x, plot_y, label='Remes_Interpolation')
        plt.plot(plot_x, plot_f, label='f(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
        plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.5)
        plt.show()

