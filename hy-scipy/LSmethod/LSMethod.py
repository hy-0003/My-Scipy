import numpy as np
import matplotlib.pyplot as plt

class LSmethod:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
    
    
    def get_f(self):
        x = self.x
        y = self.y
        n = self.n
        if len(x) != len(y):
            raise ValueError("x 和 y 的长度不相等")
        

        def phi_i(x, i):
            return [x[j] ** i for j in range(len(x))]

        def get_Y(y, x, n):
            return [np.dot(y, phi_i(x, i)) for i in range(n)]
        
        def get_G(x, n):
            G = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    G[i][j] = np.dot(phi_i(x, i), phi_i(x, j))
            return G
        
        Y = np.array(get_Y(y, x, n))
        G = get_G(x, n)

        try:
            c = np.linalg.solve(G, Y)
        except np.linalg.LinAlgError:
            print("系数矩阵 G 是奇异矩阵，无法求解线性方程组。")
        p = np.poly1d(c[::-1])

        return p
    

    def get_c(self):
        x = self.x
        y = self.y
        n = self.n
        if len(x) != len(y):
            raise ValueError("x 和 y 的长度不相等")
        

        def phi_i(x, i):
            return [x[j] ** i for j in range(len(x))]

        def get_Y(y, x, n):
            return [np.dot(y, phi_i(x, i)) for i in range(n)]
        
        def get_G(x, n):
            G = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    G[i][j] = np.dot(phi_i(x, i), phi_i(x, j))
            return G
        
        Y = np.array(get_Y(y, x, n))
        G = get_G(x, n)

        try:
            c = np.linalg.solve(G, Y)
        except np.linalg.LinAlgError:
            print("系数矩阵 G 是奇异矩阵，无法求解线性方程组。")

        return c[::-1]
    

    def print_f(self, num = 2):
        c = self.get_c()
        coeffs = c
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
