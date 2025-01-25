""""

O expoente de Lyapunov averigua a sensibilidade do sistema perante as condições
iniciais e, assim, mostra se um atrator é caótico. Para calcular o expoente
de Lyapunov, utilizamos a seguinte equação:

lambda_{L} = \lim_{n \rightarrow \infty} (1/n)\sum_{i=0}^{n-1}ln|f'(x_{i})|

onde, aqui, f(x_{i}) = x_{i+1}. Para lambda_{L} negativo a trajetória converge
e a evolução não é caótica, se lambda_{L} é positivo então a evolução é sensí-
vel as condições iniciais e a evolução é caótica.

"""

import numpy as np
import matplotlib.pyplot as plt

#função do mapa logístico
def logistic_map(x, r):
    return r * x * (1 - x)

#função para calcular a derivada da função logística
def logistic_map_derivative(x, r):
    return r - 2 * r * x

#função para calcular lambda para um valor de r
def lyapunov(r):
    #inicializando uma lista para armazenar os valores de derivada
    diff_values = []

    #avalia se a trajetória é caótica ou não para a condição inicial escolhida
    x = 0.6

    #número de iterações para calcular a derivada
    n = 1000

    #calculando a derivada para vários valores de x
    for _ in range(n):
        derivada = logistic_map_derivative(x, r)
        diff_values.append(derivada)
        x = logistic_map(x, r)

    #calculando lambda usando a expressão fornecida
    lambda_L = np.mean(np.log(np.abs(diff_values)))

    return lambda_L

#intervalo de valores de r
r_values = np.linspace(0, 4, 400)

#calculando lambda para cada valor de r
lambda_values = [lyapunov(r) for r in r_values]


# Plotando lambda em função de r
plt.figure(figsize=(10, 6))
plt.axhline(y=0, color='red', linestyle='--')
plt.plot(r_values, lambda_values, color='blue')
plt.title('Expoente de Lyapunov')
plt.xlabel('r')
plt.ylabel('Lambda')
plt.grid(True)
plt.show()